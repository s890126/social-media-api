"""add content column to posts table

Revision ID: ad13b3cf6d94
Revises: 82d6ecb93b00
Create Date: 2024-04-19 16:51:42.030512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad13b3cf6d94'
down_revision: Union[str, None] = '82d6ecb93b00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
