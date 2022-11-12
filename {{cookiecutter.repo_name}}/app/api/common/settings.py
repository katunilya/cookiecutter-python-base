"""Common settings.

Any application requires settings. This module contains settings specifically for
FastAPI and API layer. Do not include there anything related to infrastructure or domain
logic. This dependencies should exist separately for flexibility purposes.

For settings I suggest using environment variables (see *.env files in settings folder)
and pydantic BaseSettings for reading and validation. It fulfills all requirements that
I personally have to settings management.

Useful materials:
    - https://pydantic-docs.helpmanual.io/usage/settings/

----------------------------------------------------------------------------------------
Общие настройки.

Любое приложение требует настроек. Этот модуль содержит в себе настройки специально для
FastAPI и API слоя. Не включайте сюда что-либо относящееся к инфраструктуре или
бизнес-логике. Эти зависимости должны существовать отдельно для большей гибкости.

Для настроек я предлагаю использовать переменные окружения (смотри *.env файлы в папке
settings) и pydantic BaseSettings для чтения и валидации. Он полностью покрывает мои
требования к настройкам.

Полезные материалы:
    - https://pydantic-docs.helpmanual.io/usage/settings/
"""
from fastapi import FastAPI
from pydantic import BaseSettings, Field


class FastAPISettings(BaseSettings):
    """FastAPI settings from environment variables.

    Configuration options must be named in upper snake case as they are constant.

    When more configuration options required add needed fields, add environment
    variables to /settings/debug.env and /settings/docker.env and modify create_fastapi
    method.
    """

    DEBUG: bool = Field(default=False)
    TITLE: str = Field(default="{{cookiecutter.project_name}}")
    DESCRIPTION: str = Field(default="{{cookiecutter.description}}")
    VERSION: str = Field(default="{{cookiecutter.version}}")
    ROOT_PATH: str = Field(default="")

    CORS_ALLOW_ORIGINS: list[str] = Field(default=["*"])
    CORS_ALLOW_CREDENTIALS: bool = Field(default=True)
    CORS_ALLOW_METHODS: list[str] = Field(default=["*"])
    CORS_ALLOW_HEADERS: list[str] = Field(default=["*"])

    class Config:  # noqa
        env_prefix = "FASTAPI_"
        frozen = True

    def create_fastapi(self) -> FastAPI:
        """Initialize common FastAPI middleware.

        Returns:
            FastAPI: configured based on settings class.
        """
        return FastAPI(
            debug=self.DEBUG,
            title=self.TITLE,
            description=self.DESCRIPTION,
            version=self.VERSION,
            root_path=self.ROOT_PATH,
        )
