"""Add composite primary key to number_of_tennis_training_available

Revision ID: 2e85d81ca590
Revises: 443b7ec842a6
Create Date: 2025-01-21 13:54:51.061862

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2e85d81ca590"
down_revision: Union[str, None] = "443b7ec842a6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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


def downgrade() -> None:
    op.drop_constraint(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        type_="primary",
    )
    op.create_primary_key(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        ["client_id"],
    )
