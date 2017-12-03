def verify_payload(payload, schema):
    from voluptuous import Schema
    from voluptuous import REMOVE_EXTRA
    from voluptuous import MultipleInvalid

    if not payload:
        return None
    schema = Schema(schema, extra=REMOVE_EXTRA)
    try:
        payload = schema(payload)
    except MultipleInvalid:
        return None
    return payload


def verify_email(email):
    import re
    return re.compile('[^@]+@[^@]+\.[^@]+').match(email)
