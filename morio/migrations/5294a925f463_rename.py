"""rename

Revision ID: 5294a925f463
Revises: 417e11090ca9
Create Date: 2018-01-14 21:36:36.804679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5294a925f463'
down_revision = '417e11090ca9'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course_card_progress', sa.Column('last_feel', sa.Integer(), nullable=True))
    op.drop_column('course_card_progress', 'today_last_feel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course_card_progress', sa.Column('today_last_feel', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('course_card_progress', 'last_feel')
    # ### end Alembic commands ###
