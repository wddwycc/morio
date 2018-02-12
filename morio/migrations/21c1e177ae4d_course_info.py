"""course info

Revision ID: 21c1e177ae4d
Revises: 342bd4c70bce
Create Date: 2018-02-11 12:39:10.982942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c1e177ae4d'
down_revision = '342bd4c70bce'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('course', sa.Column('q_sides', sa.String(), nullable=True,
                                      server_default='a'))
    op.add_column('course', sa.Column('a_sides', sa.String(), nullable=True,
                                      server_default='b'))
    op.add_column('course', sa.Column('daily_new', sa.Integer(),
                                      nullable=False, server_default='30'))
    op.add_column('course', sa.Column('daily_review', sa.Integer(),
                                      nullable=False, server_default='180'))
    op.add_column('course', sa.Column('name', sa.String(), nullable=True))


def downgrade():
    op.drop_column('course', 'q_sides')
    op.drop_column('course', 'name')
    op.drop_column('course', 'daily_review')
    op.drop_column('course', 'daily_new')
    op.drop_column('course', 'a_sides')
