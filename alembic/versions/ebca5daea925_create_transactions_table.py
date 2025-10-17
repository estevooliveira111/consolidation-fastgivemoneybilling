"""create transactions table

Revision ID: ebca5daea925
Revises: e47755f37f39
Create Date: 2025-10-17 17:15:27.388395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebca5daea925'
down_revision: Union[str, Sequence[str], None] = 'e47755f37f39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
