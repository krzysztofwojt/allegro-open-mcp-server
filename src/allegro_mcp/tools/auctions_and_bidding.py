# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Auctions and Bidding
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
def place_bid(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("placeBid", "path:offerId", "offerId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("placeBid", "header:Accept-Language", "Accept_Language")
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None, Field(json_schema_extra=input_schema("placeBid", "body", "body"))
    ] = None,
) -> Any | ErrorResponse:
    """Place a bid in an auction

    Use this resource to place a bid in an auction. Read more: <a href="../../news/nowe-zasoby-zloz-oferte-kupna-w-licytacji-q018m02vDT1" target="_blank">PL</a> / <a href="../../news/new-resources-place-a-bid-in-an-auction-rjWwEj1e7sG" target="_blank">EN</a>.


    HTTP: ``PUT /bidding/offers/{offerId}/bid``
    """
    return call_operation(
        "placeBid",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_bid(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("getBid", "path:offerId", "offerId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getBid", "header:Accept-Language", "Accept_Language")
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get current user's bid information

    Use this resource to retrieve current user's bid information. Read more: <a href="../../news/nowe-zasoby-zloz-oferte-kupna-w-licytacji-q018m02vDT1" target="_blank">PL</a> / <a href="../../news/new-resources-place-a-bid-in-an-auction-rjWwEj1e7sG" target="_blank">EN</a>.


    HTTP: ``GET /bidding/offers/{offerId}/bid``
    """
    return call_operation(
        "getBid", {"path:offerId": offerId, "header:Accept-Language": Accept_Language}
    )
