from enum import Enum
from flask import jsonify


class APIError(Enum):
    USER_NOT_FOUND = 'User doesn\'t exist'
    WRONG_PASSWORD = 'Wrong password'
    NO_AUTH = 'Authorization required'
    AUTH_FAILED = 'Authorization failed'
    AUTH_EXPIRED = 'Authorization expired'

    @property
    def json(self):
        return jsonify({'error': self.value})

    @staticmethod
    def customize(msg):
        return jsonify({'error': msg})
