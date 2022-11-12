"""API commons.

This package contains different important parts of API in terms of FastAPI like
middleware, dependencies, error and event handlers, API settings, etc.

This package generally configures API and also provides dependencies used for each sub
route.

Worth noting that each sub route must be structured like this package, except multiple
API version support case. Multi-version API might lead to separation of sub route
packages into multiple v1, v2, etc. sub packages. Concrete solution for each case must
be done individually depending on delivery and deployment strategy and considering
business requirements.

----------------------------------------------------------------------------------------
Общее API.

Этот пакет содержит различные важные составляющие API в рамках FastAPI такие как
промежуточные обработчики, зависимости, обработчики событий и ошибок, настройки API и
т.д.

Данный пакет в целом настраивает API и предлагает общие зависимости для каждого под-пути
запроса.

Стоит отметить, что каждый под-путь должен быть структурирован аналогично этому пакеты,
за исключением ситуации с версионированием API. Много-версионное API может привести к
разделению пакета для под-пути на несколько v1, v2 и так далее пакетов. Конкретное
решение для каждой ситуации должно происходить индивидуально в зависимости от стратегии
распространения, поставки и требований бизнеса.
"""
