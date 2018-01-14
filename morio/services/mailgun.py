import requests
from flask import current_app
from morio.task import celery


@celery.task()
def send_mail(to, subject, text=None, html=None):
    config = current_app.config
    domain = config.get('MAILGUN_DOMAIN')
    key = config.get('MAILGUN_API_KEY')
    mailgun_address = config.get('MAILGUN_ADDRESS')

    return requests.post(
        '{}/messages'.format(domain),
        auth=('api', key),
        data={
            'from': mailgun_address,
            'to': to,
            'subject': subject,
            'text': text,
            'html': html,
        }
    )
