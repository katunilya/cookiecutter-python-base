"""Common API contracts.

Contract is some model used for client-server interaction. Contracts are responsible for
converting domain models to API-friendly models and vice versa.

Common example is camel case used in TypeScript/JavaScript frontend applications and
json which is not used in python, so linter argue on using that case directly in code.
For solving this specific problem we have pydantic aliases which are present in API
layer and not domain one.

Contracts must have "Request" or "Response" postfix depending on use-case. If we have
Contract that is used both as response and request than it must have postfix "Contract".

Contracts must be well documented for better OpenAPI usage. Contracts must always have
descriptive docstring and description for each field and also include rules and
limitation.

Useful materials:
    - https://fastapi.tiangolo.com/
    - https://pydantic-docs.helpmanual.io/
    - https://github.com/chrisdoherty4/python-case-converter
    - https://json-schema.org/

----------------------------------------------------------------------------------------
Общие контракты API.

Контракт - некоторая модель для клиент-серверного взаимодействия. Контракты отвечают за
перевод доменных моделей данных в модели данных понятные в рамках API и наоборот.

Частный пример этого - camel case, который используются в TypeScript/JavaScript
клиентских приложениях и json, но не используется в python, поэтому линтеры могут
воспринимать его как ошибку в наименовании при использовании его напрямую в коде.
Конкретно эта проблема решается псевдонимами pydantic, которые используются именно в
API, а не бизнес-логике.

Контракты должны иметь постфикс "Request" или "Response" в зависимости от места
применения. Если же контракт используется в обоих случаях, то он должен иметь постфикс
"Contract".

Контракты должны быть хорошо задокументированы, для повышения качества OpenAPI.
Контракты всегда должны сопровождаться docstring, а каждое поле должно иметь описание и
ограничения предметной области.

Полезные материалы:
    - https://fastapi.tiangolo.com/
    - https://pydantic-docs.helpmanual.io/
    - https://github.com/chrisdoherty4/python-case-converter
    - https://json-schema.org/
"""
from caseconverter import camelcase  # noqa: PyPI package name differs from actual
from pydantic import BaseModel


class JSONContract(BaseModel):
    """Base class for handling camelCase json naming format."""

    class Config:  # noqa
        alias_generator = camelcase
