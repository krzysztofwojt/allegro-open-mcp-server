# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Returns
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
def get_refund_dispositions_report(
    *,
    createdAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundDispositionsReport", "query:createdAt.gte", "createdAt_gte"
            )
        ),
    ] = None,
    createdAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundDispositionsReport", "query:createdAt.lte", "createdAt_lte"
            )
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getRefundDispositionsReport", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getRefundDispositionsReport", "query:offset", "offset")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundDispositionsReport", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get refund dispositions report

    Use this resource to get refund dispositions for returns handled in One Fulfillment. The response contains data from the last 90 days only. The response contains both buyer returns and operational returns. When there is no matching disposition, the `report` array is empty. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-pobrac-raport-dyspozycji-zwrotu-srodkow" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#how-to-retrieve-the-refund-disposition-report" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/returns/refund-dispositions``
    """
    return call_operation(
        "getRefundDispositionsReport",
        {
            "query:createdAt.gte": createdAt_gte,
            "query:createdAt.lte": createdAt_lte,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )
