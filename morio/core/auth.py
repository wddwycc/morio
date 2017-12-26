from functools import wraps
from flask import request, g
from jwt import DecodeError, ExpiredSignatureError, InvalidTokenError
from morio.core.error import SignatureMissingError, SignatureError
from morio.model import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise SignatureMissingError()
        try:
            user_id = User.verify_auth_token(token)
        except (DecodeError, InvalidTokenError):
            raise SignatureError()
        except ExpiredSignatureError:
            raise SignatureError(description='Signature expired')
        user = User.query.get(user_id)
        if not user:
            return SignatureError()
        g.user = user
        return f(*args, **kwargs)
    return decorated_function


def login_optional(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            g.user = None
            return f(*args, **kwargs)
        try:
            user_id = User.verify_auth_token(token)
        except Exception:
            g.user = None
            return f(*args, **kwargs)
        user = User.query.get(user_id)
        if not user:
            g.user = None
            return f(*args, **kwargs)
        g.user = user
        return f(*args, **kwargs)
    return decorated_function
