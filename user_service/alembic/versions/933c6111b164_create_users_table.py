"""create users table

Revision ID: 933c6111b164
Revises: 
Create Date: 2025-11-07 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = '933c6111b164'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True, index=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('users')
