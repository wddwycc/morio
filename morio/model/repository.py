from datetime import datetime

from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy import Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

from morio.model import db


class Repository(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(Integer, nullable=False)

    private = Column(Boolean, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    repositories = relationship('Card', backref='repository', lazy='dynamic')

    __table_args__ = (
        UniqueConstraint('user_id', 'name', name='_user_repo_uc'),
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            user_id=self.user_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
