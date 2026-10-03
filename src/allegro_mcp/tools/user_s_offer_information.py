# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: User's offer information
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
def get_product_offer(
    *,
    offerId: Annotated[
        str, Field(json_schema_extra=input_schema("getProductOffer", "path:offerId", "offerId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getProductOffer", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get all data of the particular product-offer

    Use this resource to retrieve all data of the particular product-offer. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#asynchroniczne-procesowanie" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#asynchronous-processing" target="_blank">EN</a>.


    HTTP: ``GET /sale/product-offers/{offerId}``
    """
    return call_operation(
        "getProductOffer", {"path:offerId": offerId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_partial_product_offer(
    *,
    offerId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getPartialProductOffer", "path:offerId", "offerId")),
    ],
    include: Annotated[
        list[str],
        Field(json_schema_extra=input_schema("getPartialProductOffer", "query:include", "include")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPartialProductOffer", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get selected data of the particular product-offer

    Use this resource to retrieve selected data of the particular product-offer. The model and functionality is a subset of the full product offer get endpoint (`GET /sale/product-offers/{offerId}`), but it is faster and more reliable. Read more: <a href="../../news/get-sale-product-offers-offerid-parts-pobierz-wybrane-elementy-oferty-aMoB3nZk3Iv" target="_blank">PL</a> / <a href="../../news/get-sale-product-offers-offerid-parts-retrieve-selected-parts-of-the-offer-Pg51yzeAPf3" target="_blank">EN</a>.


    HTTP: ``GET /sale/product-offers/{offerId}/parts``
    """
    return call_operation(
        "getPartialProductOffer",
        {
            "path:offerId": offerId,
            "query:include": include,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def search_offers(
    *,
    offer_id: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("searchOffersUsingGET", "query:offer.id", "offer_id")),
    ] = None,
    name: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("searchOffersUsingGET", "query:name", "name")),
    ] = None,
    sellingMode_price_amount_gte: Annotated[
        float | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:sellingMode.price.amount.gte",
                "sellingMode_price_amount_gte",
            )
        ),
    ] = None,
    sellingMode_price_amount_lte: Annotated[
        float | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:sellingMode.price.amount.lte",
                "sellingMode_price_amount_lte",
            )
        ),
    ] = None,
    sellingMode_priceAutomation_rule_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:sellingMode.priceAutomation.rule.id",
                "sellingMode_priceAutomation_rule_id",
            )
        ),
    ] = None,
    sellingMode_priceAutomation_rule_id_empty: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:sellingMode.priceAutomation.rule.id.empty",
                "sellingMode_priceAutomation_rule_id_empty",
            )
        ),
    ] = None,
    publication_status: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:publication.status", "publication_status"
            )
        ),
    ] = None,
    publication_marketplace: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:publication.marketplace", "publication_marketplace"
            )
        ),
    ] = None,
    sellingMode_format: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:sellingMode.format", "sellingMode_format"
            )
        ),
    ] = None,
    external_id: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:external.id", "external_id"
            )
        ),
    ] = None,
    delivery_shippingRates_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:delivery.shippingRates.id",
                "delivery_shippingRates_id",
            )
        ),
    ] = None,
    delivery_shippingRates_id_empty: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:delivery.shippingRates.id.empty",
                "delivery_shippingRates_id_empty",
            )
        ),
    ] = None,
    sort: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("searchOffersUsingGET", "query:sort", "sort")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("searchOffersUsingGET", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("searchOffersUsingGET", "query:offset", "offset")),
    ] = None,
    category_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:category.id", "category_id"
            )
        ),
    ] = None,
    product_id_empty: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:product.id.empty", "product_id_empty"
            )
        ),
    ] = None,
    productizationRequired: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:productizationRequired", "productizationRequired"
            )
        ),
    ] = None,
    b2b_buyableOnlyByBusiness: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:b2b.buyableOnlyByBusiness",
                "b2b_buyableOnlyByBusiness",
            )
        ),
    ] = None,
    fundraisingCampaign_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:fundraisingCampaign.id", "fundraisingCampaign_id"
            )
        ),
    ] = None,
    fundraisingCampaign_id_empty: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:fundraisingCampaign.id.empty",
                "fundraisingCampaign_id_empty",
            )
        ),
    ] = None,
    afterSalesServices_returnPolicy_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET",
                "query:afterSalesServices.returnPolicy.id",
                "afterSalesServices_returnPolicy_id",
            )
        ),
    ] = None,
    isFulfillment: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "query:isFulfillment", "isFulfillment"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "searchOffersUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get seller's offers

    Use this resource to get the list of the seller's offers. You can use different query parameters to filter the list. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-moje-oferty-w-rest-api" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#list-of-offers" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers``
    """
    return call_operation(
        "searchOffersUsingGET",
        {
            "query:offer.id": offer_id,
            "query:name": name,
            "query:sellingMode.price.amount.gte": sellingMode_price_amount_gte,
            "query:sellingMode.price.amount.lte": sellingMode_price_amount_lte,
            "query:sellingMode.priceAutomation.rule.id": sellingMode_priceAutomation_rule_id,
            "query:sellingMode.priceAutomation.rule.id.empty": sellingMode_priceAutomation_rule_id_empty,
            "query:publication.status": publication_status,
            "query:publication.marketplace": publication_marketplace,
            "query:sellingMode.format": sellingMode_format,
            "query:external.id": external_id,
            "query:delivery.shippingRates.id": delivery_shippingRates_id,
            "query:delivery.shippingRates.id.empty": delivery_shippingRates_id_empty,
            "query:sort": sort,
            "query:limit": limit,
            "query:offset": offset,
            "query:category.id": category_id,
            "query:product.id.empty": product_id_empty,
            "query:productizationRequired": productizationRequired,
            "query:b2b.buyableOnlyByBusiness": b2b_buyableOnlyByBusiness,
            "query:fundraisingCampaign.id": fundraisingCampaign_id,
            "query:fundraisingCampaign.id.empty": fundraisingCampaign_id_empty,
            "query:afterSalesServices.returnPolicy.id": afterSalesServices_returnPolicy_id,
            "query:isFulfillment": isFulfillment,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_offer_smart_classification_get(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getOfferSmartClassificationGET", "path:offerId", "offerId"
            )
        ),
    ],
    marketplaceId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferSmartClassificationGET", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferSmartClassificationGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get Smart! classification report of the particular offer

    Use this resource to get a full Smart! offer classification report of one of your offers. Please keep in mind you have to meet Smart! seller conditions first - for more details, use *GET /sale/smart*. To learn more about Smart! offer requirements, see our knowledge base article: [PL](https://help.allegro.com/pl/sell/a/allegro-smart-na-allegro-pl-informacje-dla-sprzedajacych-9g0rWRXKxHG#jakie-warunki-musisz-spelnic-aby-zyskac-oznaczenie-smart) / [EN](https://help.allegro.com/en/sell/a/allegro-smart-on-allegro-pl-information-for-sellers-LR8j8Y26GTR#what-requirements-you-need-to-meet-to-get-the-smart-badge). Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#kwalifikacja-oferty" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#offer-qualification" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/{offerId}/smart``
    """
    return call_operation(
        "getOfferSmartClassificationGET",
        {
            "path:offerId": offerId,
            "query:marketplaceId": marketplaceId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_offer_events(
    *,
    from_: Annotated[
        str | None, Field(json_schema_extra=input_schema("getOfferEvents", "query:from", "from_"))
    ] = None,
    limit: Annotated[
        int | None, Field(json_schema_extra=input_schema("getOfferEvents", "query:limit", "limit"))
    ] = None,
    type_: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getOfferEvents", "query:type", "type_")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferEvents", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get events about the seller's offers

    Use this endpoint to get events from the last 24 hours concerning changes in the authorized seller's offers. At present we support the following events: - OFFER_ACTIVATED - offer is visible on site and available for purchase, occurs when offer status changes from ACTIVATING to ACTIVE. - OFFER_CHANGED - occurs when offer's fields have been changed e.g. description or photos, but does not apply to shipping rates and dispatch time. - OFFER_ENDED - offer is no longer available for purchase, occurs when offer status changes from ACTIVE to ENDED. - OFFER_STOCK_CHANGED - stock in an offer was changed either via purchase or by seller. - OFFER_PRICE_CHANGED - occurs when price in an offer was changed. - OFFER_ARCHIVED - offer is no longer available on listing and has been archived. - OFFER_BID_PLACED - bid was placed on the offer. - OFFER_BID_CANCELED - bid for offer was canceled. - OFFER_TRANSLATION_UPDATED - translation of offer was updated. - OFFER_VISIBILITY_CHANGED - visibility of offer was changed on marketplaces. - OFFER_DELIVERY_COUNTRIES_BLOCKED - the offer has been blocked in selected countries. Returned events may occur by actions made via browser or API. The resource allows you to get events concerning active offers and offers scheduled for activation (status ACTIVE and ACTIVATING). Returned events do not concern offers in INACTIVE and ENDED status (the exception is OFFER_ARCHIVED event). External id is returned for all event types except OFFER_BID_PLACED and…


    HTTP: ``GET /sale/offer-events``
    """
    return call_operation(
        "getOfferEvents",
        {
            "query:from": from_,
            "query:limit": limit,
            "query:type": type_,
            "header:Accept-Language": Accept_Language,
        },
    )
