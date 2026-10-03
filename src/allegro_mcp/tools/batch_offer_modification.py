# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Batch offer modification
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
def modification_command(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "modificationCommandUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modificationCommandUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("modificationCommandUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Batch offer modification

    Use this resource to modify multiple offers at once. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#edycja-wielu-ofert-jednoczesnie" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#editing-many-offers" target="_blank">EN</a>. This resource is rate limited to 250 000 offer changes per hour or 9000 offer changes per minute - limit applies to a single user of the application.


    HTTP: ``PUT /sale/offer-modification-commands/{commandId}``
    """
    return call_operation(
        "modificationCommandUsingPUT",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_general_report(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getGeneralReportUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getGeneralReportUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Modification command summary

    Use this resource to find out how many offers were edited within one {commandId}. You will receive a summary with a number of successfully edited offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#edycja-wielu-ofert-jednoczesnie" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#editing-many-offers" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-modification-commands/{commandId}``
    """
    return call_operation(
        "getGeneralReportUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_tasks(
    *,
    commandId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getTasksUsingGET", "path:commandId", "commandId")),
    ],
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getTasksUsingGET", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getTasksUsingGET", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTasksUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Modification command detailed report

    Use this resource to retrieve a detailed summary of changes introduced within one {commandId} (defaults: limit = 100, offset = 0). Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#edycja-wielu-ofert-jednoczesnie" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#editing-many-offers" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-modification-commands/{commandId}/tasks``
    """
    return call_operation(
        "getTasksUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def price_modification_command(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "priceModificationCommandUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "priceModificationCommandUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("priceModificationCommandUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Batch offer price modification

    Change price of offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price" target="_blank">EN</a>. This resource is rate limited to 150 000 offer changes per hour or 9000 offer changes per minute - limit applies to a single user of the application.


    HTTP: ``PUT /sale/offer-price-change-commands/{commandId}``
    """
    return call_operation(
        "priceModificationCommandUsingPUT",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_price_modification_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandStatusUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandStatusUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Change price command summary

    Returns status and summary of particular command execution. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-price-change-commands/{commandId}``
    """
    return call_operation(
        "getPriceModificationCommandStatusUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_price_modification_command_tasks_statuses(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandTasksStatusesUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandTasksStatusesUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandTasksStatusesUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPriceModificationCommandTasksStatusesUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Change price command detailed report

    Defaults: limit = 100, offset = 0. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-price-change-commands/{commandId}/tasks``
    """
    return call_operation(
        "getPriceModificationCommandTasksStatusesUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def batch_offer_modification(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("batchOfferModificationUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Batch offer price and stock modification (beta)

    Bulk price and stock modification. Contrary to standard batch price or stock modification, it lets you modify both price and stock modification across multiple offers, or within the same offer but in a separate modification unit. <br> Change price and stock of offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena-i-liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price-and-stock" target="_blank">EN</a>. <br> This resource is rate limited to 150 000 offer changes per hour or 9000 offer changes per minute - limit applies to a single user of the application.


    HTTP: ``POST /sale/offer-bulk-modification-commands``
    """
    return call_operation(
        "batchOfferModificationUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def batch_offer_modification_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandStatusUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandStatusUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Batch price and stock command summary (beta)

    Returns status and summary of particular command execution. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena-i-liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price-and-stock" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-bulk-modification-commands/{commandId}``
    """
    return call_operation(
        "batchOfferModificationCommandStatusUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def batch_offer_modification_command_task_statuses(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandTaskStatusesUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandTaskStatusesUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandTaskStatusesUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "batchOfferModificationCommandTaskStatusesUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Batch price and stock command detailed report (beta)

    Defaults: limit = 100, offset = 0. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#cena-i-liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#price-and-stock" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-bulk-modification-commands/{commandId}/tasks``
    """
    return call_operation(
        "batchOfferModificationCommandTaskStatusesUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def quantity_modification_command(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "quantityModificationCommandUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "quantityModificationCommandUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema("quantityModificationCommandUsingPUT", "body", "body")
        ),
    ],
) -> Any | ErrorResponse:
    """Batch offer quantity modification

    Change quantity of multiple offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#quantity" target="_blank">EN</a>. This resource is rate limited to 250 000 offer changes per hour or 9000 offer changes per minute - limit applies to a single user of the application.


    HTTP: ``PUT /sale/offer-quantity-change-commands/{commandId}``
    """
    return call_operation(
        "quantityModificationCommandUsingPUT",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_quantity_modification_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandStatusUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandStatusUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Change quantity command summary

    Returns status and summary of the command. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#quantity" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-quantity-change-commands/{commandId}``
    """
    return call_operation(
        "getQuantityModificationCommandStatusUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_quantity_modification_command_tasks_statuses(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandTasksStatusesUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandTasksStatusesUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandTasksStatusesUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getQuantityModificationCommandTasksStatusesUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Change quantity command detailed report

    Defaults: limit = 100, offset = 0. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#liczba-przedmiotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#quantity" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-quantity-change-commands/{commandId}/tasks``
    """
    return call_operation(
        "getQuantityModificationCommandTasksStatusesUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def offer_automatic_pricing_modification_command(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "offerAutomaticPricingModificationCommandUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "offerAutomaticPricingModificationCommandUsingPOST", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Batch offer automatic pricing rules modification

    Use this resource to modify the automatic pricing rules of multiple offers at the same time. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#pricing-rules" target="_blank">EN</a>. This resource is rate limited to 150 000 offer changes per hour or 9000 offer changes per minute - limit applies to a single user of the application.


    HTTP: ``POST /sale/offer-price-automation-commands``
    """
    return call_operation(
        "offerAutomaticPricingModificationCommandUsingPOST",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def getoffer_automatic_pricing_modification_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandStatusUsingGET",
                "path:commandId",
                "commandId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandStatusUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Automatic pricing command summary

    Returns status and summary of the offer-price-automation-command. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#pricing-rules" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-price-automation-commands/{commandId}``
    """
    return call_operation(
        "getofferAutomaticPricingModificationCommandStatusUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def getoffer_automatic_pricing_modification_command_tasks_statuses(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandTasksStatusesUsingGET",
                "path:commandId",
                "commandId",
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandTasksStatusesUsingGET",
                "query:limit",
                "limit",
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandTasksStatusesUsingGET",
                "query:offset",
                "offset",
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getofferAutomaticPricingModificationCommandTasksStatusesUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Automatic pricing command detailed report

    Defaults: limit = 100, offset = 0. Returns status and report of the offer-price-automation-command. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#pricing-rules" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-price-automation-commands/{commandId}/tasks``
    """
    return call_operation(
        "getofferAutomaticPricingModificationCommandTasksStatusesUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )
