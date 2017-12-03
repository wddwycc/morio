"""repo

Revision ID: 423fffdc2e53
Revises: b3cc7f1dbf31
Create Date: 2017-12-03 13:41:20.408937

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '423fffdc2e53'
down_revision = 'b3cc7f1dbf31'
branch_labels = ()
depends_on = None


def upgrade():
    op.create_table(
        'repository',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'name', name='_user_repo_uc')
    )
    op.create_table(
        'card',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('repository_id', sa.Integer(), nullable=False),
        sa.Column('side_a', sa.Text(), nullable=True),
        sa.Column('site_b', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('card')
    op.drop_table('repository')
