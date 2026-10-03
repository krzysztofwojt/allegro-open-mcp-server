# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Badge campaigns
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
def badge_campaigns_get_all(
    *,
    marketplace_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeCampaigns_get_all", "query:marketplace.id", "marketplace_id"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeCampaigns_get_all", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of available badge campaigns

    Badge campaigns are another way to promote your offers. You can apply for a badge, which - depending on a type - will be displayed on your offer page of on the list of offers. First - use this resource to get a list of all available badge campaigns at the moment, then use *POST /sale/badges* to apply for badge. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#lista-dostepnych-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#list-of-available-campaigns" target="_blank">EN</a>.


    HTTP: ``GET /sale/badge-campaigns``
    """
    return call_operation(
        "badgeCampaigns_get_all",
        {"query:marketplace.id": marketplace_id, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def post_badges(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "postBadges", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None, Field(json_schema_extra=input_schema("postBadges", "body", "body"))
    ] = None,
) -> Any | ErrorResponse:
    """Apply for badge in selected offer

    This resource allows you to apply for a badge. Most badges involve additional fee charged. Your badge application will be verified and you will be notified about the verification status via e-mail. You can use *Location* provided in header of the response to track your application status. Application will be removed after 30 days when status of the application was changed form PROCESSED or DECLINED. Fees will be charged in accordance with Annex No. 1 to the <a href="https://allegro.pl/regulaminy/regulamin-strefy-okazji-9dGVAPB69In" target="_blank">Daily deals zone terms and conditions</a>. By using this resource you agree to the <a href="https://allegro.pl/regulaminy/regulamin-strefy-okazji-9dGVAPB69In" target="_blank">Daily deals zone terms and conditions</a> or <a href="https://allegro.pl/regulaminy/regulamin-programu-bonusowego-prowizja-nawet-0-5-0KPkAE7wkcv" target="_blank">Commission discount terms and conditions</a>. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#zglos-oferte-do-kampanii" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#submit-offer-to-a-campaign" target="_blank">EN</a>.


    HTTP: ``POST /sale/badges``
    """
    return call_operation("postBadges", {"header:Accept-Language": Accept_Language, "body": body})


@mcp.tool
@allegro_call
def get_badges(
    *,
    offer_id: Annotated[
        str | None, Field(json_schema_extra=input_schema("getBadges", "query:offer.id", "offer_id"))
    ] = None,
    marketplace_id: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getBadges", "query:marketplace.id", "marketplace_id")
        ),
    ],
    offset: Annotated[
        int | None, Field(json_schema_extra=input_schema("getBadges", "query:offset", "offset"))
    ] = None,
    limit: Annotated[
        int | None, Field(json_schema_extra=input_schema("getBadges", "query:limit", "limit"))
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getBadges", "header:Accept-Language", "Accept_Language")
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of badges

    Use this resource to get a list of badges in authorized seller's offers. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#kampanie-przypisane-do-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#check-badges-assigned-to-offers" target="_blank">EN</a>.


    HTTP: ``GET /sale/badges``
    """
    return call_operation(
        "getBadges",
        {
            "query:offer.id": offer_id,
            "query:marketplace.id": marketplace_id,
            "query:offset": offset,
            "query:limit": limit,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def badge_applications_get_one(
    *,
    applicationId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "badgeApplications_get_one", "path:applicationId", "applicationId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeApplications_get_one", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a badge application details

    Use this resource to get a badge application details. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#pobierz-dane-zgloszenie" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#retrieve-campaign-application" target="_blank">EN</a>.


    HTTP: ``GET /sale/badge-applications/{applicationId}``
    """
    return call_operation(
        "badgeApplications_get_one",
        {"path:applicationId": applicationId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def badge_applications_get_all(
    *,
    campaign_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeApplications_get_all", "query:campaign.id", "campaign_id"
            )
        ),
    ] = None,
    offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeApplications_get_all", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("badgeApplications_get_all", "query:offset", "offset")
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("badgeApplications_get_all", "query:limit", "limit")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeApplications_get_all", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of badge applications

    Use this resource to get a list of badge applications. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#pobierz-swoje-zgloszenia" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#retrieve-all-campaign-applications" target="_blank">EN</a>.


    HTTP: ``GET /sale/badge-applications``
    """
    return call_operation(
        "badgeApplications_get_all",
        {
            "query:campaign.id": campaign_id,
            "query:offer.id": offer_id,
            "query:offset": offset,
            "query:limit": limit,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def badge_operations_get_one(
    *,
    operationId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "badgeOperations_get_one", "path:operationId", "operationId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "badgeOperations_get_one", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get badge operation details

    Use this resource to get badge operation details. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#zmiana-ceny-i-zakonczenie-oznaczenia" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#change-price-and-finish-badge" target="_blank">EN</a>.


    HTTP: ``GET /sale/badge-operations/{operationId}``
    """
    return call_operation(
        "badgeOperations_get_one",
        {"path:operationId": operationId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def patch_badge(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("patchBadge", "path:offerId", "offerId"))
    ],
    campaignId: Annotated[
        str, Field(json_schema_extra=input_schema("patchBadge", "path:campaignId", "campaignId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "patchBadge", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None, Field(json_schema_extra=input_schema("patchBadge", "body", "body"))
    ] = None,
) -> Any | ErrorResponse:
    """Update campaign badge for the given offer

    This resource allows you to update a campaign badge for the given offer. You can use *Location* provided in header of the response to track your update status. Update offer price in a campaign or finish marking an offer in a campaign. Read more: <a href="../../tutorials/jak-przypisac-oferte-kampanii-GRaj0q6Gwuy#zmiana-ceny-i-zakonczenie-oznaczenia" target="_blank">PL</a> / <a href="../../tutorials/how-to-submit-offers-to-campaigns-AgGjd6EmyH4#change-price-and-finish-badge" target="_blank">EN</a>.


    HTTP: ``PATCH /sale/badges/offers/{offerId}/campaigns/{campaignId}``
    """
    return call_operation(
        "patchBadge",
        {
            "path:offerId": offerId,
            "path:campaignId": campaignId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )
