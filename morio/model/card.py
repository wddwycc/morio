from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, DateTime

from morio.model import db


class Card(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    repository_id = Column(
        Integer, ForeignKey('repository.id'), nullable=False)
    side_a = Column(Text)
    site_b = Column(Text)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now,
        nullable=False
    )
