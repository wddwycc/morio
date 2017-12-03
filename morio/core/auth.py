from functools import wraps
from flask import request, g
from jwt import DecodeError, ExpiredSignatureError, InvalidTokenError
from morio.core.error import APIError
from morio.model import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return APIError.NO_AUTH.json, 401
        try:
            user_id = User.verify_auth_token(token)
        except (DecodeError, InvalidTokenError):
            return APIError.AUTH_FAILED.json, 401
        except ExpiredSignatureError:
            return APIError.AUTH_EXPIRED, 401
        user = User.query.get(user_id)
        if not user:
            return APIError.AUTH_FAILED.json, 401
        g.user = user
        return f(*args, **kwargs)
    return decorated_function
