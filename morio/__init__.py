from flask import Flask
from . import routes
from . import model


def create_app():
    app = Flask(__name__)
    routes.init_app(app)
    model.init_app(app)

    import os

    dev_config = os.path.join(app.root_path, '../conf/dev_settings.py')
    app.config.from_pyfile(dev_config)
    return app
