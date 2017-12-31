from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, DateTime

from morio.model import db


class Course(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    repository_id = Column(
        Integer, ForeignKey('repository.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            repository=self.repository,
        )
