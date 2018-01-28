"""repo sides num

Revision ID: 342bd4c70bce
Revises: 0caf4a2d5ad5
Create Date: 2018-01-28 21:49:18.466841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '342bd4c70bce'
down_revision = '0caf4a2d5ad5'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('repository', sa.Column('sides', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('repository', 'sides')
