# morio

web service for memory ( under development )

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
DEBUG = True
SECRET_KEY = 'morio.secret'
SQLALCHEMY_DATABASE_URI = (
    'postgresql://morio:pw@localhost:5432/morio'
)
```

## run dev server

```
$ docker-compose up
$ python manage.py db upgrade
$ npm run dev
$ python manage.py run
```
