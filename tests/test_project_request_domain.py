from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)
from project_orders.modules.project_requests.domain.enums.project_request_status import (
    ProjectRequestStatus,
)
from project_orders.modules.project_requests.domain.enums.project_type import ProjectType


def test_new_project_request_is_always_created_as_pending():
    project_request = ProjectRequest.create(
        client_name="Maria Souza",
        client_email="maria@example.com",
        whatsapp="84988887777",
        project_type=ProjectType.WEBSITE,
        description="Preciso de um site institucional para minha clínica odontológica.",
        deadline="45 dias",
        budget="R$ 3.000 - R$ 5.000",
    )

    assert project_request.status == ProjectRequestStatus.PENDING
    assert project_request.id is not None
    assert project_request.created_at is not None
