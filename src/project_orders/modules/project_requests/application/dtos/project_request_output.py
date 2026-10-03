from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr

from project_orders.modules.project_requests.domain.entities.project_request import (
    ProjectRequest,
)
from project_orders.modules.project_requests.domain.enums.project_request_status import (
    ProjectRequestStatus,
)
from project_orders.modules.project_requests.domain.enums.project_type import ProjectType


class ProjectRequestOutput(BaseModel):
    id: UUID
    client_name: str
    client_email: EmailStr
    whatsapp: str
    project_type: ProjectType
    description: str
    deadline: str
    budget: str
    status: ProjectRequestStatus
    created_at: datetime

    @classmethod
    def from_domain(cls, project_request: ProjectRequest) -> ProjectRequestOutput:
        return cls(
            id=project_request.id,
            client_name=project_request.client_name,
            client_email=project_request.client_email,
            whatsapp=project_request.whatsapp,
            project_type=project_request.project_type,
            description=project_request.description,
            deadline=project_request.deadline,
            budget=project_request.budget,
            status=project_request.status,
            created_at=project_request.created_at,
        )
