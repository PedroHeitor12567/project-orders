from project_orders.modules.project_requests.application.dtos.project_request_input import (
    ProjectRequestInput,
)
from project_orders.modules.project_requests.application.dtos.project_request_output import (
    ProjectRequestOutput,
)
from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)


class CreateProjectRequestUseCase:
    """Caso de uso: cria uma nova solicitação de projeto.

    Nesta fase (Fase 1) ainda não há persistência: a solicitação é
    criada e devolvida em memória. A integração com repositório será
    adicionada na Fase 2, sem alterar esta assinatura publicamente.
    """

    def execute(self, data: ProjectRequestInput) -> ProjectRequestOutput:
        project_request = ProjectRequest.create(
            client_name=data.client_name,
            client_email=data.client_email,
            whatsapp=data.whatsapp,
            project_type=data.project_type,
            description=data.description,
            deadline=data.deadline,
            budget=data.budget,
        )

        return ProjectRequestOutput.from_domain(project_request)
