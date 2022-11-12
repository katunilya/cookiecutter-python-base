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
