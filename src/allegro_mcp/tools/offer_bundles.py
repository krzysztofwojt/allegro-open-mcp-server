# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Offer bundles
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
def list_sellers_offer_bundles(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersOfferBundlesUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersOfferBundlesUsingGET", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    page_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersOfferBundlesUsingGET", "query:page.id", "page_id"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersOfferBundlesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List seller's bundles

    You can fetch page of seller's offer bundles using this endpoint. <br> Paging: <br> To move to next page, specify `page.id` parameter with value obtained in response from previous request. Number of offer bundles on single page can be specified using `limit` parameter. <br> Filtering: <br> Offer bundles can be filtered to bundles which contain offer specified in `offer.id` parameter. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-liste-zestawow-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-offer-bundles-list" target="_blank">EN</a>.


    HTTP: ``GET /sale/bundles``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "listSellersOfferBundlesUsingGET",
        {
            "query:limit": limit,
            "query:offer.id": offer_id,
            "query:page.id": page_id,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_offer_bundle(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getOfferBundleUsingGET", "path:bundleId", "bundleId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferBundleUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get bundle by ID

    Use this resource to retrieve offer bundle by its unique identifier. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-szczegoly-wybranego-zestawu" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-details-of-the-selected-offer-bundle" target="_blank">EN</a>.


    HTTP: ``GET /sale/bundles/{bundleId}``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "getOfferBundleUsingGET",
        {"path:bundleId": bundleId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_offer_bundle(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("deleteOfferBundleUsingGET", "path:bundleId", "bundleId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteOfferBundleUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete bundle by ID

    Use this resource to delete offer bundle by its unique identifier. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#usun-wybrany-zestaw" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#remove-the-selected-offer-bundle" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/bundles/{bundleId}``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "deleteOfferBundleUsingGET",
        {"path:bundleId": bundleId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_offer_bundle_discount(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateOfferBundleDiscountUsingPUT", "path:bundleId", "bundleId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateOfferBundleDiscountUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateOfferBundleDiscountUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update discount associated with bundle

    Use this resource to update discount per marketplaces associated with bundle specified by its unique identifier. This will override currently set discounts for all marketplaces, so the unchanged discounts also must be specified in request. In case discount for marketplace is not specified in request it will be deleted. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#zmien-rabat-przypisany-do-wybranego-zestawu" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#change-the-discount-for-the-selected-offer-bundle" target="_blank">EN</a>.


    HTTP: ``PUT /sale/bundles/{bundleId}/discount``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "updateOfferBundleDiscountUsingPUT",
        {"path:bundleId": bundleId, "header:Accept-Language": Accept_Language, "body": body},
    )
