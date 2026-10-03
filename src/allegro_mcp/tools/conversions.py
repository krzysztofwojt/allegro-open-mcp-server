# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Conversions
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
def get_cps_conversions(
    *,
    orderCreatedAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions", "query:orderCreatedAt.gte", "orderCreatedAt_gte"
            )
        ),
    ] = None,
    orderCreatedAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions", "query:orderCreatedAt.lte", "orderCreatedAt_lte"
            )
        ),
    ] = None,
    lastModifiedAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions", "query:lastModifiedAt.gte", "lastModifiedAt_gte"
            )
        ),
    ] = None,
    lastModifiedAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions", "query:lastModifiedAt.lte", "lastModifiedAt_lte"
            )
        ),
    ] = None,
    status: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCpsConversions", "query:status", "status")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCpsConversions", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCpsConversions", "query:limit", "limit")),
    ] = None,
    includePublisherUrlParameters: Annotated[
        dict[str, Any] | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions",
                "query:includePublisherUrlParameters",
                "includePublisherUrlParameters",
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCpsConversions", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """[BETA] List CPS conversions

    Use this resource to find your CPS (Cost Per Sale) conversions for specific filters. The response contains a list of CPS conversions that correspond with the specified parameters. Read more: <a href="../../tutorials/afiliacja-0A1bPnwVwUq#jak-pobrac-informacje-o-konwersji-cps" target="_blank">PL</a> / <a href="../../tutorials/affiliation-8do60yLKPIq#how-to-retrieve-cps-conversion-information" target="_blank">EN</a>.


    HTTP: ``GET /affiliate/conversions/cps``
    """
    return call_operation(
        "getCpsConversions",
        {
            "query:orderCreatedAt.gte": orderCreatedAt_gte,
            "query:orderCreatedAt.lte": orderCreatedAt_lte,
            "query:lastModifiedAt.gte": lastModifiedAt_gte,
            "query:lastModifiedAt.lte": lastModifiedAt_lte,
            "query:status": status,
            "query:offset": offset,
            "query:limit": limit,
            "query:includePublisherUrlParameters": includePublisherUrlParameters,
            "header:Accept-Language": Accept_Language,
        },
    )
