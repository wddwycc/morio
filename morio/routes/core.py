from sqlalchemy import desc

from flask import Blueprint
from flask import g
from flask import jsonify, request

from voluptuous import Required
from voluptuous import Coerce, Any

from morio.core.error import NotFoundError, ConflictException
from morio.core.auth import login_required, login_optional
from morio.core.pagination import with_pagination
from morio.model import db
from morio.model import Repository, Card, User

from .utils import verify_payload, retrieve_user_repo


bp = Blueprint('core', __name__)


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
    cards = Card.query.filter_by(repository_id=repo.id) \
        .order_by(desc(Card.updated_at)) \
        .limit(g.limit).offset(g.offset).all()
    return jsonify(cards)


@bp.route('/repos', methods=['POST'])
@login_required
def create_repo():
    schema = {
        Required('name'): str,
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
@login_optional
def create_repo_card():
    schema = {
        Required('repository_id'): int,
        Required('side_a'): str,
        Required('side_b'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    card = Card(**payload)
    with db.auto_commit():
        db.session.add(card)
    return jsonify(card)
