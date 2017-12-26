"""fix

Revision ID: 80eee7e421f3
Revises: 2a24a12e0afe
Create Date: 2017-12-26 18:48:58.349437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80eee7e421f3'
down_revision = '2a24a12e0afe'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('side_b', sa.Text(), nullable=True))
    op.drop_column('card', 'site_b')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('site_b', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('card', 'side_b')
    # ### end Alembic commands ###
