# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Ingredients
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
def parse_ingredients(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "parseIngredients", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("parseIngredients", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Parse product ingredients

    Use this resource to parse raw, free-text ingredients declarations into structured ingredient lists for one or more products. Every submitted product text is parsed independently. The response contains parsed items together with errors and warnings detected for each product.


    HTTP: ``POST /ingredients/parse``
    """
    return call_operation(
        "parseIngredients", {"header:Accept-Language": Accept_Language, "body": body}
    )
