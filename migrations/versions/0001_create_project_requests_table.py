"""create project_requests table

Revision ID: 0001
Revises:
Create Date: 2026-10-03

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "project_requests",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("client_name", sa.String(length=100), nullable=False),
        sa.Column("client_email", sa.String(length=255), nullable=False),
        sa.Column("whatsapp", sa.String(length=20), nullable=False),
        sa.Column("project_type", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("deadline", sa.String(length=100), nullable=False),
        sa.Column("budget", sa.String(length=100), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )
    op.create_index("ix_project_requests_status", "project_requests", ["status"])


def downgrade() -> None:
    op.drop_index("ix_project_requests_status", table_name="project_requests")
    op.drop_table("project_requests")
