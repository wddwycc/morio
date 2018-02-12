from flask import Blueprint
from flask import g
from flask import jsonify, request
from sqlalchemy import desc
from voluptuous import Coerce, Match, Length, Range, Optional
from voluptuous import Required, Any, All

from morio.core.auth import login_required, login_optional
from morio.core.error import (
    ConflictException, NotFoundError, SignatureError,
    BadRequestError,
)
from morio.core.pagination import with_pagination
from morio.model import Repository, Card, User, Course
from morio.model import db, CourseCardProgress
from .utils import retrieve_payload, retrieve_user_repo, retrieve_course

bp = Blueprint('core', __name__)


@bp.route('/users/<name>')
def get_user(name):
    src = User.query.filter_by(name=name).first()
    if not src:
        raise NotFoundError(description='User not found')
    return jsonify(src)


@bp.route('/users/<username>/repos')
@login_optional
@with_pagination
def get_repos(username):
    query = Repository.query.filter(Repository.user.has(name=username))
    if not g.user or g.user.name != username:
        query = query.filter_by(private=False)
    repos = query.order_by(desc(Repository.updated_at)) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(repos)


@bp.route('/users/<username>/repos/<repo_name>')
@login_optional
def get_repo(username, repo_name):
    _, repo = retrieve_user_repo(username, repo_name)
    return jsonify(repo)


@bp.route('/users/<username>/repos/<repo_name>/cards')
@login_optional
@with_pagination
def repo_cards(username, repo_name):
    _, repo = retrieve_user_repo(username, repo_name)
    total = Card.query.filter_by(repository_id=repo.id).count()
    cards = Card.query.filter_by(repository_id=repo.id) \
        .order_by(desc(Card.updated_at)) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(dict(
        total=total,
        data=cards,
    ))


@bp.route('/repos')
@login_required
@with_pagination
def get_own_repos():
    repos = Repository.query.filter_by(user_id=g.user.id) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(repos)


common_repo_schema = {
    Required('desc'): Any(str, None),
    Required('private'): Coerce(bool),
    Required('sides'): Range(min=2, max=6),
    Required('side_a_name'): Any(str, None),
    Required('side_b_name'): Any(str, None),
    Required('side_c_name'): Any(str, None),
    Required('side_d_name'): Any(str, None),
    Required('side_e_name'): Any(str, None),
    Required('side_f_name'): Any(str, None),
}


@bp.route('/repos', methods=['POST'])
@login_required
def create_repo():
    schema = {
        Required('name'): All(
            Match(r'^[a-zA-Z0-9_.-]+$',
                  msg='repository name has invalid symbol'),
            Length(min=1, max=30, msg='repository name too long')
        ),
        **common_repo_schema,
    }
    payload = retrieve_payload(schema)
    src = Repository.query \
        .filter_by(user_id=g.user.id, name=payload['name']) \
        .first()
    if src:
        raise ConflictException(description='repo already exist')
    repo = Repository(user_id=g.user.id, **payload)
    with db.auto_commit():
        db.session.add(repo)
    return jsonify(repo)


# todo: private repo can be accessed
@bp.route('/repos/<id_>')
def get_repo_by_id(id_):
    src = Repository.query.get(id_)
    if not src:
        raise NotFoundError(description='Repo not found')
    return jsonify(src)


@bp.route('/repos/<id_>', methods=['PUT'])
@login_required
def update_repo(id_):
    payload = retrieve_payload(common_repo_schema)
    src = Repository.query.filter_by(id=id_, user_id=g.user.id) \
        .first()
    if not src:
        raise NotFoundError(description='Repo not found')
    with db.auto_commit():
        for key, value in payload.items():
            setattr(src, key, value)
    return jsonify(src)


# MARK: cards
@bp.route('/cards', methods=['POST'])
@login_required
def create_repo_card():
    schema = {
        Required('repository_id'): int,
        Required('side_a'): Any(str, None),
        Required('side_b'): Any(str, None),
        Required('side_c'): Any(str, None),
        Required('side_d'): Any(str, None),
        Required('side_e'): Any(str, None),
        Required('side_f'): Any(str, None),
    }
    payload = retrieve_payload(schema)
    repo = Repository.query.get(payload['repository_id'])
    if not repo:
        raise NotFoundError
    if repo.user_id != g.user.id:
        raise SignatureError
    card = Card(**payload)
    with db.auto_commit():
        db.session.add(card)
    courses = Course.query \
        .filter_by(repository_id=payload['repository_id']) \
        .all()
    with db.auto_commit():
        for course in courses:
            progress = CourseCardProgress(course_id=course.id, card_id=card.id)
            db.session.add(progress)
    return jsonify(card)


@bp.route('/cards/<card_id>', methods=['DELETE'])
@login_required
def delete_repo_card(card_id):
    card = Card.query.get(card_id)
    if not card:
        raise NotFoundError
    if card.repository.user_id != g.user.id:
        raise SignatureError(description='Permission denied')
    with db.auto_commit():
        CourseCardProgress.query.filter_by(card_id=card.id).delete()
        db.session.delete(card)
    return jsonify({})


# MARK: courses

@bp.route('/courses')
@login_required
@with_pagination
def get_courses():
    rv = Course.query.filter_by(user_id=g.user.id) \
        .order_by(desc(Course.updated_at)) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(rv)


@bp.route('/courses/<id_>')
@login_required
def get_course(id_):
    rv = Course.query.filter_by(user_id=g.user.id).filter_by(id=id_).first()
    if not rv:
        raise NotFoundError
    return jsonify(rv)


@bp.route('/courses', methods=['POST'])
@login_required
def create_course():
    schema = {
        Required('repository_id'): int,
        Required('name'): str,
        Required('daily_new'): int,
        Required('daily_review'): int,
        Required('q_sides'): str,
        Required('a_sides'): str,
    }
    payload = retrieve_payload(schema)
    repo = Repository.query.get(payload['repository_id'])
    if not repo:
        raise NotFoundError
    if repo.private and g.user.id != repo.user_id:
        raise NotFoundError
    q_sides = payload['q_sides']
    a_sides = payload['a_sides']
    if not q_sides or not a_sides:
        raise BadRequestError(description='Q&A should both has values')
    # todo: q_sides, a_sides more validation
    course = Course(**payload, user_id=g.user.id)
    # todo: make it transaction
    with db.auto_commit():
        db.session.add(course)
    cards = Card.query.filter_by(repository_id=repo.id).all()
    with db.auto_commit():
        for card in cards:
            progress = CourseCardProgress(course_id=course.id, card_id=card.id)
            db.session.add(progress)
    course.refresh_progress()
    return jsonify(course)


@bp.route('/courses/<course_id>', methods=['DELETE'])
@login_required
def update_course(course_id):
    course = retrieve_course(course_id)
    with db.auto_commit():
        CourseCardProgress.query.filter_by(course_id=course_id).delete()
        db.session.delete(course)
    return jsonify({})


@bp.route('/courses/<course_id>/next', methods=['POST'])
@login_required
def course_next_card(course_id):
    course = retrieve_course(course_id)
    payload = request.get_json()
    if payload:
        schema = {
            Required('card_id'): int,
            Required('feel'): Any(*CourseCardProgress.feels),
        }
        payload = retrieve_payload(schema)
        CourseCardProgress.record(
            course.id, payload['card_id'], payload['feel'])
    return jsonify(course.next() or {})
