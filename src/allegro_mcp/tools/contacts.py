# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Contacts
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
def create_contact(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createContactUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createContactUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create a new contact

    Use this resource to create a new contact. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-utworzyc-nowy-kontakt" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-create-new-contact" target="_blank">EN</a>.


    HTTP: ``POST /sale/offer-contacts``
    """
    return call_operation(
        "createContactUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_list_of_contacts(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfContactsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's contacts

    Use this resource to get details of many contacts. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-liste-kontaktow" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-a-list-of-contacts" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-contacts``
    """
    return call_operation("getListOfContactsUsingGET", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
def get_contact(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getContactUsingGET", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getContactUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get contact details

    Use this resource to get contact details. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-szczegoly-danego-kontaktu" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-contact-details" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-contacts/{id}``
    """
    return call_operation(
        "getContactUsingGET", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def modify_contact(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("modifyContactUsingPUT", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modifyContactUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("modifyContactUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Modify contact details

    Use this resource to modify contact details. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-zmienic-dane-kontaktu" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-change-contact-data" target="_blank">EN</a>.


    HTTP: ``PUT /sale/offer-contacts/{id}``
    """
    return call_operation(
        "modifyContactUsingPUT",
        {"path:id": id, "header:Accept-Language": Accept_Language, "body": body},
    )
