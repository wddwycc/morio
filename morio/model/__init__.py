from .base import db
from .user import User
from .repository import Repository
from .card import Card
from .course import Course
from .course_card_progress import CourseCardProgress


def init_app(app):
    db.init_app(app)
