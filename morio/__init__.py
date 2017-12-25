import os

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from . import model
from . import routes


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return _JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app():
    app = Flask(__name__)

    dev_config = os.path.join(app.root_path, '../conf/base_settings.py')
    app.config.from_pyfile(dev_config)

    local_settings = os.path.join(app.root_path, '../local_settings.py')
    app.config.from_pyfile(local_settings)

    routes.init_app(app)
    model.init_app(app)

    return app
