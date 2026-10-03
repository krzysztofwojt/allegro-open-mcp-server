# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Responsible persons
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
def responsible_persons_get(
    *,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("responsiblePersonsGET", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("responsiblePersonsGET", "query:limit", "limit")),
    ] = None,
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsiblePersonsGET", "header:Accept", "Accept")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsiblePersonsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the list of responsible persons

    Use this resource to get a list of responsible persons for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#osoba-odpowiedzialna-za-zgodnosc-produktu-z-przepisami-unijnymi" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-persons-for-the-compliance-of-the-product-with-eu-regulations" target="_blank">EN</a>.


    HTTP: ``GET /sale/responsible-persons``
    """
    return call_operation(
        "responsiblePersonsGET",
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
def responsible_persons_post(
    *,
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsiblePersonsPOST", "header:Accept", "Accept")),
    ],
    Content_Type: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "responsiblePersonsPOST", "header:Content-Type", "Content_Type"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsiblePersonsPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("responsiblePersonsPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create responsible person

    Use this resource to create a new responsible person for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#osoba-odpowiedzialna-za-zgodnosc-produktu-z-przepisami-unijnymi" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-persons-for-the-compliance-of-the-product-with-eu-regulations" target="_blank">EN</a>.


    HTTP: ``POST /sale/responsible-persons``
    """
    return call_operation(
        "responsiblePersonsPOST",
        {
            "header:Accept": Accept,
            "header:Content-Type": Content_Type,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def responsible_persons_put(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("responsiblePersonsPUT", "path:id", "id"))
    ],
    Accept: Annotated[
        str,
        Field(json_schema_extra=input_schema("responsiblePersonsPUT", "header:Accept", "Accept")),
    ],
    Content_Type: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "responsiblePersonsPUT", "header:Content-Type", "Content_Type"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "responsiblePersonsPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("responsiblePersonsPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update responsible person

    Use this resource to update the responsible person for the compliance of the product with EU regulations. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#osoba-odpowiedzialna-za-zgodnosc-produktu-z-przepisami-unijnymi" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#responsible-persons-for-the-compliance-of-the-product-with-eu-regulations" target="_blank">EN</a>.


    HTTP: ``PUT /sale/responsible-persons/{id}``
    """
    return call_operation(
        "responsiblePersonsPUT",
        {
            "path:id": id,
            "header:Accept": Accept,
            "header:Content-Type": Content_Type,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )
