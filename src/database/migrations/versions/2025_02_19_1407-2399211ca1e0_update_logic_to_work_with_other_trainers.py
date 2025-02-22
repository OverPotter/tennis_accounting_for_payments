"""update logic to work with other trainers

Revision ID: 2399211ca1e0
Revises: 2ceb0fbc9761
Create Date: 2025-02-19 14:07:04.096707

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2399211ca1e0"
down_revision: Union[str, None] = "2ceb0fbc9761"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "number_of_tennis_training_available",
        sa.Column("coach_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        None,
        "number_of_tennis_training_available",
        "coaches",
        ["coach_id"],
        ["id"],
    )

    op.add_column(
        "payments", sa.Column("coach_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(None, "payments", "coaches", ["coach_id"], ["id"])

    op.drop_constraint(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        type_="primary",
    )

    op.create_primary_key(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        ["client_id", "coach_id", "training_type"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        type_="primary",
    )

    op.create_primary_key(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        ["client_id", "training_type"],
    )

    op.drop_constraint(
        None, "number_of_tennis_training_available", type_="foreignkey"
    )
    op.drop_column("number_of_tennis_training_available", "coach_id")

    op.drop_constraint(None, "payments", type_="foreignkey")
    op.drop_column("payments", "coach_id")
