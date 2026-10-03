from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from project_orders.core.config import get_settings


class Base(DeclarativeBase):
    """Base declarativa compartilhada por todos os models do SQLAlchemy."""


_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def get_engine() -> AsyncEngine:
    """Retorna o engine assíncrono (criado uma única vez).

    Lança um erro explícito se DATABASE_URL não estiver configurada,
    em vez de falhar de forma obscura mais adiante.
    """
    global _engine
    if _engine is None:
        settings = get_settings()
        if not settings.database_url:
            raise RuntimeError(
                "DATABASE_URL não configurada. Defina-a no .env antes de usar o banco."
            )
        _engine = create_async_engine(settings.database_url, pool_pre_ping=True)
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(bind=get_engine(), expire_on_commit=False)
    return _session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency do FastAPI: fornece uma sessão por requisição."""
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session
