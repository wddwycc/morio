from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, SmallInteger, DateTime

from morio.model import db


class CourseAction(db.Model):
    EASY = 0
    MEDIUM = 1
    HARD = 2

    types = [EASY, MEDIUM, HARD]

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(SmallInteger, nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    card_id = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            course_id=self.course_id,
            type=self.type,
        )
