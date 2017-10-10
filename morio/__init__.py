import os

from flask import Flask

from . import model
from . import routes


def create_app():
    app = Flask(__name__)

    dev_config = os.path.join(app.root_path, '../conf/base_settings.py')
    app.config.from_pyfile(dev_config)

    local_settings = os.path.join(app.root_path, '../local_settings.py')
    app.config.from_pyfile(local_settings)

    routes.init_app(app)
    model.init_app(app)

    return app
