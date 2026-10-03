# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Offer management
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
def create_product_offers(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createProductOffers", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("createProductOffers", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Create offer based on product

    Use this resource to create offer based on product. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-utworzyc-oferte-powiazana-z-produktem" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-list-product-offer" target="_blank">EN</a>. Note that requests may be limited.


    HTTP: ``POST /sale/product-offers``
    """
    return call_operation(
        "createProductOffers", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def edit_product_offers(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("editProductOffers", "path:offerId", "offerId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "editProductOffers", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("editProductOffers", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Edit an offer

    Use this resource to edit offer. This resource allows you to edit each field independently, so use it if you want to change only, for example, the price or the quantity in an offer. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#edycja-pojedynczej-oferty" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#editing-single-offer" target="_blank">EN</a>. Note that requests may be limited.


    HTTP: ``PATCH /sale/product-offers/{offerId}``
    """
    return call_operation(
        "editProductOffers",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_product_offer_processing_status(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getProductOfferProcessingStatus", "path:offerId", "offerId"
            )
        ),
    ],
    operationId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getProductOfferProcessingStatus", "path:operationId", "operationId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getProductOfferProcessingStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Check the processing status of a POST or PATCH request

    The URI for the resource given by Location header of POST /sale/product-offers and PATCH /sale/product-offers/{offerId}. Use this resource to check processing status of a POST or PATCH request. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#procesowanie-oferty" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#offer-processing" target="_blank">EN</a>.


    HTTP: ``GET /sale/product-offers/{offerId}/operations/{operationId}``
    """
    return call_operation(
        "getProductOfferProcessingStatus",
        {
            "path:offerId": offerId,
            "path:operationId": operationId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_offer(
    *,
    offerId: Annotated[
        str,
        Field(json_schema_extra=input_schema("deleteOfferUsingDELETE", "path:offerId", "offerId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteOfferUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete a draft offer

    Use this resource to delete a draft offer. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#szkic-oferty" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#inactive-status" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/offers/{offerId}``
    """
    return call_operation(
        "deleteOfferUsingDELETE",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_change_price_command(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "createChangePriceCommandUsingPUT", "path:offerId", "offerId"
            )
        ),
    ],
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "createChangePriceCommandUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createChangePriceCommandUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createChangePriceCommandUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Modify the Buy Now price in an offer

    Use this resource to change the Buy Now price in a single offer. Read more: <a href="../../news/mozliwosc-zmiany-ceny-kup-teraz-2YzrKRrr3Sl" target="_blank">PL</a> / <a href="../../news/possibility-to-change-the-buy-it-now-price-q018mq8D2hW" target="_blank">EN</a>.


    HTTP: ``PUT /offers/{offerId}/change-price-commands/{commandId}``
    """
    return call_operation(
        "createChangePriceCommandUsingPUT",
        {
            "path:offerId": offerId,
            "path:commandId": commandId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def change_publication_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "changePublicationStatusUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "changePublicationStatusUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("changePublicationStatusUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Batch offer publish / unpublish

    Use this resource to modify multiple offers publication at once. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-zakonczyc-oferte" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#ending-offers" target="_blank">EN</a>. This resource is rate limited to 250 000 offer changes per hour or 9000 offer changes per minute.


    HTTP: ``PUT /sale/offer-publication-commands/{commandId}``
    """
    return call_operation(
        "changePublicationStatusUsingPUT",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_publication_report(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPublicationReportUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicationReportUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Publish command summary

    Use this resource to retrieve information about the offer listing statuses. You will receive a summary with a number of correctly listed offers and errors. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#zestawienie-zadan" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#task-list" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-publication-commands/{commandId}``
    """
    return call_operation(
        "getPublicationReportUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_publication_tasks(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPublicationTasksUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getPublicationTasksUsingGET", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getPublicationTasksUsingGET", "query:offset", "offset")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicationTasksUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Publish command detailed report

    Use this resource to retrieve information about the offer statuses on the site (Defaults: limit = 100, offset = 0). Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#asynchroniczne-procesowanie" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#asynchronous-processing" target="_blank">EN</a>. This resource is rate limited to retrieving information about 270 000 offer changes per minute.


    HTTP: ``GET /sale/offer-publication-commands/{commandId}/tasks``
    """
    return call_operation(
        "getPublicationTasksUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_available_offer_promotion_packages(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAvailableOfferPromotionPackages", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get all available offer promotion packages

    Use this resource to retrieve all available offer promotion packages. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-dostepne-opcje-promowania" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-available-promo-options" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-promotion-packages``
    """
    return call_operation(
        "getAvailableOfferPromotionPackages", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def modify_offer_promo_options(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "modifyOfferPromoOptionsUsingPOST", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "modifyOfferPromoOptionsUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("modifyOfferPromoOptionsUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Modify offer promotion packages

    Use this resource to modify offer promotion packages. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-lub-zmienic-opcje-promowania-w-pojedynczej-ofercie" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-or-change-promo-options-in-a-single-offer" target="_blank">EN</a>.


    HTTP: ``POST /sale/offers/{offerId}/promo-options-modification``
    """
    return call_operation(
        "modifyOfferPromoOptionsUsingPOST",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_offer_promo_options(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getOfferPromoOptionsUsingGET", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferPromoOptionsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get offer promotion packages

    Use this resource to get promotion packages assigned to an offer. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-opcje-promowania-przypisane-do-oferty" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-promo-options-assigned-to-an-offer" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/{offerId}/promo-options``
    """
    return call_operation(
        "getOfferPromoOptionsUsingGET",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_promo_options_for_seller_offers(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoOptionsForSellerOffersUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoOptionsForSellerOffersUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoOptionsForSellerOffersUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get promo options for seller's offers

    Use this resource to retrieve promo options for seller offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-opcje-promowania-dla-wielu-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-available-promo-options-for-multiple-offers" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/promo-options``
    """
    return call_operation(
        "getPromoOptionsForSellerOffersUsingGET",
        {"query:limit": limit, "query:offset": offset, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def promo_modification_command(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "promoModificationCommandUsingPUT", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "promoModificationCommandUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Batch offer promotion package modification

    Use this resource to modify promotion packages on multiple offers at once. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-lub-edytowac-opcje-promowania-na-wielu-ofertach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-or-change-promo-options-in-multiple-offers" target="_blank">EN</a>.


    HTTP: ``PUT /sale/offers/promo-options-commands/{commandId}``
    """
    return call_operation(
        "promoModificationCommandUsingPUT",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_promo_modification_command_result(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandResultUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandResultUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Modification command summary

    Use this resource to find out how many offers were edited within one {commandId}. You will receive a summary with a number of successfully edited offers and errors. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-sprawdzic-szczegolowy-raport-zadania" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-check-a-detailed-report-of-your-task" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/promo-options-commands/{commandId}``
    """
    return call_operation(
        "getPromoModificationCommandResultUsingGET",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_promo_modification_command_detailed_result(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandDetailedResultUsingGET", "path:commandId", "commandId"
            )
        ),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandDetailedResultUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandDetailedResultUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPromoModificationCommandDetailedResultUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Modification command detailed result

    Use this resource to retrieve the result of an offer modification command. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-sprawdzic-szczegolowy-raport-zadania" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-check-a-detailed-report-of-your-task" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/promo-options-commands/{commandId}/tasks``
    """
    return call_operation(
        "getPromoModificationCommandDetailedResultUsingGET",
        {
            "path:commandId": commandId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_offers_unfilled_parameters_using_get_1(
    *,
    offer_id: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersUnfilledParametersUsingGET_1", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    parameterType: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersUnfilledParametersUsingGET_1", "query:parameterType", "parameterType"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersUnfilledParametersUsingGET_1", "query:offset", "offset"
            )
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersUnfilledParametersUsingGET_1", "query:limit", "limit"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOffersUnfilledParametersUsingGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get offers with missing parameters

    Use this resource to get information about required parameters or parameters scheduled to become required that are not filled in offers. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-sprawdzic-nieuzupelnione-parametry-w-ofertach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-check-unfilled-parameters-in-offers" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/unfilled-parameters``
    """
    return call_operation(
        "getOffersUnfilledParametersUsingGET_1",
        {
            "query:offer.id": offer_id,
            "query:parameterType": parameterType,
            "query:offset": offset,
            "query:limit": limit,
            "header:Accept-Language": Accept_Language,
        },
    )
