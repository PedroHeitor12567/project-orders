from typing import Protocol
from uuid import UUID

from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)


class ProjectRequestRepository(Protocol):
    """Porta (interface) que a camada de aplicação depende.

    A implementação concreta (SQLAlchemy, em memória para testes, etc.)
    vive na camada de infraestrutura. Isso é a Inversão de Dependência
    descrita na seção 5 da especificação: as regras de negócio não
    conhecem PostgreSQL diretamente.
    """

    async def save(self, project_request: ProjectRequest) -> ProjectRequest: ...

    async def get_by_id(self, project_request_id: UUID) -> ProjectRequest | None: ...
