"""changed table clients, column account number from BigInteger to string

Revision ID: c56aefd0a46a
Revises: 3380503dbde5
Create Date: 2024-06-19 20:48:15.171383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c56aefd0a46a'
down_revision: Union[str, None] = '3380503dbde5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
