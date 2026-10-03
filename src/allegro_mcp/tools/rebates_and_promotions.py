# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Rebates and promotions
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
def create_promotion_using_post_1(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createPromotionUsingPOST_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createPromotionUsingPOST_1", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create a new promotion

    This endpoint creates a new promotion. You can create promotions only if your base marketplace is `allegro-pl`. Created promotions are visible only on the `allegro-pl` marketplace. You can define the following types of promotions: 1. Large order discount <br> Only company users will see and be eligible for this type of promotion. In order to create a large order discount, you also have to be a company user. Furthermore, you are allowed to have only one active order discount at a time. Define a promotion with a single benefit of type **LARGE_ORDER_DISCOUNT** and a single criterion of type **ALL_OFFERS**. The benefit specification should contain a list of order value based discount thresholds. Threshold's order value defines the minimum total value of an order for which the threshold is applicable (`lowerBound`). Threshold's discount defines the discount percentage applied when the threshold is applied. The percentage's fractional part must be equal to 0. Only the highest applicable threshold (if any) will be applied to the total value of the order. A threshold with a higher order value than another threshold in the order discount must also have a higher discount. Large order discount is assigned automatically to all seller's offers. Moreover, it will be assigned to all newly added seller's offers once activated. Please note that it may take some time to propagate this type of promotion to all of your offers. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-…


    HTTP: ``POST /sale/loyalty/promotions``
    """
    return call_operation(
        "createPromotionUsingPOST_1", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def list_seller_promotions_using_get_1(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("listSellerPromotionsUsingGET_1", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "listSellerPromotionsUsingGET_1", "query:offset", "offset"
            )
        ),
    ] = None,
    offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellerPromotionsUsingGET_1", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    promotionType: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "listSellerPromotionsUsingGET_1", "query:promotionType", "promotionType"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellerPromotionsUsingGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's list of promotions

    Get a list of promotions defined by the authorized user and filtered by promotion type. <p>Restrictions:</p> <p>Filtering by promotion type is required.</p> <p>Sum of limit and offset must be equal to or lower than 50000. Limit must be equal to or lower than 5000.</p> <p>Example:</p> <p>offset = 49950 and limit = 50 will return promotions</p> <p>offset = 49950 and limit = 51 will return 422 http error</p> <p>offset = 0 and limit = 5000 will return promotions</p> <p>offset = 0 and limit = 5001 will return 422 http error</p> <p>Read more about: Large order discount <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-dostepne-rabaty" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-large-order-discount" target="_blank">EN</a>, Wholesale price list <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-dostepne-cenniki" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-wholesale-price-lists" target="_blank">EN</a>, Multipack <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-dostepne-rabaty-ilosciowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-promotional-sets" target="_blank">EN</a>.</p>


    HTTP: ``GET /sale/loyalty/promotions``
    """
    return call_operation(
        "listSellerPromotionsUsingGET_1",
        {
            "query:limit": limit,
            "query:offset": offset,
            "query:offer.id": offer_id,
            "query:promotionType": promotionType,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_promotion(
    *,
    promotionId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getPromotionUsingGET", "path:promotionId", "promotionId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPromotionUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a promotion data by id

    <br> Use this resource to return the requested promotion. You need to use its unique id. <br> Read more about: Large order discount <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-informacje-o-rabacie" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-information-about-large-order-discount" target="_blank">EN</a>, Wholesale price list <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-informacje-o-cenniku" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-information-about-wholesale-price-list" target="_blank">EN</a>, Multipack <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-informacje-o-rabacie-ilosciowym" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#information-about-an-quantitative-discount" target="_blank">EN</a>.


    HTTP: ``GET /sale/loyalty/promotions/{promotionId}``
    """
    return call_operation(
        "getPromotionUsingGET",
        {"path:promotionId": promotionId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_promotion(
    *,
    promotionId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updatePromotionUsingPUT", "path:promotionId", "promotionId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updatePromotionUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updatePromotionUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Modify a promotion

    Use this resource to update a promotion by its unique id. <br> It supports editing bundle's discount, wholesale price lists and large order discounts. Read more about: Large order discount <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#edytuj-progi-rabatowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#edit-discount-thresholds" target="_blank">EN</a>, Wholesale price list <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#edytuj-cennik" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#edit-wholesale-price-list" target="_blank">EN</a>.


    HTTP: ``PUT /sale/loyalty/promotions/{promotionId}``
    """
    return call_operation(
        "updatePromotionUsingPUT",
        {"path:promotionId": promotionId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def deactivate_promotion(
    *,
    promotionId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deactivatePromotionUsingDELETE", "path:promotionId", "promotionId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deactivatePromotionUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Deactivate a promotion by id

    Use this resource to deactivate the requested promotion. You need to use its unique id. <br> Read more about: Large order discount <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#usun-rabat" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#remove-large-order-discount" target="_blank">EN</a>, Wholesale price list <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#usun-cennik" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#remove-wholesale-price-list" target="_blank">EN</a>, Multipack <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#usun-rabat-ilosciowy" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#remove-an-quantitative-discount" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/loyalty/promotions/{promotionId}``
    """
    return call_operation(
        "deactivatePromotionUsingDELETE",
        {"path:promotionId": promotionId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_or_modify_turnover_discount(
    *,
    marketplaceId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "createOrModifyTurnoverDiscountUsingPUT", "path:marketplaceId", "marketplaceId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createOrModifyTurnoverDiscountUsingPUT",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema("createOrModifyTurnoverDiscountUsingPUT", "body", "body")
        ),
    ],
) -> Any | ErrorResponse:
    """Create/modify turnover discount for marketplace

    You cannot create or modify a turnover-based discount. Turnover-based discounts are about to be withdrawn from the platform. Any existing discounts will be removed automatically. This resource is deprecated and will be removed on November 2, 2026.


    HTTP: ``PUT /sale/turnover-discount/{marketplaceId}``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "createOrModifyTurnoverDiscountUsingPUT",
        {
            "path:marketplaceId": marketplaceId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
def get_turnover_discounts(
    *,
    marketplaceId: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getTurnoverDiscountsUsingGET", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTurnoverDiscountsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the list of turnover discounts

    Get a list of turnover discounts for all supported marketplaces. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-liste-rabatow-obrotowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#retrieve-the-list-of-turnover-discounts" target="_blank">EN</a>. Currently, the only supported marketplace is `allegro-business-cz`. This resource is deprecated and will be removed on November 2, 2026. <br/> Turnover discount for the marketplace can have one of the three statuses: 1. `ACTIVATING` - neither accumulation of the turnover, nor applying of the discount has started yet. Turnover will be being accumulated from the beginning of the next month. 2. `ACTIVE` - there is ongoing accumulation of the turnover and/or applying of the discount. The latest discount definition does not have fields `cumulatingToDate` and `spendingToDate` set to a specific date. There may be multiple (up to 3) definitions of the discount returned for each marketplace. Only one definition can be accumulated against, and only one definition can be applied at the same time - appropriate periods from different definitions will not overlap. 3. `DEACTIVATING` - there is ongoing accumulation of the turnover and/or applying of the discount. Accumulation of the turnover will be continued until `cumulatingToDate` of the last definition. Applying of the discount will be continued until `spendingToDate` of the last definition.


    HTTP: ``GET /sale/turnover-discount``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "getTurnoverDiscountsUsingGET",
        {"query:marketplaceId": marketplaceId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def deactivate_turnover_discounts(
    *,
    marketplaceId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deactivateTurnoverDiscountsUsingPUT", "path:marketplaceId", "marketplaceId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deactivateTurnoverDiscountsUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Deactivate turnover discount for marketplace

    Deactivate turnover discount for a given marketplace. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#deaktywuj-rabat-obrotowy" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#deactivate-turnover-discount" target="_blank">EN</a>. Currently, the only supported marketplace is `allegro-business-cz`. This resource is deprecated and will be removed on November 2, 2026. <br/> Turnover discount will stop being cumulated with the end of the current month. Discount based on cumulated turnover will stop being applied with the end of the next month. After that, the discount will be completely deactivated. <br/> When deactivating the discount that still has `ACTIVATING` status, turnover discount is deactivated immediately. In that case, no turnover discount will start being cumulated with the new month.


    HTTP: ``PUT /sale/turnover-discount/{marketplaceId}/deactivate``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "deactivateTurnoverDiscountsUsingPUT",
        {"path:marketplaceId": marketplaceId, "header:Accept-Language": Accept_Language},
    )
