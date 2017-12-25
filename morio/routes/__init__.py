from . import user
from . import core


def init_app(app):
    app.register_blueprint(core.bp, url_prefix='/api')
    app.register_blueprint(user.bp, url_prefix='/api/user')
