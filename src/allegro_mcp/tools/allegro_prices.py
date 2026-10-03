# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Allegro Prices
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
def get_account_participation(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAccountParticipation", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get account participation status

    Use this resource to retrieve the account participation status for all supported marketplaces in the Allegro Prices program. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-pobrac-aktualny-status-uczestnictwa-w-programie" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-retrieve-the-current-program-participation-status" target="_blank">EN</a>.


    HTTP: ``GET /sale/allegro-prices/accounts/participations``
    """
    return call_operation("getAccountParticipation", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_account_participation(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAccountParticipation", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateAccountParticipation", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update account participation

    Use this resource to update the account participation status for one or more marketplaces in the Allegro Prices program. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zmienic-status-uczestnictwa-w-programie" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-change-the-program-participation-status" target="_blank">EN</a>.


    HTTP: ``PATCH /sale/allegro-prices/accounts/participations``
    """
    return call_operation(
        "updateAccountParticipation", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def submit_offer_commands(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "submitOfferCommands", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("submitOfferCommands", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Submit offers command

    Use this resource to submit a command to add offers to the Allegro Prices program. Returns a command ID that can be used to track the processing status. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zlecic-dodanie-ofert-do-programu" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-submit-a-command-to-add-offers-to-the-program" target="_blank">EN</a>.


    HTTP: ``POST /sale/allegro-prices/offers/submit-offer-commands``
    """
    return call_operation(
        "submitOfferCommands", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_submit_offer_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getSubmitOfferCommandStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSubmitOfferCommandStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get submit offer command status

    Use this resource to retrieve the status and details of a previously submitted offer command. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zlecic-dodanie-ofert-do-programu" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-submit-a-command-to-add-offers-to-the-program" target="_blank">EN</a>.


    HTTP: ``GET /sale/allegro-prices/offers/submit-offer-commands/{commandId}``
    """
    return call_operation(
        "getSubmitOfferCommandStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def exclude_offer_commands(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "excludeOfferCommands", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("excludeOfferCommands", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Exclude offers command

    Use this resource to submit a command to exclude offers from the Allegro Prices program. Returns a command ID that can be used to track the processing status. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zlecic-wykluczenie-ofert-z-programu" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-submit-a-command-to-exclude-offers-from-the-program" target="_blank">EN</a>.


    HTTP: ``POST /sale/allegro-prices/offers/exclusion-commands``
    """
    return call_operation(
        "excludeOfferCommands", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_exclude_offer_command_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getExcludeOfferCommandStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getExcludeOfferCommandStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get exclude offer command status

    Use this resource to retrieve the status and details of a previously submitted exclusion command. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zlecic-wykluczenie-ofert-z-programu" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-submit-a-command-to-exclude-offers-from-the-program" target="_blank">EN</a>.


    HTTP: ``GET /sale/allegro-prices/offers/exclusion-commands/{commandId}``
    """
    return call_operation(
        "getExcludeOfferCommandStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def get_allegro_prices_offers(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAllegroPricesOffers", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("getAllegroPricesOffers", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Query Allegro Prices offers status

    Use this resource to retrieve a list of offers and their status in the Allegro Prices program with optional filtering and pagination. Allows filtering by offer IDs, marketplace, and scope (WITH_DECLARATION, DISCOUNTED, or EXCLUDED). Only offers in ACTIVATING, ACTIVE, or ENDED statuses are considered. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-pobrac-liste-ofert-i-ich-obecny-status-w-programie" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-retrieve-a-list-of-offers-and-their-status-in-the-program" target="_blank">EN</a>.


    HTTP: ``POST /sale/allegro-prices/offers-queries``
    """
    return call_operation(
        "getAllegroPricesOffers", {"header:Accept-Language": Accept_Language, "body": body}
    )
