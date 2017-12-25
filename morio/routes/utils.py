from morio.core.error import JsonException


def verify_payload(payload, schema):
    from voluptuous import Schema
    from voluptuous import REMOVE_EXTRA
    from voluptuous import MultipleInvalid

    if not payload:
        raise JsonException(description='Payload missing')
    schema = Schema(schema, extra=REMOVE_EXTRA)
    try:
        payload = schema(payload)
    except MultipleInvalid as e:
        raise JsonException(description=e.msg)
    return payload


def if_email(email):
    import re
    return re.compile('[^@]+@[^@]+\.[^@]+').match(email)
