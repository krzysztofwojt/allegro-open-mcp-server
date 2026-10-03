# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Post Purchase Issues
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
def get_list_of_issues(
    *,
    checkoutForm_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfIssuesUsingGET", "query:checkoutForm.id", "checkoutForm_id"
            )
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getListOfIssuesUsingGET", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getListOfIssuesUsingGET", "query:offset", "offset")),
    ] = None,
    status: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getListOfIssuesUsingGET", "query:status", "status")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfIssuesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's post purchase issues

    Use this resource to get the list of your disputes and claims ordered by descending opened date. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#lista-dyskusji-i-reklamacji-na-koncie" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#all-disputes-and-claims" target="_blank">EN</a>.


    HTTP: ``GET /sale/issues``
    """
    return call_operation(
        "getListOfIssuesUsingGET",
        {
            "query:checkoutForm.id": checkoutForm_id,
            "query:limit": limit,
            "query:offset": offset,
            "query:status": status,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_issue(
    *,
    issueId: Annotated[
        str, Field(json_schema_extra=input_schema("getIssueUsingGET", "path:issueId", "issueId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getIssueUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a single dispute or claim

    Use this resource to get a single dispute or claim. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#szczegolowe-informacje-o-dyskusji-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#detailed-information-about-the-dispute-claim" target="_blank">EN</a>.


    HTTP: ``GET /sale/issues/{issueId}``
    """
    return call_operation(
        "getIssueUsingGET", {"path:issueId": issueId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_chat_from_issue(
    *,
    issueId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getChatFromIssueUsingGET", "path:issueId", "issueId")
        ),
    ],
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getChatFromIssueUsingGET", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getChatFromIssueUsingGET", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getChatFromIssueUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the messages and state claim changes within a post purchase issue

    Use this resource to get the list of messages and state changes within a dispute or claim. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#wiadomosci-z-dyskusji-i-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#disputes-and-claims-messages" target="_blank">EN</a>.


    HTTP: ``GET /sale/issues/{issueId}/chat``
    """
    return call_operation(
        "getChatFromIssueUsingGET",
        {
            "path:issueId": issueId,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def add_message_to_issue(
    *,
    issueId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("addMessageToIssueUsingPOST", "path:issueId", "issueId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "addMessageToIssueUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Add a message to an issue

    Use this resource to post a message in certain issue. At least one of fields: 'text', 'attachment' has to be present. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#nowa-wiadomosc-w-dyskusji-lub-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#new-message-in-dispute-or-claim" target="_blank">EN</a>.


    HTTP: ``POST /sale/issues/{issueId}/message``
    """
    return call_operation(
        "addMessageToIssueUsingPOST",
        {"path:issueId": issueId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def change_status_of_issue(
    *,
    issueId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "changeStatusOfIssueUsingPOST", "path:issueId", "issueId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "changeStatusOfIssueUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Change status of a claim

    Change the formal status of a claim, for example accept or reject it. Not a valid operation for disputes. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#zmien-status-reklamacji" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#change-claim-status" target="_blank">EN</a>.


    HTTP: ``POST /sale/issues/{issueId}/status``
    """
    return call_operation(
        "changeStatusOfIssueUsingPOST",
        {"path:issueId": issueId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_an_issue_attachment(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAnIssueAttachmentUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Create an attachment declaration

    Use this resource to post an attachment declaration. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#deklaracja-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#attachment-declaration" target="_blank">EN</a>.


    HTTP: ``POST /sale/issues/attachments``
    """
    return call_operation(
        "createAnIssueAttachmentUsingPOST", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_issue_attachment(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "uploadIssueAttachmentUsingPUT", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadIssueAttachmentUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    content_base64: str,
    content_type: str = "image/png",
) -> Any | ErrorResponse:
    """Upload an attachment

    Upload a post purchase issue message attachment. This operation should be used after creating an attachment declaration with *POST /sale/issues/attachments* **Important!** You can find the URL address to upload the file to our server in the *Location* response header of *POST /sale/issues/attachments*. The URL is unique and one-time. As its format may change in time, you should always use the address from the header. Do not compose the address on your own. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#dodanie-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#adding-an-attachment" target="_blank">EN</a>.


    HTTP: ``PUT /sale/issues/attachments/{attachmentId}``
    """
    return call_operation(
        "uploadIssueAttachmentUsingPUT",
        {
            "path:attachmentId": attachmentId,
            "header:Accept-Language": Accept_Language,
            "content_base64": content_base64,
            "content_type": content_type,
        },
    )


@mcp.tool
@allegro_call
def get_issue_attachment(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getIssueAttachmentUsingGET", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getIssueAttachmentUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get an attachment

    Use this resource to get an attachment. Read more: <a href="../../tutorials/jak-zarzadzac-dyskusjami-E7Zj6gK7ysE#pobranie-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-discussions-VL6Yr40e5t5#attachment-related-to-dispute-claim" target="_blank">EN</a>.


    HTTP: ``GET /sale/issues/attachments/{attachmentId}``
    """
    return call_operation(
        "getIssueAttachmentUsingGET",
        {"path:attachmentId": attachmentId, "header:Accept-Language": Accept_Language},
    )
