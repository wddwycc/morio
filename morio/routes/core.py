from sqlalchemy import desc

from flask import Blueprint
from flask import g
from flask import jsonify, request

from voluptuous import Required, Any, All
from voluptuous import Coerce, Match, Length

from morio.core.error import ConflictException, NotFoundError, SignatureError
from morio.core.auth import login_required, login_optional
from morio.core.pagination import with_pagination
from morio.model import db
from morio.model import Repository, Card, User, Course

from .utils import verify_payload, retrieve_user_repo


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


@bp.route('/users/<username>/repos/<repo_name>', methods=['PUT'])
@login_required
def update_repo(username, repo_name):
    user, repo = retrieve_user_repo(username, repo_name)
    if user.id != g.user.id:
        raise SignatureError
    schema = {
        Required('side_a_name'): Any(str, None),
        Required('side_b_name'): Any(str, None),
        Required('desc'): Any(str, None),
        Required('private'): Coerce(bool),
    }
    payload = verify_payload(request.get_json(), schema)
    for key, value in payload.items():
        setattr(repo, key, value)
    with db.auto_commit():
        db.session.add(repo)
    return jsonify(repo)


@bp.route('/users/<username>/repos/<repo_name>/cards')
@login_optional
@with_pagination
def repo_cards(username, repo_name):
    _, repo = retrieve_user_repo(username, repo_name)
    cards = Card.query.filter_by(repository_id=repo.id) \
        .order_by(desc(Card.updated_at)) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(cards)


@bp.route('/repos', methods=['POST'])
@login_required
def create_repo():
    schema = {
        Required('name'): All(
            Match(r'^[a-zA-Z0-9_.-]+$',
                  msg='repository name has invalid symbol'),
            Length(min=1, max=30, msg='repository name too long')
        ),
        Required('desc'): Any(str, None),
        Required('private'): Coerce(bool),
    }
    payload = verify_payload(request.get_json(), schema)
    src = Repository.query.filter_by(user_id=g.user.id, name=payload['name']) \
        .first()
    if src:
        raise ConflictException(description='repo already exist')
    repo = Repository(user_id=g.user.id, **payload)
    with db.auto_commit():
        db.session.add(repo)
    return jsonify(repo)


@bp.route('/cards', methods=['POST'])
@login_required
def create_repo_card():
    schema = {
        Required('repository_id'): int,
        Required('side_a'): str,
        Required('side_b'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    repo = Repository.query.get(payload['repository_id'])
    if not repo:
        raise NotFoundError
    if repo.user_id != g.user.id:
        raise SignatureError
    card = Card(**payload)
    with db.auto_commit():
        db.session.add(card)
    return jsonify(card)


@bp.route('/courses', methods=['POST'])
@login_required
def create_course():
    schema = {
        Required('repository_id'): int,
    }
    payload = verify_payload(request.get_json(), schema)
    repo = Repository.query.get(payload['repository_id'])
    if not repo or repo.private:
        raise NotFoundError
    course = Course(**payload)
    with db.auto_commit():
        db.session.add(course)
    return jsonify(course)


@bp.route('/courses/<course_id>', methods=['DELETE'])
@login_required
def update_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        raise NotFoundError
    if course.user_id != g.user.id:
        raise SignatureError(description='Not the owner')
    with db.auto_commit():
        db.session.remove(course)
    return jsonify({})
