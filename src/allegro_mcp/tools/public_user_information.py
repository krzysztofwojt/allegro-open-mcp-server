# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Public user information
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
def get_user_summary(
    *,
    userId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getUserSummaryUsingGET", "path:userId", "userId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserSummaryUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get any user's ratings summary

    Use this resource to receive feedback statistics. Read more: <a href="../../news/nowe-zasoby-ktorymi-pobierzesz-informacje-o-ocenach-ZM9L1WPBbUb" target="_blank">PL</a> / <a href="../../news/new-resources-to-download-sales-feedback-d2VYERBMRiz" target="_blank">EN</a>.


    HTTP: ``GET /users/{userId}/ratings-summary``
    """
    return call_operation(
        "getUserSummaryUsingGET", {"path:userId": userId, "header:Accept-Language": Accept_Language}
    )
