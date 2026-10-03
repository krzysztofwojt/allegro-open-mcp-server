# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Charity
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
def search_fundraising_campaigns(
    *,
    limit: Annotated[
        int,
        Field(json_schema_extra=input_schema("searchFundraisingCampaigns", "query:limit", "limit")),
    ],
    phrase: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("searchFundraisingCampaigns", "query:phrase", "phrase")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchFundraisingCampaigns", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Search fundraising campaigns

    Use this resource to search fundraising campaigns. Read more: <a href="../../news/wystaw-oferte-charytatywna-na-allegro-MR87PBxZySY" target="_blank">PL</a> / <a href="../../news/list-a-charity-offer-on-allegro-LRV0572GOhr" target="_blank">EN</a>.


    HTTP: ``GET /charity/fundraising-campaigns``
    """
    return call_operation(
        "searchFundraisingCampaigns",
        {"query:limit": limit, "query:phrase": phrase, "header:Accept-Language": Accept_Language},
    )
