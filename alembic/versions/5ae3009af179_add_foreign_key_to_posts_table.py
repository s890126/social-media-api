"""add foreign-key to posts table

Revision ID: 5ae3009af179
Revises: d2997f4334a0
Create Date: 2024-04-19 20:49:14.061287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ae3009af179'
down_revision: Union[str, None] = 'd2997f4334a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table = 'posts', referent_table = 'users', local_cols = ['owner_id'], remote_cols = ['id'], ondelete= 'CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name = 'posts')
    op.drop_column('posts', 'owner_id')
    pass
