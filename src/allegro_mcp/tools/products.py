# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Products
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
def get_flat_product_parameters(
    *,
    categoryId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getFlatProductParametersUsingGET", "path:categoryId", "categoryId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFlatProductParametersUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get product parameters available in given category

    Use this resource to get the list of product parameters available in given category. You can use these parameters to create a new product. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-utworzyc-nowy-produkt" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-create-a-product" target="_blank">EN</a>.


    HTTP: ``GET /sale/categories/{categoryId}/product-parameters``
    """
    return call_operation(
        "getFlatProductParametersUsingGET",
        {"path:categoryId": categoryId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_sale_products(
    *,
    phrase: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getSaleProducts", "query:phrase", "phrase")),
    ] = None,
    mode: Annotated[
        str | None, Field(json_schema_extra=input_schema("getSaleProducts", "query:mode", "mode"))
    ] = None,
    language: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getSaleProducts", "query:language", "language")),
    ] = None,
    category_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getSaleProducts", "query:category.id", "category_id")
        ),
    ] = None,
    Dynamic_filters: Annotated[
        dict[str, Any] | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleProducts", "query:Dynamic filters", "Dynamic_filters"
            )
        ),
    ] = None,
    page_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getSaleProducts", "query:page.id", "page_id")),
    ] = None,
    searchFeatures: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleProducts", "query:searchFeatures", "searchFeatures"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleProducts", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get search products results

    Use this resource to get a list of products according to provided parameters. At least ean or phrase parameter is required. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-znalezc-produkt" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-find-a-product" target="_blank">EN</a>. This resource is limited with Leaky Bucket mechanism, read more <a href="../../tutorials/informacje-podstawowe-b21569boAI1#ograniczenie-liczby-zapytan-limity" target="_blank">PL</a> / <a href="../../tutorials/basic-information-VL6YelvVKTn#limiting-the-number-of-queries-limits" target="_blank">EN</a>.


    HTTP: ``GET /sale/products``
    """
    return call_operation(
        "getSaleProducts",
        {
            "query:phrase": phrase,
            "query:mode": mode,
            "query:language": language,
            "query:category.id": category_id,
            "query:Dynamic filters": Dynamic_filters,
            "query:page.id": page_id,
            "query:searchFeatures": searchFeatures,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_sale_product(
    *,
    productId: Annotated[
        str, Field(json_schema_extra=input_schema("getSaleProduct", "path:productId", "productId"))
    ],
    category_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getSaleProduct", "query:category.id", "category_id")),
    ] = None,
    language: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getSaleProduct", "query:language", "language")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleProduct", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get all data of the particular product

    Use this resource to retrieve all data of the particular product. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-pobrac-pelne-dane-o-produkcie" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-retrieve-product-data" target="_blank">EN</a>. This resource is limited with <a href="../../tutorials/basic-information-VL6YelvVKTn#limiting-the-number-of-queries-limits" target="_blank">Leaky Bucket</a> mechanism.


    HTTP: ``GET /sale/products/{productId}``
    """
    return call_operation(
        "getSaleProduct",
        {
            "path:productId": productId,
            "query:category.id": category_id,
            "query:language": language,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def propose_sale_product(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "proposeSaleProduct", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("proposeSaleProduct", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Propose a product

    Use this resource to propose a product. You can add up to 20,000 new products to the Catalog each month. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-utworzyc-nowy-produkt" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-create-a-product" target="_blank">EN</a>.


    HTTP: ``POST /sale/product-proposals``
    """
    return call_operation(
        "proposeSaleProduct", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def product_change_proposal(
    *,
    productId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("productChangeProposal", "path:productId", "productId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "productChangeProposal", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("productChangeProposal", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Propose changes in product

    Use this resource to propose changes in product. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-zglosic-blad-w-produkcie" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-report-incorrect-data-in-a-product" target="_blank">EN</a>. This resource is limited to 100 suggestions per day for a single user.


    HTTP: ``POST /sale/products/{productId}/change-proposals``
    """
    return call_operation(
        "productChangeProposal",
        {"path:productId": productId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_product_change_proposal(
    *,
    changeProposalId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getProductChangeProposal", "path:changeProposalId", "changeProposalId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getProductChangeProposal", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get all data of the particular product changes proposal

    Use this resource to retrieve all data of the particular product changes proposal. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-zglosic-blad-w-produkcie" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-report-incorrect-data-in-a-product" target="_blank">EN</a>.


    HTTP: ``GET /sale/products/change-proposals/{changeProposalId}``
    """
    return call_operation(
        "getProductChangeProposal",
        {"path:changeProposalId": changeProposalId, "header:Accept-Language": Accept_Language},
    )
