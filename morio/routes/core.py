from flask import Blueprint

from morio.core.error import NotFoundError
from morio.model import User


bp = Blueprint('core', __name__)


@bp.route('/api/repositories')
def someone(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        raise NotFoundError()
    return


@bp.route('/<username>/<repo>')
def prototype(username, repo):
    raise NotImplemented
