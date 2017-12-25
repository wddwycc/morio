"""repo meta

Revision ID: 6123c27d47d6
Revises: 423fffdc2e53
Create Date: 2017-12-25 16:20:41.191893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6123c27d47d6'
down_revision = '423fffdc2e53'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('repository', sa.Column('desc', sa.Text(), nullable=True))
    op.add_column('repository', sa.Column('private', sa.Boolean(), nullable=False))


def downgrade():
    op.drop_column('repository', 'private')
    op.drop_column('repository', 'desc')
