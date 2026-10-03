from fastapi import APIRouter, status

from project_orders.modules.project_requests.application.dtos.project_request_input import (
    ProjectRequestInput,
)
from project_orders.modules.project_requests.application.dtos.project_request_output import (
    ProjectRequestOutput,
)
from project_orders.modules.project_requests.application.use_cases.create_project_request import (
    CreateProjectRequestUseCase,
)

router = APIRouter(prefix="/api/v1/project-requests", tags=["project-requests"])


@router.post(
    "",
    response_model=ProjectRequestOutput,
    status_code=status.HTTP_201_CREATED,
)
async def create_project_request(payload: ProjectRequestInput) -> ProjectRequestOutput:
    use_case = CreateProjectRequestUseCase()
    return use_case.execute(payload)
