import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from project_orders.core.config import get_settings
from project_orders.core.database import Base, get_db_session
from project_orders.main import create_app


@pytest.fixture
async def db_session():
    """Cria um banco de teste isolado para cada teste."""

    settings = get_settings()

    if not settings.database_url:
        raise RuntimeError(
            "DATABASE_URL não configurada. Defina-a no .env antes de executar os testes."
        )

    engine = create_async_engine(
        settings.database_url,
        pool_pre_ping=True,
    )

    session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

        async with session_factory() as session:
            yield session

        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)

    finally:
        await engine.dispose()


@pytest.fixture
async def client(db_session):
    app = create_app()

    async def override_get_db_session():
        yield db_session

    app.dependency_overrides[get_db_session] = override_get_db_session

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as async_client:
        yield async_client

    app.dependency_overrides.clear()