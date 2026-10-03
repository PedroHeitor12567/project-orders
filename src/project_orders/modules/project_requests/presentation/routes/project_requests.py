from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from project_orders.core.database import get_db_session
from project_orders.modules.project_requests.application.dtos.project_request_input import (
    ProjectRequestInput,
)
from project_orders.modules.project_requests.application.dtos.project_request_output import (
    ProjectRequestOutput,
)
from project_orders.modules.project_requests.application.use_cases.create_project_request import (
    CreateProjectRequestUseCase,
)
from project_orders.modules.project_requests.infrastructure.repositories.sqlalchemy_project_request_repository import (
    SQLAlchemyProjectRequestRepository,
)

router = APIRouter(prefix="/api/v1/project-requests", tags=["project-requests"])


@router.post(
    "",
    response_model=ProjectRequestOutput,
    status_code=status.HTTP_201_CREATED,
)
async def create_project_request(
    payload: ProjectRequestInput,
    session: AsyncSession = Depends(get_db_session),
) -> ProjectRequestOutput:
    repository = SQLAlchemyProjectRequestRepository(session)
    use_case = CreateProjectRequestUseCase(repository)
    return await use_case.execute(payload)
