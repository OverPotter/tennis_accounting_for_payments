"""Upgrade pk key to constraint pk key

Revision ID: 443b7ec842a6
Revises: 265a69a27b42
Create Date: 2025-01-21 12:55:26.801424

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "443b7ec842a6"
down_revision: Union[str, None] = "265a69a27b42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE trainingtypesenum AS ENUM ('INDIVIDUAL_TRAINING', 'SPLIT_TRAINING', 'GROUP_TRAINING')"
    )

    op.execute(
        """
        ALTER TABLE number_of_tennis_training_available
        ALTER COLUMN training_type
        TYPE trainingtypesenum
        USING training_type::text::trainingtypesenum
        """
    )
    op.execute(
        """
        ALTER TABLE visits
        ALTER COLUMN training_type
        TYPE trainingtypesenum
        USING training_type::text::trainingtypesenum
        """
    )

    op.execute("DROP TYPE trainingtypeenum")


def downgrade() -> None:
    op.execute(
        "CREATE TYPE trainingtypeenum AS ENUM ('INDIVIDUAL_TRAINING', 'SPLIT_TRAINING', 'GROUP_TRAINING')"
    )

    op.execute(
        """
        ALTER TABLE number_of_tennis_training_available
        ALTER COLUMN training_type
        TYPE trainingtypeenum
        USING training_type::text::trainingtypeenum
        """
    )
    op.execute(
        """
        ALTER TABLE visits
        ALTER COLUMN training_type
        TYPE trainingtypeenum
        USING training_type::text::trainingtypeenum
        """
    )

    op.execute("DROP TYPE trainingtypesenum")
