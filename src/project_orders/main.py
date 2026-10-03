import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from project_orders.core.config import get_settings
from project_orders.modules.project_requests.presentation.routes.project_requests import (
    router as project_requests_router,
)

logger = logging.getLogger("project_orders")


def create_app() -> FastAPI:
    """Application factory.

    Usar uma factory (em vez de uma instância global de módulo)
    facilita testes, permite configuração diferente por ambiente
    e evita import side-effects indesejados.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        # Em produção, esconder docs interativos reduz superfície de
        # reconhecimento por atacantes automatizados.
        docs_url="/docs" if not settings.is_production else None,
        redoc_url="/redoc" if not settings.is_production else None,
        openapi_url="/openapi.json" if not settings.is_production else None,
    )

    register_exception_handlers(app)
    register_routes(app)

    return app


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        # Nunca expor stack trace, mensagens internas ou detalhes de
        # infraestrutura ao cliente. O detalhe completo vai só para o log.
        logger.exception("Unhandled error on %s %s", request.method, request.url.path)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error."},
        )


def register_routes(app: FastAPI) -> None:
    settings = get_settings()

    @app.get("/health", tags=["health"])
    async def health_check() -> dict[str, str]:
        return {
            "status": "ok",
            "environment": settings.environment,
        }

    app.include_router(project_requests_router)


app = create_app()