# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Information about marketplaces
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from ..errors import ErrorResponse
from ._decorators import requires_writes_enabled
from ._runtime import allegro_call, mcp
from ._request import call_operation, input_schema


@mcp.tool
@allegro_call
def marketplaces_get(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "marketplacesGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get details for all marketplaces in allegro

    Use this resource to get information about all the marketplaces on the platform. Read more: <a href="../../tutorials/wystawianie-i-zarzadzanie-oferta-w-serwisach-zagranicznych-wwzjP4M8gTZ#serwis-bazowy-uzytkownika-oraz-lista-dostepnych-serwisow" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-offers-on-foreign-marketplaces-7GndGjeAATn#user-s-base-marketplace-and-list-of-available-marketplaces" target="_blank">EN</a>.


    HTTP: ``GET /marketplaces``
    """
    return call_operation("marketplacesGET", {"header:Accept-Language": Accept_Language})
