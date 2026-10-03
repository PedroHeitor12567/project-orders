from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)
from project_orders.modules.project_requests.domain.enums.project_request_status import (
    ProjectRequestStatus,
)
from project_orders.modules.project_requests.domain.enums.project_type import ProjectType
from project_orders.modules.project_requests.infrastructure.models.project_request_model import (
    ProjectRequestModel,
)


class SQLAlchemyProjectRequestRepository:
    """Implementação concreta de ProjectRequestRepository usando SQLAlchemy.

    A camada de aplicação depende apenas do Protocol definido em
    domain/repositories — ela não sabe (nem precisa saber) que esta é
    a implementação usada.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, project_request: ProjectRequest) -> ProjectRequest:
        model = ProjectRequestModel(
            id=project_request.id,
            client_name=project_request.client_name,
            client_email=project_request.client_email,
            whatsapp=project_request.whatsapp,
            project_type=project_request.project_type.value,
            description=project_request.description,
            deadline=project_request.deadline,
            budget=project_request.budget,
            status=project_request.status.value,
            created_at=project_request.created_at,
        )
        self._session.add(model)
        await self._session.commit()
        return project_request

    async def get_by_id(self, project_request_id: UUID) -> ProjectRequest | None:
        result = await self._session.execute(
            select(ProjectRequestModel).where(ProjectRequestModel.id == project_request_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None

        return ProjectRequest(
            id=model.id,
            client_name=model.client_name,
            client_email=model.client_email,
            whatsapp=model.whatsapp,
            project_type=ProjectType(model.project_type),
            description=model.description,
            deadline=model.deadline,
            budget=model.budget,
            status=ProjectRequestStatus(model.status),
            created_at=model.created_at,
        )
