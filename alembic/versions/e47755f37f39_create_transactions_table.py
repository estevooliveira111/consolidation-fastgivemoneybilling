"""create transactions table

Revision ID: e47755f37f39
Revises: b44607be809b
Create Date: 2025-10-17 17:14:48.289706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e47755f37f39'
down_revision: Union[str, Sequence[str], None] = 'b44607be809b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
