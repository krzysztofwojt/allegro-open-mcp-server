# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Classifieds
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
def classified_seller_offer_stats_get(
    *,
    date_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "classifiedSellerOfferStatsGET", "query:date.gte", "date_gte"
            )
        ),
    ] = None,
    date_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "classifiedSellerOfferStatsGET", "query:date.lte", "date_lte"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "classifiedSellerOfferStatsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the seller's advertisements daily statistics

    This endpoint returns daily statistics collected for a list of advertisements in a given date range for logged user. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#statystyki-wszystkich-ogloszen-sprzedawcy" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#statistics-of-seller-s-classified-ads" target="_blank">EN</a>.


    HTTP: ``GET /sale/classified-seller-stats``
    """
    return call_operation(
        "classifiedSellerOfferStatsGET",
        {
            "query:date.gte": date_gte,
            "query:date.lte": date_lte,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def classified_offers_stats_get(
    *,
    offer_id: Annotated[
        list[str],
        Field(
            json_schema_extra=input_schema("classifiedOffersStatsGET", "query:offer.id", "offer_id")
        ),
    ],
    date_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("classifiedOffersStatsGET", "query:date.gte", "date_gte")
        ),
    ] = None,
    date_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("classifiedOffersStatsGET", "query:date.lte", "date_lte")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "classifiedOffersStatsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the advertisements daily statistics

    This endpoint returns daily statistics collected for a list of advertisements in a given date range. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#statystyki-wybranych-ogloszen" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#statistics-of-selected-classified-ads" target="_blank">EN</a>.


    HTTP: ``GET /sale/classified-offers-stats``
    """
    return call_operation(
        "classifiedOffersStatsGET",
        {
            "query:offer.id": offer_id,
            "query:date.gte": date_gte,
            "query:date.lte": date_lte,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_classified_packages(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackagesUsingGET", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackagesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get classified packages assigned to an offer

    Use this resource to retrieve classified packages currently assigned to an offer. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#dodatkowe-opcje-promowania" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#additional-promo-options" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-classifieds-packages/{offerId}``
    """
    return call_operation(
        "getClassifiedPackagesUsingGET",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def assign_classified_packages(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "assignClassifiedPackagesUsingPUT", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "assignClassifiedPackagesUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("assignClassifiedPackagesUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Assign packages to a classified

    Use this resource to assign classified packages to an offer. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#dodatkowe-opcje-promowania" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#additional-promo-options" target="_blank">EN</a>.


    HTTP: ``PUT /sale/offer-classifieds-packages/{offerId}``
    """
    return call_operation(
        "assignClassifiedPackagesUsingPUT",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_classified_package_configurations_for_category(
    *,
    category_id: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackageConfigurationsForCategoryUsingGET",
                "query:category.id",
                "category_id",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackageConfigurationsForCategoryUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get configurations of packages

    Use this resource to retrieve configurations of classifieds packages for a category. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#lista-pakietow-i-opcji-dodatkowych" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#list-of-promo-options" target="_blank">EN</a>.


    HTTP: ``GET /sale/classifieds-packages``
    """
    return call_operation(
        "getClassifiedPackageConfigurationsForCategoryUsingGET",
        {"query:category.id": category_id, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_classified_package_configuration(
    *,
    packageId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackageConfigurationUsingGET", "path:packageId", "packageId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getClassifiedPackageConfigurationUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the configuration of a package

    Use this resource to retrieve the configuration of a classifieds package. Read more: <a href="../../tutorials/jak-wystawic-i-zarzadzac-ogloszeniem-K6r3Z47dKcy#lista-pakietow-i-opcji-dodatkowych" target="_blank">PL</a> / <a href="../../tutorials/listing-and-managing-classified-ads-5Ln0r6wkWs7#list-of-promo-options" target="_blank">EN</a>.


    HTTP: ``GET /sale/classifieds-packages/{packageId}``
    """
    return call_operation(
        "getClassifiedPackageConfigurationUsingGET",
        {"path:packageId": packageId, "header:Accept-Language": Accept_Language},
    )
