# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Images and attachments
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
def upload_offer_image(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadOfferImageUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    isAiCoCreated: Annotated[
        bool | None,
        Field(
            json_schema_extra=input_schema(
                "uploadOfferImageUsingPOST", "query:isAiCoCreated", "isAiCoCreated"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None,
        Field(json_schema_extra=input_schema("uploadOfferImageUsingPOST", "body", "body")),
    ] = None,
    url: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("uploadOfferImageUsingPOST", "body:url", "url")),
    ] = None,
    content_base64: str | None = None,
    content_type: str = "image/jpeg",
    body_base64: str | None = None,
) -> Any | ErrorResponse:
    """Upload an offer image

    Upload image to our servers. You can choose from two upload options: * - provide a link and we will download an image for you * - send an image as binary data **Important!** Remember to use dedicated domain for upload, i.e. * - https://upload.allegro.pl for Production * - https://upload.allegro.pl.allegrosandbox.pl for Sandbox Read more about the rules for photos in an offer's gallery and description: <a href="https://help.allegro.com/pl/sell/a/zasady-dla-zdjec-w-galerii-i-w-opisie-8dvWz3eo4T5?marketplaceId=allegro-pl" target="_blank">PL</a> / <a href="https://help.allegro.com/en/sell/a/rules-for-images-in-the-gallery-and-in-descriptions-8dvWB8Y2PIq" target="_blank">EN</a>.


    HTTP: ``POST /sale/images``

    Provide either body (JSON), url, or base64 image bytes, never multiple payloads. The returned URL can be used in product.images and offer images.
    """
    return call_operation(
        "uploadOfferImageUsingPOST",
        {
            "header:Accept-Language": Accept_Language,
            "query:isAiCoCreated": isAiCoCreated,
            "body": body,
            "body:url": url,
            "content_base64": content_base64,
            "content_type": content_type,
            "body_base64": body_base64,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_offer_attachment(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createOfferAttachmentUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createOfferAttachmentUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create an offer attachment

    You can attach pdf, jpeg or png files to your offers. We will present them under the offer description in the Additional information section. You can attach multiple files to one offer – one per each type from the list: * Guide (MANUAL). Allowed media types: PDF * Special offer terms (SPECIAL_OFFER_RULES). Allowed media types: PDF * Competition terms (COMPETITION_RULES). Allowed media types: PDF * Book excerpt (BOOK_EXCERPT). Allowed media types: PDF * Manual (USER_MANUAL). Allowed media types: PDF * Installation manual (INSTALLATION_INSTRUCTIONS). Allowed media types: PDF * Game manual (GAME_INSTRUCTIONS). Allowed media types: PDF * Energy label (ENERGY_LABEL). Allowed media types: JPEG, JPG, PNG * Product information sheet (PRODUCT_INFORMATION_SHEET). Allowed media types: PDF * Tire label (TIRE_LABEL). Allowed media types: JPEG, JPG, PNG * Data processing sheet - software (SOFTWARE_DATA_PROCESSING). Allowed media types: PDF * Data processing sheet - device (HARDWARE_DATA_PROCESSING). Allowed media types: PDF * Plant Protection Products (PPPs) license (PLANT_PROTECTION_PRODUCTS_AUTHORIZATION). Allowed media types: PDF You can attach up to 20 files to one product for: * Safety information manual (SAFETY_INFORMATION_MANUAL). Allowed media types: PDF, JPEG, JPG, PNG Uploading attachments flow: 1. Create an attachment object to receive an upload URL (*POST /sale/offer-attachments*), 2. Use the upload URL to submit the file (*PUT /sale/offer-attachments/{attachmentId}*), 3. Add…


    HTTP: ``POST /sale/offer-attachments``
    """
    return call_operation(
        "createOfferAttachmentUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_offer_attachment(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "uploadOfferAttachmentUsingPUT", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadOfferAttachmentUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    content_base64: str,
    content_type: str = "application/pdf",
) -> Any | ErrorResponse:
    """Upload an offer attachment

    Upload an offer attachment. This operation should be used after creating an offer attachment with *POST /sale/offer-attachments* **Important!** You can find the URL address to upload the file to our server in the *Location* response header of *POST /sale/offer-attachments*. The URL is unique and one-time. As its format may change in time, you should always use the address from the header. Do not compose the address on your own. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#zalaczniki" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#attachments" target="_blank">EN</a>.


    HTTP: ``PUT /sale/offer-attachments/{attachmentId}``
    """
    return call_operation(
        "uploadOfferAttachmentUsingPUT",
        {
            "path:attachmentId": attachmentId,
            "header:Accept-Language": Accept_Language,
            "content_base64": content_base64,
            "content_type": content_type,
        },
    )


@mcp.tool
@allegro_call
def get_offer_attachment(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getOfferAttachment", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOfferAttachment", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get offer attachment details

    Get details of an offer attachments, including download link, by attachment identifier ("attachmentId"). The attachment id can be retrieved by querying a particular offer, for example by using <a href="#operation/getProductOffer">`GET /sale/product-offers/{offerId}`</a>. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#zalaczniki" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#attachments" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-attachments/{attachmentId}``
    """
    return call_operation(
        "getOfferAttachment",
        {"path:attachmentId": attachmentId, "header:Accept-Language": Accept_Language},
    )
