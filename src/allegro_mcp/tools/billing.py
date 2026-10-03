# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Billing
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
def get_billing_entries(
    *,
    marketplaceId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getBillingEntries", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    occurredAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getBillingEntries", "query:occurredAt.gte", "occurredAt_gte"
            )
        ),
    ] = None,
    occurredAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getBillingEntries", "query:occurredAt.lte", "occurredAt_lte"
            )
        ),
    ] = None,
    type_id: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getBillingEntries", "query:type.id", "type_id")),
    ] = None,
    offer_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getBillingEntries", "query:offer.id", "offer_id")),
    ] = None,
    order_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getBillingEntries", "query:order.id", "order_id")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getBillingEntries", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getBillingEntries", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getBillingEntries", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of billing entries

    Use this resource to get a list of billing entries. The billing entries are sorted in descending order (newest first) by the date on which they occurred. Read more: <a href="../../tutorials/jak-sprawdzic-oplaty-nn9DOL5PASX#historia-operacji-billingowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-check-the-fees-3An6Wame3Um#billing-operations" target="_blank">EN</a>.


    HTTP: ``GET /billing/billing-entries``
    """
    return call_operation(
        "getBillingEntries",
        {
            "query:marketplaceId": marketplaceId,
            "query:occurredAt.gte": occurredAt_gte,
            "query:occurredAt.lte": occurredAt_lte,
            "query:type.id": type_id,
            "query:offer.id": offer_id,
            "query:order.id": order_id,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_billing_types(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getBillingTypes", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of billing types

    Use this resource to get a list of all billing types. Type names are localized according to the "Accept-Language" header. Read more: <a href="../../tutorials/jak-sprawdzic-oplaty-nn9DOL5PASX#historia-operacji-billingowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-check-the-fees-3An6Wame3Um#billing-operations" target="_blank">EN</a>.


    HTTP: ``GET /billing/billing-types``
    """
    return call_operation("getBillingTypes", {"header:Accept-Language": Accept_Language})
