from datetime import datetime, timedelta

import jwt
from flask import current_app
from sqlalchemy import Column, DateTime
from sqlalchemy import Integer, SmallInteger, String
from werkzeug.security import generate_password_hash, check_password_hash

from .base import db


class User(db.Model):
    __tablename__ = 'user'

    ROLE_USER = 0
    ROLE_ADMIN = 1

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(SmallInteger, nullable=False)
    name = Column(String(30), nullable=False, index=True, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    nickname = Column(String(30), nullable=False, index=True)

    _password = Column('password', String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    # MARK: Password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # MARK: Auth token
    def gen_auth_token(self):
        secret_key = current_app.config.get('SECRET_KEY')
        payload = {
            'exp': datetime.utcnow() + timedelta(days=10),
            'sub': self.id
        }
        return jwt.encode(payload, key=secret_key, algorithm='HS256') \
            .decode('utf-8')

    @staticmethod
    def check_auth_token(auth_token):
        secret_key = current_app.config.get('SECRET_KEY')
        try:
            payload = jwt.decode(
                auth_token, key=secret_key, algorithms='HS256')
            exp = payload['exp']
            if datetime.utcfromtimestamp(exp) < datetime.now():
                raise jwt.ExpiredSignatureError
            return payload['sub']
        except Exception as e:
            raise e
