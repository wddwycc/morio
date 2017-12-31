"""courses

Revision ID: 03a874a6caaf
Revises: 60430e58fb41
Create Date: 2017-12-31 13:28:40.760330

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '03a874a6caaf'
down_revision = '60430e58fb41'
branch_labels = ()
depends_on = None


def upgrade():
    op.create_table(
        'course',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('repository_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('course')
