"""init

Revision ID: b3cc7f1dbf31
Revises:
Create Date: 2017-10-10 22:45:23.676325

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b3cc7f1dbf31'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role', sa.SmallInteger(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=False),
        sa.Column('email', sa.String(length=200), nullable=False),
        sa.Column('nickname', sa.String(length=30), nullable=False),
        sa.Column('password', sa.String(length=100), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_index(op.f('ix_user_nickname'), 'user', ['nickname'],
                    unique=False)


def downgrade():
    op.drop_index(op.f('ix_user_nickname'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_table('user')
