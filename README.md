# morio

web service for memory ( under development )

## tech stack

### front-end

* webpack
* vue.js
* element ui

### back-end

* flask
* postgresql

### others

* [tifa](https://github.com/wddwycc/tifa)
* [pipenv](https://github.com/kennethreitz/pipenv)

## setup

```
$ npm install
$ pipenv install
$ python manage.py db upgrade
```

Create `local_settings.py`, fill it with

```python
DEBUG = True
SQLALCHEMY_DATABASE_URI = ''
```

## run dev server

```
$ docker-compose up
$ npm run dev
$ python manage.py run
```
