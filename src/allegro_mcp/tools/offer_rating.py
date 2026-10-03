# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Offer rating
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
def offer_rating_get(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("offerRatingGET", "path:offerId", "offerId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "offerRatingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get offer rating

    Use this resource to get offer rating. Read more: <a href="../../news/nowy-zasob-do-pobrania-oceny-produktu-q018mmPe0H7" target="_blank">PL</a> / <a href="../../news/new-resource-to-retrieve-product-rating-q018mmPrWUX" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/{offerId}/rating``
    """
    return call_operation(
        "offerRatingGET", {"path:offerId": offerId, "header:Accept-Language": Accept_Language}
    )
