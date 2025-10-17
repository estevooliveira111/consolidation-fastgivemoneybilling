"""create transactions table

Revision ID: 8b2faf2dd9a5
Revises: ebca5daea925
Create Date: 2025-10-17 17:16:10.461707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b2faf2dd9a5'
down_revision: Union[str, Sequence[str], None] = 'ebca5daea925'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
