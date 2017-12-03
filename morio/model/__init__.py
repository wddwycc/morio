from .base import db
from .user import User
from .repository import Repository
from .card import Card


def init_app(app):
    db.init_app(app)
