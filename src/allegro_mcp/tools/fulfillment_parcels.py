# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Parcels
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
def get_fulfillment_order_parcels(
    *,
    orderId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getFulfillmentOrderParcels", "path:orderId", "orderId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentOrderParcels", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of shipped parcels

    Use this resource to get list of parcels and included items for a given order. Items include detailed information such as expiration dates and serial numbers. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-obslugiwac-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#how-to-handle-orders" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/orders/{orderId}/parcels``
    """
    return call_operation(
        "getFulfillmentOrderParcels",
        {"path:orderId": orderId, "header:Accept-Language": Accept_Language},
    )
