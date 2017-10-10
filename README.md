# morio

web service for memory ( under development )

## tech stack

### front-end

* webpack
* vue.js
* element ui

### back-end

* flask
* mysql

### others

* [tifa](https://github.com/wddwycc/tifa)

## setup

```
$ npm install
```

Create `local_settings.py`, fill it with

```python
DEBUG = True
SQLALCHEMY_DATABASE_URI = ''
```

```
$ virtualenv venv -p <python_version>
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py db upgrade
```

## run webpack dev server

```
npm run dev
```

## run flask server

```
python manage.py run
```
