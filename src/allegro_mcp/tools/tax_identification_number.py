# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Tax Identification Number
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
def add_tax_id(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("addTaxId", "header:Accept-Language", "Accept_Language")
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("addTaxId", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Add tax identification number

    Use this resource to add tax identification number. For international sellers only. Read more: <a href="../../news/one-fulfillment-umozliwiamy-zarzadzanie-numerem-identyfikacji-podatkowej-vat-6M2xgdAmGFM" target="_blank">PL</a> / <a href="../../news/one-fulfillment-we-allow-you-to-manage-your-vat-identification-number-Pgj9WXjWwcm" target="_blank">EN</a>.


    HTTP: ``POST /fulfillment/tax-id``
    """
    return call_operation("addTaxId", {"header:Accept-Language": Accept_Language, "body": body})


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_tax_id(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateTaxId", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("updateTaxId", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Update tax identification number

    Use this resource to update tax identification number. For international sellers only. Read more: <a href="../../news/one-fulfillment-umozliwiamy-zarzadzanie-numerem-identyfikacji-podatkowej-vat-6M2xgdAmGFM" target="_blank">PL</a> / <a href="../../news/one-fulfillment-we-allow-you-to-manage-your-vat-identification-number-Pgj9WXjWwcm" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/tax-id``
    """
    return call_operation("updateTaxId", {"header:Accept-Language": Accept_Language, "body": body})


@mcp.tool
@allegro_call
def get_tax_id(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getTaxId", "header:Accept-Language", "Accept_Language")
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get tax identification number

    Use this resource to get tax identification number with verification status. After adding or updating the tax identification number the status will be NOT_VERIFIED and you will have to wait for acceptance status to start selling. Read more: <a href="../../news/one-fulfillment-umozliwiamy-zarzadzanie-numerem-identyfikacji-podatkowej-vat-6M2xgdAmGFM" target="_blank">PL</a> / <a href="../../news/one-fulfillment-we-allow-you-to-manage-your-vat-identification-number-Pgj9WXjWwcm" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/tax-id``
    """
    return call_operation("getTaxId", {"header:Accept-Language": Accept_Language})
