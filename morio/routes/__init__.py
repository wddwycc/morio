from . import user


def init_app(app):
    app.register_blueprint(user.bp, url_prefix='/api/user')
