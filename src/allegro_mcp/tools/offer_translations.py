# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Offer translations
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
def get_offer_translation(
    *,
    language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferTranslationUsingGET", "query:language", "language"
            )
        ),
    ] = None,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getOfferTranslationUsingGET", "path:offerId", "offerId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferTranslationUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get offer translations

    Get offer translation for given language or all present. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#offer-translations" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/{offerId}/translations``
    """
    return call_operation(
        "getOfferTranslationUsingGET",
        {
            "query:language": language,
            "path:offerId": offerId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_offer_translation(
    *,
    language: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateOfferTranslationUsingPATCH", "path:language", "language"
            )
        ),
    ],
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateOfferTranslationUsingPATCH", "path:offerId", "offerId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateOfferTranslationUsingPATCH", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateOfferTranslationUsingPATCH", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update offer translation

    Update manual translation for offer. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#offer-translations" target="_blank">EN</a>.


    HTTP: ``PATCH /sale/offers/{offerId}/translations/{language}``
    """
    return call_operation(
        "updateOfferTranslationUsingPATCH",
        {
            "path:language": language,
            "path:offerId": offerId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_manual_translation(
    *,
    language: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteManualTranslationUsingDELETE", "path:language", "language"
            )
        ),
    ],
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteManualTranslationUsingDELETE", "path:offerId", "offerId"
            )
        ),
    ],
    element: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteManualTranslationUsingDELETE", "query:element", "element"
            )
        ),
    ] = None,
    products_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteManualTranslationUsingDELETE", "query:products.id", "products_id"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteManualTranslationUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete offer translation

    Delete single element or entire manual translation. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-ofert" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#offer-translations" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/offers/{offerId}/translations/{language}``
    """
    return call_operation(
        "deleteManualTranslationUsingDELETE",
        {
            "path:language": language,
            "path:offerId": offerId,
            "query:element": element,
            "query:products.id": products_id,
            "header:Accept-Language": Accept_Language,
        },
    )
