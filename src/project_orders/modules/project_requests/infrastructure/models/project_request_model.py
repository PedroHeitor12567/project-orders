import uuid
from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from project_orders.core.database import Base


class ProjectRequestModel(Base):
    """Model de persistência. Conhece SQLAlchemy/PostgreSQL de propósito —
    isso é infraestrutura, não domínio.
    """

    __tablename__ = "project_requests"

    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    client_name: Mapped[str] = mapped_column(String(100), nullable=False)
    client_email: Mapped[str] = mapped_column(String(255), nullable=False)
    whatsapp: Mapped[str] = mapped_column(String(20), nullable=False)
    project_type: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    deadline: Mapped[str] = mapped_column(String(100), nullable=False)
    budget: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
