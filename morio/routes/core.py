from flask import Blueprint
from flask import g
from flask import jsonify, request

from voluptuous import Required
from voluptuous import Coerce, Any

from morio.core.error import NotFoundError, ConflictException
from morio.core.auth import login_required
from morio.core.pagination import with_pagination
from morio.model import db
from morio.model import Repository, Card

from .utils import verify_payload


bp = Blueprint('core', __name__)


@bp.route('/repos')
@login_required
@with_pagination
def get_repos():
    repos = Repository.query.filter_by(user_id=g.user.id) \
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


@bp.route('/repos/<repo_id>/cards')
@login_required
def repo_cards(repo_id):
    repo = Repository.query.get(repo_id)
    if repo.private and g.user.id != repo.uesr_id:
        raise NotFoundError(description='Repo not found')
    return jsonify(repo)


@bp.route('/repos/<repo_id>/cards', methods=['POST'])
@login_required
def create_repo_card(repo_id):
    schema = {
        Required('side_a'): str,
        Required('side_b'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    card = Card(repo_id=repo_id, **payload)
    with db.auto_commit():
        db.session.add(card)
    return jsonify(card)
