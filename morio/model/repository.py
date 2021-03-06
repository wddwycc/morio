from datetime import datetime

from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy import Integer, DateTime, Boolean, Text, String
from sqlalchemy.orm import relationship

from morio.model import db


class Repository(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String, nullable=False, index=True)
    desc = Column(Text)

    private = Column(Boolean, nullable=False)

    # side a-f
    sides = Column(Integer, default=2)
    side_a_name = Column(String(30))
    side_b_name = Column(String(30))
    side_c_name = Column(String(30))
    side_d_name = Column(String(30))
    side_e_name = Column(String(30))
    side_f_name = Column(String(30))

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    cards = relationship('Card', backref='repository', lazy='dynamic')
    courses = relationship('Course', backref='repository', lazy='dynamic')

    __table_args__ = (
        UniqueConstraint('user_id', 'name', name='_user_repo_uc'),
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            desc=self.desc,
            username=self.user.name,
            private=self.private,

            sides=self.sides,
            side_a_name=self.side_a_name,
            side_b_name=self.side_b_name,
            side_c_name=self.side_c_name,
            side_d_name=self.side_d_name,
            side_e_name=self.side_e_name,
            side_f_name=self.side_f_name,

            created_at=self.created_at,
            updated_at=self.updated_at,
        )
