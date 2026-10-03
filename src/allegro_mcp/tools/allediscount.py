# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: AlleDiscount
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
def submit_offer_to_alle_discount_commands(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "submitOfferToAlleDiscountCommands", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("submitOfferToAlleDiscountCommands", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create submit offer command

    Use this resource to create a command for submitting an offer. Offer will be submitted to the AlleDiscount campaign only if command is processed successfully. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-zglosic-oferte-do-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-submit-an-offer-to-a-campaign" target="_blank">EN</a>.


    HTTP: ``POST /sale/alle-discount/submit-offer-commands``
    """
    return call_operation(
        "submitOfferToAlleDiscountCommands",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_submit_offer_to_alle_discount_commands_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getSubmitOfferToAlleDiscountCommandsStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSubmitOfferToAlleDiscountCommandsStatus",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the offer submission command status

    Use this resource to get information about the submit offer command execution status. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-sprawdzic-status-zgloszenia-oferty-do-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-check-the-status-of-an-offer-submission-to-a-campaign" target="_blank">EN</a>.


    HTTP: ``GET /sale/alle-discount/submit-offer-commands/{commandId}``
    """
    return call_operation(
        "getSubmitOfferToAlleDiscountCommandsStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def withdraw_offer_from_alle_discount_commands(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "withdrawOfferFromAlleDiscountCommands", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema("withdrawOfferFromAlleDiscountCommands", "body", "body")
        ),
    ],
) -> Any | ErrorResponse:
    """Create withdraw offer command

    Use this resource to create a command for withdrawing an offer from specific campaign. Offer will be withdrawn from the AlleDiscount campaign only if command is processed successfully. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-wycofac-oferte-z-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-withdraw-an-offer-from-a-campaign" target="_blank">EN</a>.


    HTTP: ``POST /sale/alle-discount/withdraw-offer-commands``
    """
    return call_operation(
        "withdrawOfferFromAlleDiscountCommands",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_withdraw_offer_from_alle_discount_commands_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getWithdrawOfferFromAlleDiscountCommandsStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getWithdrawOfferFromAlleDiscountCommandsStatus",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the offer withdrawal command status

    Use this resource to get information about the withdrawal command execution status. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#jak-sprawdzic-status-wycofania-oferty-z-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#how-to-check-the-withdrawal-status-of-an-offer-from-a-campaign" target="_blank">EN</a>.


    HTTP: ``GET /sale/alle-discount/withdraw-offer-commands/{commandId}``
    """
    return call_operation(
        "getWithdrawOfferFromAlleDiscountCommandsStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_offers_eligible_for_alle_discount(
    *,
    campaignId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "path:campaignId", "campaignId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "query:offset", "offset"
            )
        ),
    ] = None,
    meetsConditions: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "query:meetsConditions", "meetsConditions"
            )
        ),
    ] = None,
    offerId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "query:offerId", "offerId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersEligibleForAlleDiscount", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List eligible offers

    Endpoint returning info about offers that can be submitted to a given AlleDiscount campaign. Only offer linked to the product in published list of goods (products) can be submitted to a given AlleDiscount campaign. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#lista-ofert-kwalifikujacych-sie-do-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#list-of-offers-eligible-for-the-selected-campaign" target="_blank">EN</a>.


    HTTP: ``GET /sale/alle-discount/{campaignId}/eligible-offers``
    """
    return call_operation(
        "getOffersEligibleForAlleDiscount",
        {
            "path:campaignId": campaignId,
            "query:limit": limit,
            "query:offset": offset,
            "query:meetsConditions": meetsConditions,
            "query:offerId": offerId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_offers_submitted_to_alle_discount(
    *,
    campaignId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "path:campaignId", "campaignId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "query:offset", "offset"
            )
        ),
    ] = None,
    offerId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "query:offerId", "offerId"
            )
        ),
    ] = None,
    participationId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "query:participationId", "participationId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersSubmittedToAlleDiscount", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List offer participations

    Endpoint returning info about offer participations for a given AlleDiscount campaign. With this endpoint you are able to validate if the offer participates in AlleDiscount and if it has lowered price on the platform. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#lista-ofert-zgloszonych-do-wybranej-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#list-of-offers-submitted-for-the-selected-campaign" target="_blank">EN</a>.


    HTTP: ``GET /sale/alle-discount/{campaignId}/submitted-offers``
    """
    return call_operation(
        "getOffersSubmittedToAlleDiscount",
        {
            "path:campaignId": campaignId,
            "query:limit": limit,
            "query:offset": offset,
            "query:offerId": offerId,
            "query:participationId": participationId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_alle_discount_campaigns(
    *,
    campaignId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAlleDiscountCampaigns", "query:campaignId", "campaignId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAlleDiscountCampaigns", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List AlleDiscount campaigns

    List current AlleDiscount campaigns. Each campaign has its own list of goods (products) that indicate which offers can be submitted to it. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#lista-dostepnych-kampanii-alleobnizka" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#list-of-available-allediscount-campaigns" target="_blank">EN</a>.


    HTTP: ``GET /sale/alle-discount/campaigns``
    """
    return call_operation(
        "getAlleDiscountCampaigns",
        {"query:campaignId": campaignId, "header:Accept-Language": Accept_Language},
    )
