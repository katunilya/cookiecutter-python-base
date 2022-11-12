"""Entrypoint for ASGI.

This module provides a factory function for FastAPI application where it is fully
configured. Factory function is needed for testing purposes and cleaner environment
handling. For example some global sqlalchemy engine can cause an error during tests if
module the declares it is accidentally imported, but actual connection is not needed.

Thus FastAPI in case of uvicorn ASGI must be called with --factory flag.

Worth noting that for building application there I am using toolz, however I replacing
it some it (at least partially) with fundom, which provides similar features for
building declarative function pipelines, but (opinionated) implements better monad
approach than returns.

----------------------------------------------------------------------------------------
Точка входа для ASGI

Данный модель содержит функцию-фабрику для FastAPI приложения, где оно полностью
настраивается. Функция-фабрика нужна для тестирования и более чистого окружения.
Например если где-то объявлена глобальная переменная с sqlalchemy engine, то может
произойти ошибка при неочевидном импортировании данного модуля в ходе теста, где это
подключение не нужно.

Таким образом FastAPI в случае с uvicorn ASGI должно запускать с --factory флагом.

Стоит отметить, что для построения приложения я использую toolz, однако предполагаю
важным со временем заменить его (хотя бы частично) на fundom, так как он предлагает
похожую функциональность для создания декларативных цепочек функций, но (на мой взгляд)
предлагает лучший подход к монадам, чем returns.
"""
from fastapi import FastAPI
from toolz import pipe

from .common import dependencies, endpoints, error_handlers, event_handlers, middleware


def bootstrap() -> FastAPI:
    """Factory function for FastAPI."""
    # Initialize dependency container
    container = dependencies.Container(
        # Abstract dependencies are configured via override or arguments for Container
        # constructor
    )
    # Wire package and modules - API only as this is the only place where dependencies
    # are injected
    container.wire(
        modules=[
            dependencies,
            endpoints,
            error_handlers,
            event_handlers,
            middleware,
        ],
        packages=[],
    )
    fastapi_settings = container.fastapi_settings()

    return pipe(
        fastapi_settings.create_fastapi(),
        # bootstrap commons
        dependencies.bootstrap,
        middleware.bootstrap,
        error_handlers.bootstrap,
        event_handlers.bootstrap,
        # bootstrap endpoints and sub routes
        endpoints.bootstrap,
    )
