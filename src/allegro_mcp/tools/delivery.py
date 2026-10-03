# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Delivery
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
def get_list_of_shipping_ratest(
    *,
    marketplace: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfShippingRatestUsingGET", "query:marketplace", "marketplace"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfShippingRatestUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's shipping rates

    Use this resource to get a list of seller's shipping rates. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-cennik-dostaw" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-shipping-rates" target="_blank">EN</a>.


    HTTP: ``GET /sale/shipping-rates``
    """
    return call_operation(
        "getListOfShippingRatestUsingGET",
        {"query:marketplace": marketplace, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_shipping_rates_set(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createShippingRatesSetUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createShippingRatesSetUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create a new shipping rates set

    Use this resource to create a new seller's shipping rates set. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-dodac-cennik-dostaw" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-add-shipping-rates" target="_blank">EN</a>.


    HTTP: ``POST /sale/shipping-rates``
    """
    return call_operation(
        "createShippingRatesSetUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_shipping_rates_set(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getShippingRatesSetUsingGET", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShippingRatesSetUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the details of a shipping rates set

    Use this resource to get details of the given shipping rates set. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-cennik-dostaw" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-shipping-rates" target="_blank">EN</a>.


    HTTP: ``GET /sale/shipping-rates/{id}``
    """
    return call_operation(
        "getShippingRatesSetUsingGET", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def modify_shipping_rates_set(
    *,
    id: Annotated[
        str,
        Field(json_schema_extra=input_schema("modifyShippingRatesSetUsingPUT", "path:id", "id")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modifyShippingRatesSetUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("modifyShippingRatesSetUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Edit a user's shipping rates set

    Use this resource to edit a new seller's shipping rates set. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-edytowac-cennik-dostaw" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-modify-shipping-rates" target="_blank">EN</a>.


    HTTP: ``PUT /sale/shipping-rates/{id}``
    """
    return call_operation(
        "modifyShippingRatesSetUsingPUT",
        {"path:id": id, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_sale_delivery_settings(
    *,
    marketplace_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleDeliverySettings", "query:marketplace.id", "marketplace_id"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleDeliverySettings", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's delivery settings

    Use this resource to get the delivery settings declared by the seller. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-ustawienia-dostawy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-get-delivery-settings" target="_blank">EN</a>.


    HTTP: ``GET /sale/delivery-settings``
    """
    return call_operation(
        "getSaleDeliverySettings",
        {"query:marketplace.id": marketplace_id, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def put_sale_delivery_settings(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "putSaleDeliverySettings", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("putSaleDeliverySettings", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Modify the user's delivery settings

    Use this resource to modify the delivery settings declared by the seller. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-edytowac-ustawienia-dostawy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-edit-delivery-settings" target="_blank">EN</a>.


    HTTP: ``PUT /sale/delivery-settings``
    """
    return call_operation(
        "putSaleDeliverySettings", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_list_of_delivery_methods(
    *,
    marketplace: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfDeliveryMethodsUsingGET", "query:marketplace", "marketplace"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfDeliveryMethodsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the list of delivery methods

    Use this resource to get a list of all delivery methods currently available on the platform, as well as those that have already been discontinued. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-dodac-cennik-dostaw" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-add-shipping-rates" target="_blank">EN</a>.


    HTTP: ``GET /sale/delivery-methods``
    """
    return call_operation(
        "getListOfDeliveryMethodsUsingGET",
        {"query:marketplace": marketplace, "header:Accept-Language": Accept_Language},
    )
