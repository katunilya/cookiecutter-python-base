"""Common endpoints.

As an agreement handler functions are called as "<method>_<route>" in standard python
snake case.

For example if handler has full route "task/{uid}" and GET method then function is
called "get_task_uid".

Handler can ignore docstrings, but then description is required. response_model and
status_code parameters for endpoint are also required (except 204 No Content).

Usually there we have some app health/ping/info endpoints. There I provide only ping
health endpoint. Fully functional health endpoint is recommended and should return:
    - status of the connections to the infrastructure services used by the service
      instance
    - status of the host, e.g. disk space
    - application specific logic

Note on implementation: fastapi Request object contains app field with FastAPI so some
application info can be extracted from it. For host information use shutil package for
example.

Useful materials:
    - https://fastapi.tiangolo.com/
    - https://microservices.io/patterns/observability/health-check-api.html

----------------------------------------------------------------------------------------
Общие запросы.

Как договоренность название обработчиков запросов должно быть "<method>_<route>" в
стандартном для python snake case.

Например если обработчик имеет полный путь "task/{uid}" и GET метод, то функция должна
называться "get_task_uid".

Обработчики могут игнорировать docstrings, но тогда description обязателен.
response_model и status_code тоже являются обязательными параметрами запроса (кроме 204
No Content).

Обычно здесь должны быть health/ping/info запросы. В данном случае реализован только
ping запрос. Полновесный health запрос рекомендуется и должен возвращать:
    - статус подключения к инфраструктурным зависимостям
    - статус хоста (например использование памяти)
    - информацию специфичную для конкретного приложения

Заметка по реализации: fastapi Request содержит поле app типа FastAPI из которого можно
извлечь некоторую информацию о приложении. Для информации о хосте можно использовать
пакет shutil.

Полезные материалы:
    - https://fastapi.tiangolo.com/
    - https://microservices.io/patterns/observability/health-check-api.html
"""
from fastapi import APIRouter, FastAPI, status

router = APIRouter()


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize common FastAPI endpoints.

    Args:
        app (FastAPI): to bootstrap with common endpoints.

    Returns:
        FastAPI: bootstrapped with common endpoints.
    """
    app.include_router(router, tags=["Common"])
    return app


@router.get(
    "/ping",
    description="Health ping endpoint that just checks that app is up and running",
    status_code=status.HTTP_204_NO_CONTENT,
)
def get_ping() -> None:  # noqa
    return


# TODO: implement common /health endpoint with application settings info and host info
