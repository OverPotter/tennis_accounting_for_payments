"""create constraint key for number model

Revision ID: 90ca26e49656
Revises: 265a69a27b42
Create Date: 2024-08-21 20:12:33.819226

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "90ca26e49656"
down_revision: Union[str, None] = "265a69a27b42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_constraint(
        "number_of_tennis_training_available_ibfk_1",
        "number_of_tennis_training_available",
        type_="foreignkey",
    )

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

    op.create_foreign_key(
        "fk_number_of_tennis_training_available_client_id_clients",
        "number_of_tennis_training_available",
        "clients",
        ["client_id"],
        ["id"],
    )


def downgrade():
    op.drop_constraint(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        type_="primary",
    )

    op.create_foreign_key(
        "number_of_tennis_training_available_ibfk_1",
        "number_of_tennis_training_available",
        "clients",
        ["client_id"],
        ["id"],
    )

    op.create_primary_key(
        "number_of_tennis_training_available_pkey",
        "number_of_tennis_training_available",
        ["client_id"],
    )
