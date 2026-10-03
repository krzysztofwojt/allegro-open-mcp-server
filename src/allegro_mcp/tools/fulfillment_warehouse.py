# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Warehouse
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
def get_fulfillment_warehouse(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentWarehouse", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get seller warehouse

    Use this resource to get the warehouse assigned to the seller.


    HTTP: ``GET /fulfillment/warehouse``
    """
    return call_operation("getFulfillmentWarehouse", {"header:Accept-Language": Accept_Language})
