import click
from flask.cli import FlaskGroup


def _create_flask_app(_):
    from morio import create_app
    return create_app()


@click.group(cls=FlaskGroup, create_app=_create_flask_app)
def cli():
    pass


@cli.command(help='Initialize database')
def initdb():
    from morio.model import db
    db.create_all()


@cli.command(help='Hello World')
def hello():
    print('Hello world')


if __name__ == '__main__':
    cli()
