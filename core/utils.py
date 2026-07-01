from enum import StrEnum
from typing import Awaitable, Callable

from django.http import HttpRequest, HttpResponse


class Methods(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


async def method_mapper(
    request: HttpRequest,
    mapper: dict[Methods, Callable[[], Awaitable[HttpResponse]]],
) -> HttpResponse:
    if not request.method:
        return HttpResponse(status=405)
    try:
        method = Methods(request.method)
        return await mapper[method]()
    except (ValueError, KeyError):
        return HttpResponse(status=405)
