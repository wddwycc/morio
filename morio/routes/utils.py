from flask import g, request
from morio.model import User, Repository, Course
from morio.core.error import NotFoundError, SignatureError
from morio.core.error import JsonException


def retrieve_payload(schema):
    from voluptuous import Schema
    from voluptuous import REMOVE_EXTRA
    from voluptuous import MultipleInvalid

    payload = request.get_json()
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
    if not repo or (
        repo.private and (not g.user or g.user.id != repo.user_id)
    ):
        raise NotFoundError(description='Repo not found')
    return user, repo


def retrieve_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        raise NotFoundError
    if course.user_id != g.user.id:
        raise SignatureError(description='Permission denied')
    return course
