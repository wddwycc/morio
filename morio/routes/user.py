from flask import Blueprint
from flask import request, Response
from voluptuous import Required

from morio.core.error import APIError
from morio.model import User
from morio.model import db
from morio.routes.utils import verify_payload, verify_email

bp = Blueprint('user', __name__)


@bp.route('/register', methods=['POST'])
def register():
    # TODO: name as lower alphabet & number, not equal to core routes.
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
        return APIError.USERNAME_USED.json, 409
    user = User.query.filter_by(email=payload['email']).first()
    if user:
        return APIError.EMAIL_USED.json, 409
    user = User(
        role=User.ROLE_USER,
        name=payload['name'],
        nickname=payload['nickname'],
        email=payload['email'],
    )
    user.password = payload['password']
    with db.auto_commit():
        db.session.add(user)
    response = Response()
    response.headers['Authorization'] = user.gen_auth_token()
    return response


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
    response = Response()
    response.headers['Authorization'] = user.gen_auth_token()
    return response
