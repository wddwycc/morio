from .base import db
from .user import User
from .repository import Repository
from .card import Card
from .course import Course


def init_app(app):
    db.init_app(app)
