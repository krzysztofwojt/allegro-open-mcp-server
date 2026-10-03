# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Offer tags
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
def create_tag_post_1(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createTagPOST_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("createTagPOST_1", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Create a tag

    Use this resource to create a new tag. You can create up to 100 tags. Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>.


    HTTP: ``POST /sale/offer-tags``
    """
    return call_operation(
        "createTagPOST_1", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def list_seller_tags_get_1(
    *,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("listSellerTagsGET_1", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("listSellerTagsGET_1", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listSellerTagsGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's tags

    Use this resource to get a list of tags defined by the specified user (Defaults: limit = 1000, offset = 0). Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-tags``
    """
    return call_operation(
        "listSellerTagsGET_1",
        {"query:limit": limit, "query:offset": offset, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_tag(
    *,
    tagId: Annotated[
        str, Field(json_schema_extra=input_schema("deleteTagUsingDELETE", "path:tagId", "tagId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteTagUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete a tag

    Use this resource to delete the tag. Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/offer-tags/{tagId}``
    """
    return call_operation(
        "deleteTagUsingDELETE", {"path:tagId": tagId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_tag_put(
    *,
    tagId: Annotated[
        str, Field(json_schema_extra=input_schema("updateTagPUT", "path:tagId", "tagId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateTagPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("updateTagPUT", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Modify a tag

    Use this resource to update a tag. Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>. This resource is rate limited to 1 million changes per hour.


    HTTP: ``PUT /sale/offer-tags/{tagId}``
    """
    return call_operation(
        "updateTagPUT",
        {"path:tagId": tagId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def assign_tag_to_offer_post(
    *,
    offerId: Annotated[
        str,
        Field(json_schema_extra=input_schema("assignTagToOfferPOST", "path:offerId", "offerId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "assignTagToOfferPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("assignTagToOfferPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Assign tags to an offer

    Use this resource to assign a tag to offer. Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>.


    HTTP: ``POST /sale/offers/{offerId}/tags``
    """
    return call_operation(
        "assignTagToOfferPOST",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def list_assigned_offer_tags_get(
    *,
    offerId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("listAssignedOfferTagsGET", "path:offerId", "offerId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listAssignedOfferTagsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get tags assigned to an offer

    Use this resource to get a list of tags assigned to offer. Read more: <a href="../../news/nowe-zasoby-zarzadzaj-tagami-i-zalacznikami-w-ofertach-1nzlmKLPyHl" target="_blank">PL</a> / <a href="../../news/new-resources-manage-tags-and-attachments-in-offers-WvGz12BXrHL" target="_blank">EN</a>.


    HTTP: ``GET /sale/offers/{offerId}/tags``
    """
    return call_operation(
        "listAssignedOfferTagsGET",
        {"path:offerId": offerId, "header:Accept-Language": Accept_Language},
    )
