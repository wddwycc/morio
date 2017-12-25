from flask import Blueprint
from flask import g
from flask import jsonify, request

from voluptuous import Required
from voluptuous import Coerce, Any

from morio.core.error import SignatureError, ConflictException
from morio.core.auth import login_required
from morio.core.pagination import with_pagination
from morio.model import db
from morio.model import Repository

from .utils import verify_payload


bp = Blueprint('core', __name__)


@bp.route('/repos')
@login_required
@with_pagination
def get_repos():
    if not g.user:
        raise SignatureError()
    repos = Repository.query.filter_by(user_id=g.user.id) \
        .offest(g.limit).limit(g.offset).all()
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
def repo_cards(repo_id):
    raise NotImplemented


@bp.route('/repos/<repo_id>/cards', methods=['POST'])
def create_repo_card(repo_id):
    raise NotImplemented
