from . import front
from . import api


def init_app(app):
    app.register_blueprint(front.bp, url_prefix='')
    app.register_blueprint(api.bp, url_prefix='/api')

