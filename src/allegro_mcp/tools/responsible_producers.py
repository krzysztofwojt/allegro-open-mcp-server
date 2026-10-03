# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Responsible producers
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
def responsible_producers_get(
    *,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("responsibleProducersGET", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("responsibleProducersGET", "query:limit", "limit")),
    ] = None,
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsibleProducersGET", "header:Accept", "Accept")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducersGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the list of responsible producers

    Use this resource to get a list of responsible producers for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#dane-teleadresowe-producenta" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-producers-contact-information" target="_blank">EN</a>.


    HTTP: ``GET /sale/responsible-producers``
    """
    return call_operation(
        "responsibleProducersGET",
        {
            "query:offset": offset,
            "query:limit": limit,
            "header:Accept": Accept,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def responsible_producers_post(
    *,
    Accept: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("responsibleProducersPOST", "header:Accept", "Accept")
        ),
    ],
    Content_Type: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducersPOST", "header:Content-Type", "Content_Type"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducersPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("responsibleProducersPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create responsible producer

    Use this resource to create a new responsible producer for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#dane-teleadresowe-producenta" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-producers-contact-information" target="_blank">EN</a>.


    HTTP: ``POST /sale/responsible-producers``
    """
    return call_operation(
        "responsibleProducersPOST",
        {
            "header:Accept": Accept,
            "header:Content-Type": Content_Type,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
def responsible_producer_get(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("responsibleProducerGET", "path:id", "id"))
    ],
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsibleProducerGET", "header:Accept", "Accept")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducerGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get responsible producer

    Use this resource to get a responsible producer for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#dane-teleadresowe-producenta" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-producers-contact-information" target="_blank">EN</a>.


    HTTP: ``GET /sale/responsible-producers/{id}``
    """
    return call_operation(
        "responsibleProducerGET",
        {"path:id": id, "header:Accept": Accept, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def responsible_producers_put(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("responsibleProducersPUT", "path:id", "id"))
    ],
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsibleProducersPUT", "header:Accept", "Accept")),
    ],
    Content_Type: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducersPUT", "header:Content-Type", "Content_Type"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsibleProducersPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("responsibleProducersPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update responsible producer

    Use this resource to update the responsible producer for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#dane-teleadresowe-producenta" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-producers-contact-information" target="_blank">EN</a>.


    HTTP: ``PUT /sale/responsible-producers/{id}``
    """
    return call_operation(
        "responsibleProducersPUT",
        {
            "path:id": id,
            "header:Accept": Accept,
            "header:Content-Type": Content_Type,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )
