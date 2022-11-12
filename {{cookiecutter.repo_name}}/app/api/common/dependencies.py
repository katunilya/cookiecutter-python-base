"""Common dependencies.

Usually there are dependencies that check something during the request which makes them
look more like middleware. Check out Global Dependencies FastAPI documentation for
examples.

I personally find this inconvenient, but in case when you don't need to perform some
custom logic after the request or change request data before handling I consider it as
an acceptable solution.

More useful case is dependencies that are not binded to FastAPI as globals, but used as
route dependencies. They can be places here and used in concrete sub routes, but it is
also important that this is not full-feature dependency injection framework. For
dependency injection I encourage to use dependency_injector package.

Also I consider this module to be a good place for dependency_injector's
DeclarativeContainer.

Dependencies must be injected on presentation layer instead of domain to keep it as
flexible and independent from concrete technologies and implementations.

Useful materials:
    - https://fastapi.tiangolo.com/tutorial/dependencies/
    - https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/
    - https://fastapi.tiangolo.com/advanced/testing-dependencies/
    - https://python-dependency-injector.ets-labs.org/

----------------------------------------------------------------------------------------
Общие зависимости.

Как правило здесь находятся зависимости, которые производят те или иные проверки в
процессе обработки запроса, что делает их похожими на промежуточные обработчики.
Посмотрите статью Global Dependencies в документации к FastAPI.

На мой взгляд этот подход вносит разночтение, но для случаев, когда не нужно производить
действия после обработки запроса или менять запрос перед обработкой его можно считать
приемлемым.

Более полезный кейс - зависимости, которые не привязаны к FastAPI глобально, а
используются в конкретных обработчиках. Они могут помещаться здесь и далее
использоваться так где нужно, но стоит помнить, что это не полнофункциональный фреймворк
для инъекции зависимостей. Непосредственно для этого я рекомендую использовать
dependency_injector.

Так же я считаю, что это неплохое место для того, чтобы поместить DeclarativeContainer
из dependency_injector.

Зависимости должны вызываться в презентационном слое вместо слоя бизнес-логики, чтобы
поддерживать его максимально гибким и независимым от конкретных реализаций и технологий.

Полезные материалы:
    - https://fastapi.tiangolo.com/tutorial/dependencies/
    - https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/
    - https://fastapi.tiangolo.com/advanced/testing-dependencies/
    - https://python-dependency-injector.ets-labs.org/
"""
from dependency_injector import containers, providers
from fastapi import FastAPI

from .settings import FastAPISettings


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize common FastAPI dependencies.

    Important that there we do not configure and wire Container. It is done in FastAPI
    factory function in app.api.main module.

    Args:
        app (FastAPI): to bootstrap with global dependencies.

    Returns:
        FastAPI: bootstrapped with global dependencies.
    """
    return app


class Container(containers.DeclarativeContainer):
    """Container for dependencies used in API presentation layer.

    Highly suggested to use Object provider for BaseSettings as Configuration provider
    just looses all typing, validation and logic that might be the part of settings.

    When some dependency must be configured at startup use Abstract dependencies and
    override them on application startup.
    """

    fastapi_settings = providers.Object(FastAPISettings())
