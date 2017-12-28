from flask import current_app
from flask import send_from_directory
from . import user
from . import core


def init_app(app):
    app.register_blueprint(core.bp, url_prefix='/api')
    app.register_blueprint(user.bp, url_prefix='/api/user')

    @app.route('/upload/<path:file>')
    def serve_uploads(file):
        upload_folder = current_app.config['UPLOAD_FOLDER']
        return send_from_directory(upload_folder, file)
