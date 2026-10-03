# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Deposits
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
def get_deposit_types(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getDepositTypes", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get deposit types

    Use this resource to get deposit types available when creating an offer. Read more: <a href="../../news/1-pazdziernika-2025-dostosujemy-allegro-api-do-rozporzadzenia-o-systemie-kaucyjnym-m0mLB4XM9Ib" target="_blank">PL</a> / <a href="../../news/on-october-1-2025-we-will-adapt-Allegro-API-to-the-deposit-system-regulation-m0mLB4XM9Ib" target="_blank">EN</a>.


    HTTP: ``GET /deposit/types``
    """
    return call_operation("getDepositTypes", {"header:Accept-Language": Accept_Language})
