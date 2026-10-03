from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime

from project_orders.modules.project_requests.domain.enums.project_request_status import (
    ProjectRequestStatus,
)
from project_orders.modules.project_requests.domain.enums.project_type import ProjectType


@dataclass
class ProjectRequest:
    """Entidade de domínio.

    Não conhece FastAPI, Pydantic, SQLAlchemy nem HTTP — apenas as
    regras de negócio da solicitação de projeto.
    """

    id: uuid.UUID
    client_name: str
    client_email: str
    whatsapp: str
    project_type: ProjectType
    description: str
    deadline: str
    budget: str
    status: ProjectRequestStatus
    created_at: datetime

    @classmethod
    def create(
        cls,
        *,
        client_name: str,
        client_email: str,
        whatsapp: str,
        project_type: ProjectType,
        description: str,
        deadline: str,
        budget: str,
    ) -> ProjectRequest:
        """Cria uma nova solicitação.

        Toda solicitação nasce com status PENDING — o cliente nunca
        define o status diretamente (ver seção 8 da especificação).
        """
        return cls(
            id=uuid.uuid4(),
            client_name=client_name,
            client_email=client_email,
            whatsapp=whatsapp,
            project_type=project_type,
            description=description,
            deadline=deadline,
            budget=budget,
            status=ProjectRequestStatus.PENDING,
            created_at=datetime.now(UTC),
        )
