# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Automatic pricing
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
def get_automatic_pricing_rules(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAutomaticPricingRulesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get automatic pricing rules

    Use this resource to get automatic pricing rules. Rules with property **default** set to **true** are default rules created by Allegro for each merchant. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-dostepne-reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-pricing-rules" target="_blank">EN</a>.


    HTTP: ``GET /sale/price-automation/rules``
    """
    return call_operation(
        "getAutomaticPricingRulesUsingGET", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_automatic_pricing_rules(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAutomaticPricingRulesUsingPost", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema("createAutomaticPricingRulesUsingPost", "body", "body")
        ),
    ],
) -> Any | ErrorResponse:
    """Post automatic pricing rule

    Use this resource to create automatic pricing rule. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-utworzyc-wlasne-reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-create-own-pricing-rules" target="_blank">EN</a>.


    HTTP: ``POST /sale/price-automation/rules``
    """
    return call_operation(
        "createAutomaticPricingRulesUsingPost",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_automatic_pricing_rule_by_id(
    *,
    ruleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAutomaticPricingRuleByIdUsingGET", "path:ruleId", "ruleId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAutomaticPricingRuleByIdUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get automatic pricing rule by id

    Use this resource to get automatic pricing rule by id. Rules with property **default** set to **true** are default rules created by Allegro for each merchant and cannot be modified. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-dostepne-reguly-cenowe" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-pricing-rules" target="_blank">EN</a>.


    HTTP: ``GET /sale/price-automation/rules/{ruleId}``
    """
    return call_operation(
        "getAutomaticPricingRuleByIdUsingGET",
        {"path:ruleId": ruleId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_automatic_pricing_rule(
    *,
    ruleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAutomaticPricingRuleUsingPut", "path:ruleId", "ruleId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAutomaticPricingRuleUsingPut", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateAutomaticPricingRuleUsingPut", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Edit automatic pricing rule

    Use this resource to update automatic pricing rule. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-edytowac-regule-cenowa" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-modify-a-pricing-rule" target="_blank">EN</a>.


    HTTP: ``PUT /sale/price-automation/rules/{ruleId}``
    """
    return call_operation(
        "updateAutomaticPricingRuleUsingPut",
        {"path:ruleId": ruleId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_automatic_pricing_rule(
    *,
    ruleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteAutomaticPricingRuleUsingDelete", "path:ruleId", "ruleId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteAutomaticPricingRuleUsingDelete", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete automatic pricing rule

    Use this resource to delete automatic pricing rule. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-usunac-regule-cenowa" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-delete-a-pricing-rule" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/price-automation/rules/{ruleId}``
    """
    return call_operation(
        "deleteAutomaticPricingRuleUsingDelete",
        {"path:ruleId": ruleId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_automatic_pricing_rules_for_offer(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAutomaticPricingRulesForOfferUsingGET", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAutomaticPricingRulesForOfferUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get automatic pricing rules assigned to the offer

    Use this resource to get automatic pricing rules for offer. This resource is rate limited to 5 requests per second. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-sprawdzic-aktualnie-przypisane-reguly-przelicznika-cen-w-ofercie" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-check-price-automation-rules-currently-assigned-to-offer" target="_blank">EN</a>.


    HTTP: ``GET /sale/price-automation/offers/{offerId}/rules``
    """
    return call_operation(
        "getAutomaticPricingRulesForOfferUsingGET",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language},
    )
