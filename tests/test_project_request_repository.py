import uuid

import pytest

from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)
from project_orders.modules.project_requests.domain.enums.project_type import ProjectType
from project_orders.modules.project_requests.infrastructure.repositories.sqlalchemy_project_request_repository import (
    SQLAlchemyProjectRequestRepository,
)


@pytest.mark.asyncio
async def test_save_and_get_by_id(db_session):
    repository = SQLAlchemyProjectRequestRepository(db_session)
    project_request = ProjectRequest.create(
        client_name="Ana Paula",
        client_email="ana@example.com",
        whatsapp="84977776666",
        project_type=ProjectType.API_BACKEND,
        description="Preciso de uma API para integrar meu estoque com o e-commerce.",
        deadline="60 dias",
        budget="R$ 8.000 - R$ 12.000",
    )

    saved = await repository.save(project_request)
    fetched = await repository.get_by_id(saved.id)

    assert fetched is not None
    assert fetched.id == saved.id
    assert fetched.client_name == "Ana Paula"
    assert fetched.status == project_request.status


@pytest.mark.asyncio
async def test_get_by_id_returns_none_when_not_found(db_session):
    repository = SQLAlchemyProjectRequestRepository(db_session)

    result = await repository.get_by_id(uuid.uuid4())

    assert result is None
