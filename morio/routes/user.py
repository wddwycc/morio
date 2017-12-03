from flask import Blueprint
from flask import request, Response
from voluptuous import Required

from morio.routes.utils import verify_payload, verify_email
from morio.core.error import APIError
from morio.model import db
from morio.model import User

bp = Blueprint('user', __name__)


@bp.route('/', methods=['POST'])
def register():
    # TODO: name as lower alphabet & number
    schema = {
        Required('name'): str,
        Required('nickname'): str,
        Required('email'): str,
        Required('password'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    if not payload:
        return APIError.BAD_REQUEST.json, 400
    user = User.query.filter_by(name=payload['name']).first()
    if user:
        return APIError.USERNAME_USED, 409
    user = User.query.filter_by(name=payload['email']).first()
    if user:
        return APIError.EMAIL_USED, 409
    user = User(
        role=User.ROLE_USER,
        name=payload['name'],
        nickname=payload['nickname'],
        email=payload['email'],
    )
    user.password = payload['password']
    with db.auto_commit():
        db.session.add(user)
    return user.to_dict()


@bp.route('/login', methods=['POST'])
def login():
    schema = {
        Required('user'): str,
        Required('password'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    if not payload:
        return APIError.BAD_REQUEST.json, 400
    if verify_email(payload['user']):
        user = User.query.filter_by(email=payload['user']).first()
    else:
        user = User.query.filter_by(name=payload['user']).first()
    if not user:
        return APIError.USER_NOT_FOUND.json, 404
    if not user.verify_password(payload['password']):
        return APIError.AUTH_FAILED.json, 403
    response = Response(user.to_dict())
    response.headers['Authorization'] = user.gen_auth_token()
    return response