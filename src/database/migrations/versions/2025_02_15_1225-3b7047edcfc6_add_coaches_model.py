"""Add coaches model

Revision ID: 3b7047edcfc6
Revises: 2e85d81ca590
Create Date: 2025-02-15 12:25:00.703475

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3b7047edcfc6"
down_revision: Union[str, None] = "2e85d81ca590"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "coaches",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column(
            "specialization",
            sa.Enum(
                "FITNESS_TRAINER", "TENNIS_TRAINER", name="specializationenum"
            ),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("visits", sa.Column("coach_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "visits", "coaches", ["coach_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("visits_coach_id_fkey", "visits", type_="foreignkey")
    op.drop_column("visits", "coach_id")
    op.drop_table("coaches")
    # ### end Alembic commands ###
