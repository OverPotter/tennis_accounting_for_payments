"""Create tables

Revision ID: 5d1022a0b833
Revises: 
Create Date: 2024-08-08 20:49:50.305608

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5d1022a0b833"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "clients",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "number_of_tennis_training_available",
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("number_of_training", sa.Integer(), nullable=False),
        sa.Column(
            "training_type",
            sa.Enum(
                "INDIVIDUAL_TRAINING",
                "SPLIT_TRAINING",
                "GROUP_TRAINING",
                name="trainingtypeenum",
            ),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
        ),
        sa.PrimaryKeyConstraint("client_id"),
    )
    op.create_table(
        "payments",
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("payment_date", sa.DateTime(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "visits",
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("visit_datetime", sa.DateTime(), nullable=False),
        sa.Column(
            "training_type",
            sa.Enum(
                "INDIVIDUAL_TRAINING",
                "SPLIT_TRAINING",
                "GROUP_TRAINING",
                name="trainingtypeenum",
            ),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("visits")
    op.drop_table("payments")
    op.drop_table("number_of_tennis_training_available")
    op.drop_table("clients")
    # ### end Alembic commands ###