from enum import Enum
from flask import jsonify


class APIError(Enum):
    USERNAME_USED = 'Username already used'
    EMAIL_USED = 'Email already used'

    USER_NOT_FOUND = 'User not exist'
    WRONG_PASSWORD = 'Wrong password'
    NO_AUTH = 'Authorization required'
    AUTH_FAILED = 'Authorization failed'
    AUTH_EXPIRED = 'Authorization expired'

    BAD_REQUEST = 'Bad Request'

    @property
    def json(self):
        return jsonify({'error': self.value})

    @staticmethod
    def customize(msg):
        return jsonify({'error': msg})
