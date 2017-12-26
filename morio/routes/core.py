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

from .utils import verify_payload


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


@bp.route('/users/<username>/repos/<repo_name>')
@login_optional
def get_repo(username, repo_name):
    user = User.query.filter_by(name=username).first()
    if not user:
        raise NotFoundError(description='User not found')
    repo = Repository.query.filter_by(user_id=user.id, name=repo_name).first()
    if not repo:
        raise NotFoundError(description='Repo not found')
    if repo.private and (not g.user or g.user.id != repo.user_id):
        raise NotFoundError(description='Repo not found')
    return jsonify(repo)


@bp.route('/users/<username>/repos/<repo_name>/cards')
@login_required
def repo_cards(username, repo_name):
    user = User.query.filter_by(name=username).first()
    if not user:
        raise NotFoundError(description='User not found')
    repo = Repository.query.filter_by(user_id=user.id, name=repo_name).first()
    if not repo or (repo.private and g.user.id != repo.user_id):
        raise NotFoundError(description='Repo not found')
    return jsonify(repo)


@bp.route('/users/<username>/repos/<repo_name>/cards', methods=['POST'])
@login_required
def create_repo_card(username, repo_name):
    # schema = {
    #     Required('side_a'): str,
    #     Required('side_b'): str,
    # }
    # payload = verify_payload(request.get_json(), schema)
    # card = Card(repo_id=repo_id, **payload)
    # with db.auto_commit():
    #     db.session.add(card)
    # return jsonify(card)
    raise NotImplemented
