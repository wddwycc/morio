from flask import Blueprint
from flask import request, jsonify
from voluptuous import Required, All
from voluptuous import Email, Match, Length

from morio.core.error import ConflictException, SignatureError
from morio.model import User
from morio.model import db
from morio.routes.utils import verify_payload, if_email

bp = Blueprint('user', __name__)


@bp.route('/register', methods=['POST'])
def register():
    schema = {
        Required('name'): All(
            Match(r'^[a-zA-Z0-9_.-]+$', msg='username has invalid symbol'),
            Length(min=1, max=30, msg='username too long')
        ),
        Required('nickname'): All(
            str, Length(min=1, max=30, msg='nickname too long'),
        ),
        Required('email'): All(Email(), msg='bad email format'),
        Required('password'): All(
            str, Length(min=6, msg='password less then 6 letters'),
        ),
    }
    payload = verify_payload(request.get_json(), schema)
    user = User.query.filter_by(name=payload['name']).first()
    if user:
        raise ConflictException(description='username already used')
    user = User.query.filter_by(email=payload['email']).first()
    if user:
        raise ConflictException(description='email already used')
    user = User(
        role=User.ROLE_USER,
        name=payload['name'],
        nickname=payload['nickname'],
        email=payload['email'],
    )
    # todo: send confirm email
    user.password = payload['password']
    with db.auto_commit():
        db.session.add(user)
    resp = jsonify(user)
    resp.headers['Authorization'] = user.gen_auth_token()
    return resp


@bp.route('/login', methods=['POST'])
def login():
    schema = {
        Required('user'): str,
        Required('password'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    if if_email(payload['user']):
        user = User.query.filter_by(email=payload['user']).first()
    else:
        user = User.query.filter_by(name=payload['user']).first()
    if not user:
        raise SignatureError(description='user not exist')
    if not user.verify_password(payload['password']):
        raise SignatureError(description='wrong password')
    resp = jsonify(user)
    resp.headers['Authorization'] = user.gen_auth_token()
    return resp
