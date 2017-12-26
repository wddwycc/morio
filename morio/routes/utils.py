from flask import g
from morio.model import User, Repository
from morio.core.error import NotFoundError
from morio.core.error import JsonException


def verify_payload(payload, schema):
    from voluptuous import Schema
    from voluptuous import REMOVE_EXTRA
    from voluptuous import MultipleInvalid

    if not payload:
        raise JsonException(description='Payload missing')
    schema = Schema(schema, extra=REMOVE_EXTRA)
    try:
        payload = schema(payload)
    except MultipleInvalid as e:
        raise JsonException(description=e.msg)
    return payload


def if_email(email):
    import re
    return re.compile('[^@]+@[^@]+\.[^@]+').match(email)


def retrieve_user_repo(username, repo_name):
    user = User.query.filter_by(name=username).first()
    if not user:
        raise NotFoundError(description='User not found')
    repo = Repository.query.filter_by(user_id=user.id, name=repo_name).first()
    if not repo or (repo.private and g.user.id != repo.user_id):
        raise NotFoundError(description='Repo not found')
    return user, repo
