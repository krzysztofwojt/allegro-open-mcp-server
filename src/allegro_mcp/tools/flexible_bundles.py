# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Flexible bundles
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
def create_flexible_bundle(
    *,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createFlexibleBundleUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create new flexible bundle

    You can create flexible bundle using this resource. <br> Requirements: <ul> <li> there are max 6 slots in bundle;</li> <li> order value for each slot must be unique (ranging from 0 to 5);</li> <li> each slot can contain up to 30 offers;</li> <li> all offers in slot must be from the same category leaf (based on assortment's tree);</li> <li> at least one slot has to be marked as entrypoint;</li> <li> offer can be used in bundle only once (cannot be used in multiple slots);</li> <li> only offers active on at least one marketplace can be used;</li> <li> B2B offers cannot be used;</li> <li> age-restricted offers (eg. alcohol) cannot be used;</li> <li> cannot use multiple offers which are representing same product;</li> <li> all offers in bundle have to be 1F or not 1F.</li> </ul> Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#zestawy-elastyczne" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#flexible-bundles" target="_blank">EN</a>.


    HTTP: ``POST /sale/flexible-bundles``
    """
    return call_operation("createFlexibleBundleUsingPOST", {"body": body})


@mcp.tool
@allegro_call
def list_sellers_flexible_bundles(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersFlexibleBundlesUsingGET", "query:limit", "limit"
            )
        ),
    ] = None,
    offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersFlexibleBundlesUsingGET", "query:offer.id", "offer_id"
            )
        ),
    ] = None,
    page_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellersFlexibleBundlesUsingGET", "query:page.id", "page_id"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List seller's flexible bundles

    You can fetch page of seller's flexible bundles using this endpoint. <br> Paging: <br> To move to next page, specify `page.id` parameter with value obtained in response from previous request. Number of offer bundles on single page can be specified using `limit` parameter. <br> Filtering: <br> Offer bundles can be filtered to bundles which contain offer specified in `offer.id` parameter. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-liste-zestawow-elastycznych" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#list-seller-s-flexible-bundles" target="_blank">EN</a>.


    HTTP: ``GET /sale/flexible-bundles``
    """
    return call_operation(
        "listSellersFlexibleBundlesUsingGET",
        {"query:limit": limit, "query:offer.id": offer_id, "query:page.id": page_id},
    )


@mcp.tool
@allegro_call
def get_flexible_bundle(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getFlexibleBundleUsingGET", "path:bundleId", "bundleId")
        ),
    ],
) -> Any | ErrorResponse:
    """Get flexible bundle by ID

    Use this resource to retrieve flexible bundle by its unique identifier. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#pobierz-szczegoly-wybranego-zestawu" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#get-details-of-a-selected-bundle" target="_blank">EN</a>.


    HTTP: ``GET /sale/flexible-bundles/{bundleId}``
    """
    return call_operation("getFlexibleBundleUsingGET", {"path:bundleId": bundleId})


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_flexible_bundle(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateFlexibleBundleUsingPUT", "path:bundleId", "bundleId"
            )
        ),
    ],
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateFlexibleBundleUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Updates flexible bundle

    You can update flexible bundle using this resource. <br> Requirements: <ul> <li> there are max 6 slots in bundle;</li> <li> order value for each slot must be unique (ranging from 0 to 5);</li> <li> each slot can contain up to 30 offers;</li> <li> all offers in slot must be from the same category leaf (based on assortment's tree);</li> <li> at least one slot has to be marked as entrypoint;</li> <li> offer can be used in bundle only once (cannot be used in multiple slots);</li> <li> only offers active on at least one marketplace can be used;</li> <li> B2B offers cannot be used;</li> <li> age-restricted offers (eg. alcohol) cannot be used;</li> <li> cannot use multiple offers which are representing same product;</li> <li> all offers in bundle have to be 1F or not 1F.</li> </ul> Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#aktualizuj-wybrany-zestaw-elastyczny" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#update-a-selected-flexible-bundle" target="_blank">EN</a>.


    HTTP: ``PUT /sale/flexible-bundles/{bundleId}``
    """
    return call_operation("updateFlexibleBundleUsingPUT", {"path:bundleId": bundleId, "body": body})


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_flexible_bundle(
    *,
    bundleId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteFlexibleBundleUsingDELETE", "path:bundleId", "bundleId"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Delete flexible bundle by ID

    Use this resource to delete flexible bundle by its unique identifier. Read more: <a href="../../tutorials/jak-zarzadzac-rabatami-promocjami-yPya2mj6zUP#usun-wybrany-zestaw" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-rebates-and-promotions-g05avdL0vT4#delete-a-selected-bundle" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/flexible-bundles/{bundleId}``
    """
    return call_operation("deleteFlexibleBundleUsingDELETE", {"path:bundleId": bundleId})
