# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Stock
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
def get_fulfillment_stock(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentStock", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getFulfillmentStock", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getFulfillmentStock", "query:limit", "limit")),
    ] = None,
    phrase: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getFulfillmentStock", "query:phrase", "phrase")),
    ] = None,
    sort: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getFulfillmentStock", "query:sort", "sort")),
    ] = None,
    productId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getFulfillmentStock", "query:productId", "productId")
        ),
    ] = None,
    productAvailability: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentStock", "query:productAvailability", "productAvailability"
            )
        ),
    ] = None,
    productStatus: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentStock", "query:productStatus", "productStatus"
            )
        ),
    ] = None,
    asnStatus: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getFulfillmentStock", "query:asnStatus", "asnStatus")
        ),
    ] = None,
    outOfStockInFrom: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentStock", "query:outOfStockInFrom", "outOfStockInFrom"
            )
        ),
    ] = None,
    outOfStockInTo: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentStock", "query:outOfStockInTo", "outOfStockInTo"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get available stock

    Use this resource to get a list of the products belonging to the seller, which are in Allegro Warehouse. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-pobrac-aktualne-stany-magazynowe" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#get-available-stock" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/stock``
    """
    return call_operation(
        "getFulfillmentStock",
        {
            "header:Accept-Language": Accept_Language,
            "query:offset": offset,
            "query:limit": limit,
            "query:phrase": phrase,
            "query:sort": sort,
            "query:productId": productId,
            "query:productAvailability": productAvailability,
            "query:productStatus": productStatus,
            "query:asnStatus": asnStatus,
            "query:outOfStockInFrom": outOfStockInFrom,
            "query:outOfStockInTo": outOfStockInTo,
        },
    )
