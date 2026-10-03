# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Compatibility List
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
def get_categories_that_support_compatibility_list(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoriesThatSupportCompatibilityList",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of categories where compatibility list is supported

    Compatibility list is available in particular categories, this resource allows to get the list of these categories with additional details. Read more: <a href="../../tutorials/jak-zarzadzac-sekcja-pasuje-do-E7Zj6gAEGil#jak-sprawdzic-czy-w-danej-kategorii-moge-dodac-sekcje-pasuje-do-do-oferty" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-compatibility-section-v8WbL1wV0Hz#which-categories-support-compatibility-section" target="_blank">EN</a>.


    HTTP: ``GET /sale/compatibility-list/supported-categories``
    """
    return call_operation(
        "getCategoriesThatSupportCompatibilityList", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_compatibility_list_suggestion(
    *,
    offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibilityListSuggestion", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    product_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibilityListSuggestion", "query:product.id", "product_id"
            )
        ),
    ] = None,
    language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibilityListSuggestion", "query:language", "language"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibilityListSuggestion", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get suggested compatibility list.

    Resource allows to fetch compatibility list suggestion for given offer or product. Read more: <a href="../../tutorials/jak-zarzadzac-sekcja-pasuje-do-E7Zj6gAEGil#jak-wyszukac-sugerowana-sekcje-compatibilitylist" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-compatibility-section-v8WbL1wV0Hz#how-to-search-for-the-suggested-compatibility-section" target="_blank">EN</a>.


    HTTP: ``GET /sale/compatibility-list-suggestions``
    """
    return call_operation(
        "getCompatibilityListSuggestion",
        {
            "query:offer.id": offer_id,
            "query:product.id": product_id,
            "query:language": language,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_compatible_products_groups(
    *,
    If_Modified_Since: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProductsGroups", "header:If-Modified-Since", "If_Modified_Since"
            )
        ),
    ] = None,
    type_: Annotated[
        str,
        Field(json_schema_extra=input_schema("getCompatibleProductsGroups", "query:type", "type_")),
    ],
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getCompatibleProductsGroups", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getCompatibleProductsGroups", "query:offset", "offset")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProductsGroups", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of compatible product groups

    Compatible products are organized in groups, this resource allows to browse these groups. Read more: <a href="../../tutorials/jak-zarzadzac-sekcja-pasuje-do-E7Zj6gAEGil#jak-zarzadzac-sekcja-pasuje-do-zintegrowana-z-baza-pojazdow" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-compatibility-section-v8WbL1wV0Hz#managing-the-compatibility-section-compatibilitylist-integrated-vehicle-database" target="_blank">EN</a>.


    HTTP: ``GET /sale/compatible-products/groups``
    """
    return call_operation(
        "getCompatibleProductsGroups",
        {
            "header:If-Modified-Since": If_Modified_Since,
            "query:type": type_,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_compatible_products(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProducts", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    If_Modified_Since: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProducts", "header:If-Modified-Since", "If_Modified_Since"
            )
        ),
    ] = None,
    type_: Annotated[
        str, Field(json_schema_extra=input_schema("getCompatibleProducts", "query:type", "type_"))
    ],
    group_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getCompatibleProducts", "query:group.id", "group_id")
        ),
    ] = None,
    tecdoc_kTypNr: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProducts", "query:tecdoc.kTypNr", "tecdoc_kTypNr"
            )
        ),
    ] = None,
    tecdoc_nTypNr: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCompatibleProducts", "query:tecdoc.nTypNr", "tecdoc_nTypNr"
            )
        ),
    ] = None,
    phrase: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCompatibleProducts", "query:phrase", "phrase")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCompatibleProducts", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCompatibleProducts", "query:offset", "offset")),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of compatible products

    Resource allows to fetch compatible products of given type. Read more: <a href="../../tutorials/jak-zarzadzac-sekcja-pasuje-do-E7Zj6gAEGil#jak-zarzadzac-sekcja-pasuje-do-zintegrowana-z-baza-pojazdow" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-compatibility-section-v8WbL1wV0Hz#managing-the-compatibility-section-compatibilitylist-integrated-vehicle-database" target="_blank">EN</a>.


    HTTP: ``GET /sale/compatible-products``
    """
    return call_operation(
        "getCompatibleProducts",
        {
            "header:Accept-Language": Accept_Language,
            "header:If-Modified-Since": If_Modified_Since,
            "query:type": type_,
            "query:group.id": group_id,
            "query:tecdoc.kTypNr": tecdoc_kTypNr,
            "query:tecdoc.nTypNr": tecdoc_nTypNr,
            "query:phrase": phrase,
            "query:limit": limit,
            "query:offset": offset,
        },
    )
