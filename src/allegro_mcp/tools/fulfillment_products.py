# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Products
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
def get_available_products(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAvailableProducts", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getAvailableProducts", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getAvailableProducts", "query:limit", "limit")),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of available products

    Use this resource to get a list of products that can be added to Advance Ship Notice. The list contains products for which the seller has created offers and is ordered by product's name. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#sprawdz-dostepne-produkty-do-awizacji" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#check-available-products-for-asn" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/available-products``
    """
    return call_operation(
        "getAvailableProducts",
        {"header:Accept-Language": Accept_Language, "query:offset": offset, "query:limit": limit},
    )
