"""add create and delete access to admins

Revision ID: 76a093151aa0
Revises: 79271458a973
Create Date: 2024-12-14 17:54:25.823261

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "76a093151aa0"
down_revision = "79271458a973"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "admins",
        sa.Column(
            "create_users_access",
            sa.Boolean(),
            server_default=sa.text("1"),
            nullable=False,
        ),
    )
    op.add_column(
        "admins",
        sa.Column(
            "remove_users_access",
            sa.Boolean(),
            server_default=sa.text("1"),
            nullable=False,
        ),
    )
    op.add_column(
        "admins",
        sa.Column(
            "is_owner",
            sa.Boolean(),
            server_default=sa.text("0"),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("admins", "remove_users_access")
    op.drop_column("admins", "create_users_access")
    op.drop_column("admins", "is_owner")
    # ### end Alembic commands ###
