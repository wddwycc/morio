import click
from flask.cli import FlaskGroup
from flask_alembic import Alembic

from morio import create_app


def _create_flask_app(_):
    app = create_app()
    Alembic(app)
    return app


@click.group(cls=FlaskGroup, create_app=_create_flask_app)
def cli():
    pass


@cli.command(help='Create admin')
def create_admin():
    pass


@cli.command(help='Refresh all course progress')
def refresh_progress():
    from morio.model import Course
    courses = Course.query.all()
    for course in courses:
        course.refresh_progress()


if __name__ == '__main__':
    cli()
