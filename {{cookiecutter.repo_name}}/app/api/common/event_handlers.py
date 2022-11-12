"""Common event handlers.

According to ASGI specification there are 2 main lifecycle events - "startup" and
"shutdown" that correspondingly happen on application startup and shutdown. This events
are needed for initializing and freeing resources.

As an agreement startup events must start with "startup_" and shutdown with "shutdown_".

There might be misconception on startup and factory function. Factory function runs even
before startup event, so there we configure our application (for example DI container),
but on startup we initialize resources (for example beanie_init for initializing
MongoDB).

Useful materials:
    - https://www.starlette.io/events/
    - https://fastapi.tiangolo.com/advanced/events/
    - https://asgi.readthedocs.io/en/latest/specs/lifespan.html

----------------------------------------------------------------------------------------
Общие обработчики событий.

В соответствие со спецификацией ASGI есть 2 события жизненного цикла приложений -
"startup" и "shutdown", которые соответствуют запуски и окончанию работы сервера. Эти
события нужны для инициализации и освобождения ресурсов.

Как договоренность события запуска должны начинаться со "startup_", а окончания работы с
"shutdown_".

Наличие события запуска и функции-фабрики может привести к некоторому недопониманию их
целей. Функция фабрика отрабатывает еще до запуска приложения как такового, поэтому в
ней мы конфигурируем наше приложение (например зависимости), а на запуске мы
инициализируем ресурсы (например beanie_init для инициализации MongoDB).

Полезные материалы:
    - https://www.starlette.io/events/
    - https://fastapi.tiangolo.com/advanced/events/
    - https://asgi.readthedocs.io/en/latest/specs/lifespan.html
"""

from fastapi import FastAPI


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize common FastAPI event handlers.

    Args:
        app (FastAPI): to bootstrap with common event handlers.

    Returns:
        FastAPI: bootstrapped with common event handlers.
    """
    return app
