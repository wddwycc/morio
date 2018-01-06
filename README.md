# morio

web service for memory -> [morio.cc](https://morio.cc/)

## Built With

### front-end

* vue.js
* element ui

### back-end

* flask
* postgresql
* influxdb

### others

* [tifa](https://github.com/wddwycc/tifa)
* [pipenv](https://github.com/kennethreitz/pipenv)

## setup

```
$ npm install
$ pipenv install
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

MAILGUN_DOMAIN = ''
MAILGUN_API_KEY = ''
MAILGUN_ADDRESS = ''
```

## run dev server

```
$ docker-compose up
$ python manage.py db upgrade
$ npm run dev
$ python manage.py run
```
