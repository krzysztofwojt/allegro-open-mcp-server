# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Size tables
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
def get_table(
    *,
    tableId: Annotated[
        str, Field(json_schema_extra=input_schema("getTableUsingGET", "path:tableId", "tableId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTableUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a size table

    Use this resource to get selected size table. Read more: <a href="../../news/tabele-rozmiarow-w-rest-api-LRV05q2dGtV" target="_blank">PL</a> / <a href="../../news/size-tables-in-rest-api-D7KP4DE1BH3" target="_blank">EN</a>.


    HTTP: ``GET /sale/size-tables/{tableId}``
    """
    return call_operation(
        "getTableUsingGET", {"path:tableId": tableId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def modify_table(
    *,
    tableId: Annotated[
        str, Field(json_schema_extra=input_schema("modifyTableUsingPUT", "path:tableId", "tableId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modifyTableUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("modifyTableUsingPUT", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Update a size table

    Use this resource to update selected size table. Read more: <a href="../../news/tabele-rozmiarow-zmieniamy-istniejacy-zasob-i-dodajemy-nowe-zasoby-do-ich-obslugi-k1nyd21A4fP" target="_blank">PL</a> / <a href="../../news/size-tables-we-change-the-existing-resource-and-add-new-resources-to-handle-them-jn91bynlbC9" target="_blank">EN</a>.


    HTTP: ``PUT /sale/size-tables/{tableId}``
    """
    return call_operation(
        "modifyTableUsingPUT",
        {"path:tableId": tableId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_tables(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTablesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's size tables

    Use this resource to get all size tables assigned to a seller account. Read more: <a href="../../news/tabele-rozmiarow-w-rest-api-LRV05q2dGtV" target="_blank">PL</a> / <a href="../../news/size-tables-in-rest-api-D7KP4DE1BH3" target="_blank">EN</a>.


    HTTP: ``GET /sale/size-tables``
    """
    return call_operation("getTablesUsingGET", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_table(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createTableUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createTableUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create a size table

    Use this resource to create size table. Read more: <a href="../../news/tabele-rozmiarow-zmieniamy-istniejacy-zasob-i-dodajemy-nowe-zasoby-do-ich-obslugi-k1nyd21A4fP" target="_blank">PL</a> / <a href="../../news/size-tables-we-change-the-existing-resource-and-add-new-resources-to-handle-them-jn91bynlbC9" target="_blank">EN</a>.


    HTTP: ``POST /sale/size-tables``
    """
    return call_operation(
        "createTableUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_tables_templates(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTablesTemplatesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the size tables templates

    Use this resource to get all size tables templates. Read more: <a href="../../news/tabele-rozmiarow-zmieniamy-istniejacy-zasob-i-dodajemy-nowe-zasoby-do-ich-obslugi-k1nyd21A4fP" target="_blank">PL</a> / <a href="../../news/size-tables-we-change-the-existing-resource-and-add-new-resources-to-handle-them-jn91bynlbC9" target="_blank">EN</a>.


    HTTP: ``GET /sale/size-tables-templates``
    """
    return call_operation("getTablesTemplatesUsingGET", {"header:Accept-Language": Accept_Language})
