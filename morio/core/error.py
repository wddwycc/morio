import json
from werkzeug.exceptions import HTTPException


class JsonException(HTTPException):
    code = 400
    error = 'invalid_request'

    def __init__(self, code=None, error=None, description=None, response=None):
        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        super(JsonException, self).__init__(description, response)

    def get_body(self, environ=None):
        return json.dumps(dict(
            error=self.error,
            msg=self.description,
        ))

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class BadRequestError(JsonException):
    code = 400
    error = 'invalid_payload'
    description = 'Invalid Payload'


class SignatureMissingError(JsonException):
    code = 401
    error = 'missing_signature'
    description = 'Signature required'


class SignatureError(JsonException):
    code = 403
    error = 'invalid_signature'
    description = 'Signature is invalid'


class NotFoundError(JsonException):
    code = 404
    error = 'not_found'
    description = 'Not found'


class ConflictException(JsonException):
    code = 409
    error = 'conflicted'
    description = 'Conflicted'
