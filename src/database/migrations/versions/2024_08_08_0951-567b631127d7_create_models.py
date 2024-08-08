"""Create models

Revision ID: 567b631127d7
Revises: 
Create Date: 2024-08-08 09:51:14.738143

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "567b631127d7"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tennis_training_type",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "number_of_tennis_training_available",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("tennis_type_id", sa.Integer(), nullable=False),
        sa.Column("number_of_training", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tennis_type_id"],
            ["tennis_training_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "tennis_type_id"),
    )
    op.create_table(
        "payments",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("payment_date", sa.DateTime(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "visits",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("tennis_type_id", sa.Integer(), nullable=False),
        sa.Column("visit_datetime", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["tennis_type_id"],
            ["tennis_training_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("visits")
    op.drop_table("payments")
    op.drop_table("number_of_tennis_training_available")
    op.drop_table("users")
    op.drop_table("tennis_training_type")
    # ### end Alembic commands ###
