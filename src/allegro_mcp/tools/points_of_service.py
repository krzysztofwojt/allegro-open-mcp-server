# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Points of service
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
def create_pos(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createPOSUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("createPOSUsingPOST", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Create a point of service

    Use this resource to create a point of service. Read more: <a href="../../news/punkty-odbioru-osobistego-8dmlj8qk7ik" target="_blank">PL</a> / <a href="../../news/points-of-service-Rdoz09ZE7sW" target="_blank">EN</a>.


    HTTP: ``POST /points-of-service``
    """
    return call_operation(
        "createPOSUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_pos_list(
    *,
    seller_id: Annotated[
        str,
        Field(json_schema_extra=input_schema("getPOSListUsingGET", "query:seller.id", "seller_id")),
    ],
    countryCode: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getPOSListUsingGET", "query:countryCode", "countryCode")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPOSListUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's points of service

    Use this resource to get a list of points of service by seller ID. Read more: <a href="../../news/punkty-odbioru-osobistego-8dmlj8qk7ik" target="_blank">PL</a> / <a href="../../news/points-of-service-Rdoz09ZE7sW" target="_blank">EN</a>.


    HTTP: ``GET /points-of-service``
    """
    return call_operation(
        "getPOSListUsingGET",
        {
            "query:seller.id": seller_id,
            "query:countryCode": countryCode,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_pos_data(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getPOSDataUsingGET", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPOSDataUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the details of a point of service

    Use this resource to get a details of a point of service for a given ID. Read more: <a href="../../news/punkty-odbioru-osobistego-8dmlj8qk7ik" target="_blank">PL</a> / <a href="../../news/points-of-service-Rdoz09ZE7sW" target="_blank">EN</a>.


    HTTP: ``GET /points-of-service/{id}``
    """
    return call_operation(
        "getPOSDataUsingGET", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def modify_pos(
    *,
    id: Annotated[str, Field(json_schema_extra=input_schema("modifyPOSUsingPUT", "path:id", "id"))],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modifyPOSUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("modifyPOSUsingPUT", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Modify a point of service

    Use this resource to modify a point of service. Read more: <a href="../../news/punkty-odbioru-osobistego-8dmlj8qk7ik" target="_blank">PL</a> / <a href="../../news/points-of-service-Rdoz09ZE7sW" target="_blank">EN</a>.


    HTTP: ``PUT /points-of-service/{id}``
    """
    return call_operation(
        "modifyPOSUsingPUT",
        {"path:id": id, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_pos(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("deletePOSUsingDELETE", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deletePOSUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete a point of service

    Use this resource to delete a point of service. Read more: <a href="../../news/punkty-odbioru-osobistego-8dmlj8qk7ik" target="_blank">PL</a> / <a href="../../news/points-of-service-Rdoz09ZE7sW" target="_blank">EN</a>.


    HTTP: ``DELETE /points-of-service/{id}``
    """
    return call_operation(
        "deletePOSUsingDELETE", {"path:id": id, "header:Accept-Language": Accept_Language}
    )
