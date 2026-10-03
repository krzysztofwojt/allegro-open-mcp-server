# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Tax settings
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
def get_tax_settings_for_category(
    *,
    category_id: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getTaxSettingsForCategory", "query:category.id", "category_id"
            )
        ),
    ],
    countryCode: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getTaxSettingsForCategory", "query:countryCode", "countryCode"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getTaxSettingsForCategory", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get all tax settings for category

    Use this resource to receive tax settings for a given leaf category. Based on received settings you may set VAT tax settings for your offers. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#opcje-faktury-i-stawki-vat" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#invoice-and-vat-settings" target="_blank">EN</a>.


    HTTP: ``GET /sale/tax-settings``
    """
    return call_operation(
        "getTaxSettingsForCategory",
        {
            "query:category.id": category_id,
            "query:countryCode": countryCode,
            "header:Accept-Language": Accept_Language,
        },
    )
