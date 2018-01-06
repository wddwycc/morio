from datetime import datetime, timedelta

import jwt
from flask import current_app
from sqlalchemy import Column, DateTime
from sqlalchemy import Integer, SmallInteger, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from morio.model import db


class User(db.Model):
    ROLE_USER = 0
    ROLE_ADMIN = 1

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(SmallInteger, nullable=False)
    name = Column(String(30), nullable=False, index=True, unique=True)
    nickname = Column(String(30), nullable=False, index=True)
    email = Column(String(200), nullable=False, unique=True)
    avatar = Column(String(200))
    email_confirmed = Column(Boolean, default=False, nullable=False)

    _password = Column('password', String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    repositories = relationship('Repository', backref='user', lazy='dynamic')
    courses = relationship('Course', backref='user', lazy='dynamic')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            nickname=self.nickname,
            avatar=self.avatar,
            email=self.email,
        )

    # MARK: Password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def verify_password(self, raw):
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
        token = jwt.encode(payload, key=secret_key, algorithm='HS256') \
            .decode('utf-8')
        return 'Bearer ' + token

    @staticmethod
    def verify_auth_token(auth_token):
        if not auth_token.startswith('Bearer '):
            raise jwt.InvalidTokenError
        auth_token = auth_token[7:]
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

    # MARK: Mail Verification
    def gen_email_token(self):
        secret_key = current_app.config.get('SECRET_KEY')
        payload = {
            'exp': datetime.utcnow() + timedelta(days=7),
            'sub': self.email,
        }
        token = jwt.encode(payload, key=secret_key, algorithm='HS256') \
            .decode('utf-8')
        return token

    @staticmethod
    def verify_email_token(email_token):
        secret_key = current_app.config.get('SECRET_KEY')
        try:
            payload = jwt.decode(
                email_token, key=secret_key, algorithms='HS256')
            exp = payload['exp']
            if datetime.utcfromtimestamp(exp) < datetime.now():
                return False
            user = User.query.filter_by(email=payload['sub']).first()
            return user
        except Exception as e:
            print(e)
            return False
