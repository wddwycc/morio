"""6 sides card

Revision ID: 0caf4a2d5ad5
Revises: 5294a925f463
Create Date: 2018-01-28 14:58:11.059155

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0caf4a2d5ad5'
down_revision = '5294a925f463'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('card', sa.Column('side_c', sa.Text(), nullable=True))
    op.add_column('card', sa.Column('side_d', sa.Text(), nullable=True))
    op.add_column('card', sa.Column('side_e', sa.Text(), nullable=True))
    op.add_column('card', sa.Column('side_f', sa.Text(), nullable=True))
    op.add_column('repository', sa.Column('side_c_name', sa.String(length=30),
                                          nullable=True))
    op.add_column('repository', sa.Column('side_d_name', sa.String(length=30),
                                          nullable=True))
    op.add_column('repository', sa.Column('side_e_name', sa.String(length=30),
                                          nullable=True))
    op.add_column('repository', sa.Column('side_f_name', sa.String(length=30),
                                          nullable=True))


def downgrade():
    op.drop_column('repository', 'side_f_name')
    op.drop_column('repository', 'side_e_name')
    op.drop_column('repository', 'side_d_name')
    op.drop_column('repository', 'side_c_name')
    op.drop_column('card', 'side_f')
    op.drop_column('card', 'side_e')
    op.drop_column('card', 'side_d')
    op.drop_column('card', 'side_c')
