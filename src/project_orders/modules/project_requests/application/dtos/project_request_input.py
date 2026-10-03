from pydantic import BaseModel, ConfigDict, EmailStr, Field

from project_orders.modules.project_requests.domain.enums.project_type import ProjectType


class ProjectRequestInput(BaseModel):
    """DTO de entrada da API, pública e não confiável por padrão.

    extra="forbid" garante que qualquer campo inesperado — incluindo
    uma tentativa do cliente de enviar "status" — seja rejeitado com
    422 em vez de ser silenciosamente ignorado.
    """

    model_config = ConfigDict(extra="forbid")

    client_name: str = Field(min_length=2, max_length=100)
    client_email: EmailStr
    whatsapp: str = Field(min_length=8, max_length=20)
    project_type: ProjectType
    description: str = Field(min_length=20, max_length=3000)
    deadline: str = Field(min_length=2, max_length=100)
    budget: str = Field(min_length=1, max_length=100)
