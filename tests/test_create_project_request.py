import pytest

VALID_PAYLOAD = {
    "client_name": "João Silva",
    "client_email": "joao@example.com",
    "whatsapp": "84999999999",
    "project_type": "LANDING_PAGE",
    "description": "Preciso de uma landing page para apresentar minha empresa e meus serviços.",
    "deadline": "30 dias",
    "budget": "R$ 1.000 - R$ 2.000",
}


@pytest.mark.asyncio
async def test_create_project_request_success(client):
    response = await client.post("/api/v1/project-requests", json=VALID_PAYLOAD)

    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "PENDING"
    assert body["client_name"] == VALID_PAYLOAD["client_name"]
    assert "id" in body
    assert "created_at" in body


@pytest.mark.asyncio
async def test_create_project_request_rejects_invalid_email(client):
    payload = {**VALID_PAYLOAD, "client_email": "email-invalido"}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_project_request_rejects_invalid_project_type(client):
    payload = {**VALID_PAYLOAD, "project_type": "MOBILE_APP"}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_project_request_rejects_missing_required_field(client):
    payload = {k: v for k, v in VALID_PAYLOAD.items() if k != "client_email"}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_project_request_rejects_unknown_field(client):
    payload = {**VALID_PAYLOAD, "status": "APPROVED"}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_project_request_rejects_description_too_short(client):
    payload = {**VALID_PAYLOAD, "description": "curto"}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_project_request_rejects_client_name_too_long(client):
    payload = {**VALID_PAYLOAD, "client_name": "a" * 101}

    response = await client.post("/api/v1/project-requests", json=payload)

    assert response.status_code == 422
