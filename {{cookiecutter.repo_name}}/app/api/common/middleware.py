"""Common middleware.

Middleware is the same concept as python decorator, but specifically for requests. Thus
you don't need to wrap endpoint handlers with a whole bunch of decorators - just add
middleware, where it is needed in FastAPI.

Useful materials:
    - https://fastapi.tiangolo.com/tutorial/middleware/
    - https://fastapi.tiangolo.com/advanced/middleware/

----------------------------------------------------------------------------------------
Общие промежуточные обработчики.

Промежуточные обработчики - та же идея, что и декораторы в python, но специально для
запросов. Поэтому не нужно в ручную привязывать к каждому запросу целую кучу декораторов
- достаточно просто добавить промежуточный обработчик там где это нужно в FastAPI.

Полезные материалы:
    - https://fastapi.tiangolo.com/tutorial/middleware/
    - https://fastapi.tiangolo.com/advanced/middleware/
"""

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from toolz import pipe

from .dependencies import Container
from .settings import FastAPISettings


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize common FastAPI middleware.

    Args:
        app (FastAPI): to bootstrap with common middleware.

    Returns:
        FastAPI: bootstrapped with common middleware.
    """
    return pipe(
        app,
        __bootstrap_cors,
    )


@inject
def __bootstrap_cors(
    app: FastAPI,
    fastapi_settings: FastAPISettings = Provide[Container.fastapi_settings],
) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=fastapi_settings.CORS_ALLOW_ORIGINS,
        allow_credentials=fastapi_settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=fastapi_settings.CORS_ALLOW_METHODS,
        allow_headers=fastapi_settings.CORS_ALLOW_HEADERS,
    )
    return app
