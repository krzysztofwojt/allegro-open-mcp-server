# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Pricing
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
@requires_writes_enabled
def calculate_fee_preview(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "calculateFeePreviewUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("calculateFeePreviewUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Calculate fee and commission for an offer

    Provides information about fee and commission for an offer. This resource is limited to 25 requests per second for a single user. Read more: <a href="../../tutorials/jak-sprawdzic-oplaty-nn9DOL5PASX#kalkulator-oplat" target="_blank">PL</a> / <a href="../../tutorials/how-to-check-the-fees-3An6Wame3Um#fee-calculator" target="_blank">EN</a>.


    HTTP: ``POST /pricing/offer-fee-preview``
    """
    return call_operation(
        "calculateFeePreviewUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def offer_quotes_public(
    *,
    offer_id: Annotated[
        list[str],
        Field(
            json_schema_extra=input_schema(
                "offerQuotesPublicUsingGET", "query:offer.id", "offer_id"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "offerQuotesPublicUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's current offer quotes

    This endpoint returns current offer quotes (listing and promo fees) cycles for authenticated user and list of offers. Read more: <a href="../../tutorials/jak-sprawdzic-oplaty-nn9DOL5PASX#data-naliczenia-kolejnej-oplaty" target="_blank">PL</a> / <a href="../../tutorials/how-to-check-the-fees-3An6Wame3Um#check-when-a-fee-is-charged" target="_blank">EN</a>.


    HTTP: ``GET /pricing/offer-quotes``
    """
    return call_operation(
        "offerQuotesPublicUsingGET",
        {"query:offer.id": offer_id, "header:Accept-Language": Accept_Language},
    )
