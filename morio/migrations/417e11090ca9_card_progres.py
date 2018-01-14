"""card progres

Revision ID: 417e11090ca9
Revises: 03b528abe5bf
Create Date: 2018-01-14 18:03:34.285672

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '417e11090ca9'
down_revision = '03b528abe5bf'
branch_labels = ()
depends_on = None


def upgrade():
    op.create_table(
        'course_card_progress',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hits', sa.Integer(), nullable=False),
        sa.Column('last_time_grasped', sa.DateTime(), nullable=True),
        sa.Column('today_status', sa.Integer(), nullable=True),
        sa.Column('now_status', sa.Integer(), nullable=True),
        sa.Column('today_last_feel', sa.Integer(), nullable=True),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('card_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('course_id', 'card_id',
                            name='_course_id_card_id_uc')
    )
    op.drop_table('course_action')


def downgrade():
    op.create_table('course_action',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('type', sa.SMALLINT(), autoincrement=False,
                              nullable=False),
                    sa.Column('course_id', sa.INTEGER(), autoincrement=False,
                              nullable=False),
                    sa.Column('card_id', sa.INTEGER(), autoincrement=False,
                              nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['course_id'], ['course.id'],
                                            name='course_action_course_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='course_action_pkey')
                    )
    op.drop_table('course_card_progress')
