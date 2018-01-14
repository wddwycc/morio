from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from morio.model import db


class Card(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    repository_id = Column(
        Integer, ForeignKey('repository.id'), nullable=False)
    side_a = Column(Text)
    side_b = Column(Text)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now,
        nullable=False
    )

    progresses = relationship('CourseCardProgress',
                              backref='card', lazy='dynamic')

    def to_dict(self):
        return dict(
            id=self.id,
            side_a=self.side_a,
            side_b=self.side_b,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
