"""Common error handlers.

When application raises exception FastAPI commonly just returns 500 Internal Server
Error status code with no detailed description. To fix this problem we can provide
custom error handlers.

This is considerable way of handling error, however if we stick to monadic error
handling approach with Result monad we can do it by providing some singledispatch
function that just takes Exception object and based on type returns different Responses.

Both ways are fine depending on approach used in domain layer.

Useful materials:
    - https://returns.readthedocs.io/en/latest/pages/result.html
    - https://fastapi.tiangolo.com/tutorial/handling-errors/

----------------------------------------------------------------------------------------
Общие обработчики ошибок.

Когда приложение падает с ошибкой FastAPI обычно возвращает 500 Internal Server Error
без какого-либо описания. Чтобы исправить эту проблему мы можем добавить
пользовательские обработчики ошибок.

Это приемлемый путь обработки ошибок, однако если придерживать монадической обработки с
использованием монады Result, то мы можем получить аналогичное поведение singledispatch
функцией, которая принимает Exception и в зависимости от типа возвращает нужный
Response.

Оба способы приемлемы и зависят от подхода к разработке в бизнес-логике.

Полезные материалы:
    - https://returns.readthedocs.io/en/latest/pages/result.html
    - https://fastapi.tiangolo.com/tutorial/handling-errors/
"""

from fastapi import FastAPI


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize common FastAPI error handlers.

    Args:
        app (FastAPI): to bootstrap with common error handlers.

    Returns:
        FastAPI: bootstrapped with common error handlers.
    """
    return app
