# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: After sale services
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
def get_public_seller_listing_using_get_1(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_1", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_1", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's return policies

    Use this resource to get the seller's return policies. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-warunki-zwrotow-przypisane-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-return-policies-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/return-policies``
    """
    return call_operation(
        "getPublicSellerListingUsingGET_1",
        {"query:limit": limit, "query:offset": offset, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_after_sales_service_return_policy(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceReturnPolicyUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceReturnPolicyUsingPOST", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Create new user's return policy

    Use this resource to create a return policy definition. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-informacje-o-warunkach-zwrotow" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-return-policy-information" target="_blank">EN</a>.


    HTTP: ``POST /after-sales-service-conditions/return-policies``
    """
    return call_operation(
        "createAfterSalesServiceReturnPolicyUsingPOST",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_after_sales_service_return_policy(
    *,
    returnPolicyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceReturnPolicyUsingGET", "path:returnPolicyId", "returnPolicyId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceReturnPolicyUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's return policy

    Use this resource to get a return policy details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-warunki-zwrotow-przypisane-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-return-policies-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/return-policies/{returnPolicyId}``
    """
    return call_operation(
        "getAfterSalesServiceReturnPolicyUsingGET",
        {"path:returnPolicyId": returnPolicyId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_after_sales_service_return_policy(
    *,
    returnPolicyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceReturnPolicyUsingPUT",
                "path:returnPolicyId",
                "returnPolicyId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceReturnPolicyUsingPUT",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceReturnPolicyUsingPUT", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Change the user's return policy

    Use this resource to modify the return policy details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-edytowac-informacje-o-warunkach-zwrotu" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-update-return-policy-information" target="_blank">EN</a>.


    HTTP: ``PUT /after-sales-service-conditions/return-policies/{returnPolicyId}``
    """
    return call_operation(
        "updateAfterSalesServiceReturnPolicyUsingPUT",
        {
            "path:returnPolicyId": returnPolicyId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_after_sales_service_return_policy(
    *,
    returnPolicyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteAfterSalesServiceReturnPolicyUsingDELETE",
                "path:returnPolicyId",
                "returnPolicyId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteAfterSalesServiceReturnPolicyUsingDELETE",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete the user's return policy

    Use this resource to delete a return policy definition.


    HTTP: ``DELETE /after-sales-service-conditions/return-policies/{returnPolicyId}``
    """
    return call_operation(
        "deleteAfterSalesServiceReturnPolicyUsingDELETE",
        {"path:returnPolicyId": returnPolicyId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_public_seller_listing(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getPublicSellerListingUsingGET", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's implied warranties

    Use this resource to get the seller's implied warranties. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-warunki-reklamacji-przypisane-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-implied-warranties-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/implied-warranties``
    """
    return call_operation(
        "getPublicSellerListingUsingGET",
        {"query:limit": limit, "query:offset": offset, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_after_sales_service_implied_warranty(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceImpliedWarrantyUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceImpliedWarrantyUsingPOST", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Create new user's implied warranty

    Use this resource to create an implied warranty definition. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-informacje-o-warunkach-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-implied-warranty-information" target="_blank">EN</a>.


    HTTP: ``POST /after-sales-service-conditions/implied-warranties``
    """
    return call_operation(
        "createAfterSalesServiceImpliedWarrantyUsingPOST",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_after_sales_service_implied_warranty(
    *,
    impliedWarrantyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceImpliedWarrantyUsingGET",
                "path:impliedWarrantyId",
                "impliedWarrantyId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceImpliedWarrantyUsingGET",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's implied warranty

    Use this resource to get an implied warranty details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-warunki-reklamacji-przypisane-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-implied-warranties-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/implied-warranties/{impliedWarrantyId}``
    """
    return call_operation(
        "getAfterSalesServiceImpliedWarrantyUsingGET",
        {"path:impliedWarrantyId": impliedWarrantyId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_after_sales_service_implied_warranty(
    *,
    impliedWarrantyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceImpliedWarrantyUsingPUT",
                "path:impliedWarrantyId",
                "impliedWarrantyId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceImpliedWarrantyUsingPUT",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceImpliedWarrantyUsingPUT", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Change the user's implied warranty

    Use this resource to modify the implied warranty details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-edytowac-informacje-o-warunkach-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-update-implied-warranty-information" target="_blank">EN</a>.


    HTTP: ``PUT /after-sales-service-conditions/implied-warranties/{impliedWarrantyId}``
    """
    return call_operation(
        "updateAfterSalesServiceImpliedWarrantyUsingPUT",
        {
            "path:impliedWarrantyId": impliedWarrantyId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
def get_public_seller_listing_using_get_2(
    *,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_2", "query:limit", "limit"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_2", "query:offset", "offset"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPublicSellerListingUsingGET_2", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's warranties

    Use this resource to get the seller's warranties. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-informacje-o-gwarancjach-przypisanych-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-warranties-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/warranties``
    """
    return call_operation(
        "getPublicSellerListingUsingGET_2",
        {"query:limit": limit, "query:offset": offset, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_after_sales_service_warranty(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceWarrantyUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceWarrantyUsingPOST", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Create new user's warranty

    Use this resource to create a warranty definition. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-informacje-o-gwarancjach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-warranty-information" target="_blank">EN</a>.


    HTTP: ``POST /after-sales-service-conditions/warranties``
    """
    return call_operation(
        "createAfterSalesServiceWarrantyUsingPOST",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_after_sales_service_warranty(
    *,
    warrantyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceWarrantyUsingGET", "path:warrantyId", "warrantyId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAfterSalesServiceWarrantyUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's warranty

    Use this resource to get a warranty details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-pobrac-informacje-o-gwarancjach-przypisanych-do-konta" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-retrieve-warranties-assigned-to-the-account" target="_blank">EN</a>.


    HTTP: ``GET /after-sales-service-conditions/warranties/{warrantyId}``
    """
    return call_operation(
        "getAfterSalesServiceWarrantyUsingGET",
        {"path:warrantyId": warrantyId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_after_sales_service_warranty(
    *,
    warrantyId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceWarrantyUsingPUT", "path:warrantyId", "warrantyId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceWarrantyUsingPUT",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "updateAfterSalesServiceWarrantyUsingPUT", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Change the user's warranty

    Use this resource to modify the warranty details. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-edytowac-informacje-o-gwarancjach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-update-warranty-information" target="_blank">EN</a>.


    HTTP: ``PUT /after-sales-service-conditions/warranties/{warrantyId}``
    """
    return call_operation(
        "updateAfterSalesServiceWarrantyUsingPUT",
        {"path:warrantyId": warrantyId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_after_sales_service_conditions_attachment(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceConditionsAttachmentUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "createAfterSalesServiceConditionsAttachmentUsingPOST", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Create a warranty attachment metadata

    You can attach PDF files to warranties. Uploading attachments flow: 1. Create an attachment object to receive an upload URL (*POST /after-sales-service-conditions/attachments*), 2. Use the upload URL to submit the PDF file (*PUT /after-sales-service-conditions/attachments/{attachmentId}*), 3. Create (or update) warranty with attachment (*POST /after-sales-service-conditions/warranties*). Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-zalacznik-do-informacji-o-gwarancjach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-attachment-to-warranty-information" target="_blank">EN</a>.


    HTTP: ``POST /after-sales-service-conditions/attachments``
    """
    return call_operation(
        "createAfterSalesServiceConditionsAttachmentUsingPOST",
        {"header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_after_sales_service_conditions_attachment(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "uploadAfterSalesServiceConditionsAttachmentUsingPUT",
                "path:attachmentId",
                "attachmentId",
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadAfterSalesServiceConditionsAttachmentUsingPUT",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    content_base64: str,
    content_type: str = "application/pdf",
) -> Any | ErrorResponse:
    """Upload an warranty attachment

    Upload an after sale services attachment. This operation should be used after creating an offer attachment with *POST /sale/offer-attachments* **Important!** You can find the URL address to upload the file to our server in the *Location* response header of *POST /after-sales-service-conditions/attachments*. The URL is unique and one-time. As its format may change in time, you should always use the address from the header. Do not compose the address on your own. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-dodac-zalacznik-do-informacji-o-gwarancjach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-add-attachment-to-warranty-information" target="_blank">EN</a>.


    HTTP: ``PUT /after-sales-service-conditions/attachments/{attachmentId}``
    """
    return call_operation(
        "uploadAfterSalesServiceConditionsAttachmentUsingPUT",
        {
            "path:attachmentId": attachmentId,
            "header:Accept-Language": Accept_Language,
            "content_base64": content_base64,
            "content_type": content_type,
        },
    )
