"""...

Revision ID: 89d0fb9b4b18
Revises: 8b2faf2dd9a5
Create Date: 2025-10-17 17:20:43.821219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89d0fb9b4b18'
down_revision: Union[str, Sequence[str], None] = '8b2faf2dd9a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
