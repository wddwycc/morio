import os
from uuid import uuid4

import pagan
from flask import Blueprint, render_template
from flask import current_app
from flask import request, jsonify, g
from voluptuous import Email, Match, Length
from voluptuous import Required, Optional, All, Url

from morio.core.auth import login_required
from morio.core.error import ConflictException, SignatureError, NotFoundError
from morio.model import User
from morio.model import db
from morio.routes.utils import verify_payload, if_email
from morio.services import mailgun

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

    avatar = pagan.Avatar(payload['name'], pagan.SHA512)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    filepath = os.path.join('avatar', uuid4().hex[:8])
    avatar.save(os.path.join(upload_folder, filepath), '_.png')
    avatar_path = '/' + os.path.join('upload', filepath, '_.png')
    user = User(
        role=User.ROLE_USER,
        name=payload['name'],
        nickname=payload['nickname'],
        email=payload['email'],
        avatar=avatar_path,
    )
    user.password = payload['password']
    with db.auto_commit():
        db.session.add(user)
    confirm_url = 'https://morio.cc/confirm?token={}'.format(
        user.gen_email_token())
    mailgun.send_mail(
        user.email,
        'Welcome to Morio',
        html=render_template('email/confirm.html', url=confirm_url),
    )
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


@bp.route('/confirm', methods=['POST'])
def confirm_email():
    schema = {
        Required('token'): str,
    }
    payload = verify_payload(request.get_json(), schema)
    user = User.verify_email_token(payload['token'])
    if not user:
        raise NotFoundError(description='Token invalid')
    with db.auto_commit():
        user.email_confirmed = True
        db.session.add(user)
    return jsonify(user)


@bp.route('/me')
@login_required
def me():
    return jsonify(g.user)


@bp.route('/me', methods=['PUT'])
@login_required
def update_me():
    schema = {
        Optional('nickname'): All(
            str, Length(min=1, max=30, msg='nickname too long'),
        ),
        Optional('avatar'): All(Url, msg='invalid avatar url')
    }
    payload = verify_payload(request.get_json(), schema)
    user = g.user
    for key, value in payload.items():
        setattr(user, key, value)
    with db.auto_commit():
        db.session.add(user)
    return jsonify(user)
