# morio

web service for memory ( under development )

## tech stack

### front-end

* webpack
* vue.js
* element.io

### back-end

* flask
* mysql

### others

* [tifa](https://github.com/wddwycc/tifa)

## setup

```
$ npm install
```

```
$ virtualenv venv -p <python_version>
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## run webpack dev server

```
npm run dev
```

## run flask server

Add your flask settings in `conf/dev_settings.py`. Then run

```
python manage.py run
```
