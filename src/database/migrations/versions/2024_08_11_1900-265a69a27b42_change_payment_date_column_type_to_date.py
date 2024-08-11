"""Change payment_date column type to DATE

Revision ID: 265a69a27b42
Revises: 5d1022a0b833
Create Date: 2024-08-11 19:00:20.592123

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "265a69a27b42"
down_revision: Union[str, None] = "5d1022a0b833"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "payments", "payment_date", type_=sa.Date(), existing_type=sa.DateTime()
    )


def downgrade() -> None:
    op.alter_column(
        "payments", "payment_date", type_=sa.DateTime(), existing_type=sa.Date()
    )
