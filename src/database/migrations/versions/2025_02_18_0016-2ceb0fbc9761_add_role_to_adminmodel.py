"""add role to AdminModel

Revision ID: 2ceb0fbc9761
Revises: 3b7047edcfc6
Create Date: 2025-02-18 00:16:17.206821

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2ceb0fbc9761"
down_revision: Union[str, None] = "3b7047edcfc6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


admin_role_enum = sa.Enum("ADMIN", "TRAINER", name="adminroleenum")


def upgrade() -> None:
    admin_role_enum.create(op.get_bind())

    op.add_column("admins", sa.Column("role", admin_role_enum, nullable=False))


def downgrade() -> None:
    op.drop_column("admins", "role")

    admin_role_enum.drop(op.get_bind())
