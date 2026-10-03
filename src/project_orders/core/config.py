from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações centralizadas da aplicação.

    Todos os valores sensíveis vêm de variáveis de ambiente / .env,
    nunca hardcoded no código-fonte.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Project Orders"
    app_version: str = "0.1.0"
    environment: Literal["development", "production", "test"] = "development"

    # Preenchido a partir da Fase 2 (persistência)
    database_url: str | None = None

    # Preenchido a partir da Fase 3 (e-mail)
    email_api_key: str | None = None
    email_from: str | None = None
    email_to: str | None = None

    # Preenchido a partir da Fase 4 (segurança)
    cors_origins: list[str] = []

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    """Retorna a instância única (cacheada) de Settings.

    Usar via Depends(get_settings) no FastAPI garante que a
    configuração seja carregada uma única vez e possa ser
    facilmente substituída em testes (dependency override).
    """
    return Settings()