from enum import StrEnum


class ProjectRequestStatus(StrEnum):
    PENDING = "PENDING"
    CONTACTED = "CONTACTED"
    IN_NEGOTIATION = "IN_NEGOTIATION"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"
