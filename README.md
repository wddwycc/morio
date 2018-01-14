# morio

web service for memory -> [morio.cc](https://morio.cc/)

## Built With

### front-end

* vue.js
* element ui

### back-end

* flask
* celery
* postgresql
* redis
* influxdb

### others

* [tifa](https://github.com/wddwycc/tifa)
* [pipenv](https://github.com/kennethreitz/pipenv)

## setup

```
$ npm install
$ pipenv install
$ docker-compose up
$ python manage.py db upgrade
```

Create `local_settings.py`, fill it with

```python
import os

_here = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'morio.secret'
UPLOAD_FOLDER = os.path.join(_here, 'upload')
SQLALCHEMY_DATABASE_URI = (
    'postgresql://morio:pw@localhost:5432/morio'
)

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

MAILGUN_DOMAIN = ''
MAILGUN_API_KEY = ''
MAILGUN_ADDRESS = ''
```

## run dev server

```
$ docker-compose up
$ npm run dev
$ python manage.py run
$ celery worker -A celery_worker.celery --loglevel=info
```
