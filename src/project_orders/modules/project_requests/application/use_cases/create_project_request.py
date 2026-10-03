from project_orders.modules.project_requests.application.dtos.project_request_input import (
    ProjectRequestInput,
)
from project_orders.modules.project_requests.application.dtos.project_request_output import (
    ProjectRequestOutput,
)
from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)
from project_orders.modules.project_requests.domain.repositories.project_request_repository import (
    ProjectRequestRepository,
)


class CreateProjectRequestUseCase:
    """Caso de uso: cria e persiste uma nova solicitação de projeto.

    Depende apenas do Protocol ProjectRequestRepository — não conhece
    SQLAlchemy nem PostgreSQL diretamente (Dependency Inversion).
    """

    def __init__(self, repository: ProjectRequestRepository) -> None:
        self._repository = repository

    async def execute(self, data: ProjectRequestInput) -> ProjectRequestOutput:
        project_request = ProjectRequest.create(
            client_name=data.client_name,
            client_email=data.client_email,
            whatsapp=data.whatsapp,
            project_type=data.project_type,
            description=data.description,
            deadline=data.deadline,
            budget=data.budget,
        )

        project_request = await self._repository.save(project_request)

        return ProjectRequestOutput.from_domain(project_request)
