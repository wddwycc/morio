from .base import db
from sqlalchemy import Column
from sqlalchemy import Integer


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
