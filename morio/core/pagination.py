from functools import wraps
from flask import request, g


def with_pagination(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.limit = request.args.get('limit', type=int) or 30
        g.offset = request.args.get('offset', type=int) or 0
        return f(*args, **kwargs)
    return decorated_function
