from .base import db
from sqlalchemy import Column
from sqlalchemy import Integer


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
