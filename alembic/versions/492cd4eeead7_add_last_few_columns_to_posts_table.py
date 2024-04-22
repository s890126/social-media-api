"""add last few columns to posts table

Revision ID: 492cd4eeead7
Revises: 5ae3009af179
Create Date: 2024-04-19 21:00:31.836622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '492cd4eeead7'
down_revision: Union[str, None] = '5ae3009af179'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable = False, server_default = 'TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text
        ('NOW()')),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
