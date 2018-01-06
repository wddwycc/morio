"""email confirmed

Revision ID: 03b528abe5bf
Revises: 47938a494184
Create Date: 2018-01-06 22:34:44.492930

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '03b528abe5bf'
down_revision = '47938a494184'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column(
        'user', sa.Column(
            'email_confirmed', sa.Boolean(),
            nullable=False, server_default='0')
    )


def downgrade():
    op.drop_column('user', 'email_confirmed')
