"""user avatar

Revision ID: b35766a66ec8
Revises: 80eee7e421f3
Create Date: 2017-12-28 14:28:26.958223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b35766a66ec8'
down_revision = '80eee7e421f3'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar')
    # ### end Alembic commands ###