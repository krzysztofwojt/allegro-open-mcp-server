# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Message Center
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
def list_threads_get(
    *,
    limit: Annotated[
        int | None, Field(json_schema_extra=input_schema("listThreadsGET", "query:limit", "limit"))
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("listThreadsGET", "query:offset", "offset")),
    ] = None,
    page_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("listThreadsGET", "query:page.id", "page_id")),
    ] = None,
    read: Annotated[
        bool | None, Field(json_schema_extra=input_schema("listThreadsGET", "query:read", "read"))
    ] = None,
    status: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("listThreadsGET", "query:status", "status")),
    ] = None,
    type_: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("listThreadsGET", "query:type", "type_")),
    ] = None,
    orderId: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("listThreadsGET", "query:orderId", "orderId")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listThreadsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List user threads

    Use this resource to get the list of user threads sorted by last message date, starting from newest. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#lista-watkow-na-koncie" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#list-of-threads" target="_blank">EN</a>.


    HTTP: ``GET /messaging/threads``
    """
    return call_operation(
        "listThreadsGET",
        {
            "query:limit": limit,
            "query:offset": offset,
            "query:page.id": page_id,
            "query:read": read,
            "query:status": status,
            "query:type": type_,
            "query:orderId": orderId,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_thread_get(
    *,
    threadId: Annotated[
        str, Field(json_schema_extra=input_schema("getThreadGET", "path:threadId", "threadId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getThreadGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get user thread

    Use this resource to get thread with provided identifier. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#szczegolowe-informacje-o-danym-watku" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#information-about-a-particular-thread" target="_blank">EN</a>.


    HTTP: ``GET /messaging/threads/{threadId}``
    """
    return call_operation(
        "getThreadGET", {"path:threadId": threadId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def change_read_flag_on_thread_put(
    *,
    threadId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("changeReadFlagOnThreadPUT", "path:threadId", "threadId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "changeReadFlagOnThreadPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("changeReadFlagOnThreadPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Mark a particular thread as read

    Use this resource to mark thread with provided identifier as read. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#szczegolowe-informacje-o-wiadomosci" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#information-about-a-particular-message" target="_blank">EN</a>.


    HTTP: ``PUT /messaging/threads/{threadId}/read``
    """
    return call_operation(
        "changeReadFlagOnThreadPUT",
        {"path:threadId": threadId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def new_message_post(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "newMessagePOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("newMessagePOST", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Write a new message

    Use this resource to write new message to recipient. This resource is rate limited to 1 request per second for a user. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#nowa-wiadomosc" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#add-a-new-message" target="_blank">EN</a>.


    HTTP: ``POST /messaging/messages``
    """
    return call_operation(
        "newMessagePOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def list_messages_get(
    *,
    threadId: Annotated[
        str, Field(json_schema_extra=input_schema("listMessagesGET", "path:threadId", "threadId"))
    ],
    limit: Annotated[
        int | None, Field(json_schema_extra=input_schema("listMessagesGET", "query:limit", "limit"))
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("listMessagesGET", "query:offset", "offset")),
    ] = None,
    before: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("listMessagesGET", "query:before", "before")),
    ] = None,
    after: Annotated[
        str | None, Field(json_schema_extra=input_schema("listMessagesGET", "query:after", "after"))
    ] = None,
    page_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("listMessagesGET", "query:page.id", "page_id")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "listMessagesGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """List messages in thread

    Use this resource to list messages in thread with provided identifier. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#lista-wiadomosci-dla-wybranego-watku" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#list-of-the-messages-for-the-particular-thread" target="_blank">EN</a>.


    HTTP: ``GET /messaging/threads/{threadId}/messages``
    """
    return call_operation(
        "listMessagesGET",
        {
            "path:threadId": threadId,
            "query:limit": limit,
            "query:offset": offset,
            "query:before": before,
            "query:after": after,
            "query:page.id": page_id,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def new_message_in_thread_post(
    *,
    threadId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("newMessageInThreadPOST", "path:threadId", "threadId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "newMessageInThreadPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("newMessageInThreadPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Write a new message in thread

    Use this resource to write new message in existing thread. This resource is rate limited to 1 request per second for a user. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#nowa-wiadomosc" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#add-a-new-message" target="_blank">EN</a>.


    HTTP: ``POST /messaging/threads/{threadId}/messages``
    """
    return call_operation(
        "newMessageInThreadPOST",
        {"path:threadId": threadId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_message_get(
    *,
    messageId: Annotated[
        str, Field(json_schema_extra=input_schema("getMessageGET", "path:messageId", "messageId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getMessageGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get single message

    Use this resource to get message with provided identifier. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#szczegolowe-informacje-o-wiadomosci" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#information-about-a-particular-message" target="_blank">EN</a>.


    HTTP: ``GET /messaging/messages/{messageId}``
    """
    return call_operation(
        "getMessageGET", {"path:messageId": messageId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_message_delete(
    *,
    messageId: Annotated[
        str,
        Field(json_schema_extra=input_schema("deleteMessageDELETE", "path:messageId", "messageId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteMessageDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete single message

    Use this resource to delete message with provided identifier. This resource is deprecated and will be removed in the future. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#usuniecie-wiadomosci" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#delete-a-message" target="_blank">EN</a>.


    HTTP: ``DELETE /messaging/messages/{messageId}``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation(
        "deleteMessageDELETE",
        {"path:messageId": messageId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def new_attachment_declaration_post(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "newAttachmentDeclarationPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("newAttachmentDeclarationPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Add attachment declaration

    Use this resource to add attachment declaration before uploading. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#deklaracja-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#attachment-declaration" target="_blank">EN</a>.


    HTTP: ``POST /messaging/message-attachments``
    """
    return call_operation(
        "newAttachmentDeclarationPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_attachment_put(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "uploadAttachmentPUT", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadAttachmentPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    content_base64: str,
    content_type: str = "image/png",
) -> Any | ErrorResponse:
    """Upload attachment binary data

    Use this resource to upload attachment using identifier that was declared. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#dodanie-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#add-an-attachment" target="_blank">EN</a>.


    HTTP: ``PUT /messaging/message-attachments/{attachmentId}``
    """
    return call_operation(
        "uploadAttachmentPUT",
        {
            "path:attachmentId": attachmentId,
            "header:Accept-Language": Accept_Language,
            "content_base64": content_base64,
            "content_type": content_type,
        },
    )


@mcp.tool
@allegro_call
def download_attachment_get(
    *,
    attachmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "downloadAttachmentGET", "path:attachmentId", "attachmentId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "downloadAttachmentGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Download attachment

    Use this resource to download attachment with provided identifier. You can retrieve attachments uploaded within the last 6 months. Read more: <a href="../../tutorials/jak-zarzadzac-centrum-wiadomosci-XxWm2K890Fk#pobranie-zalacznika" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-the-message-center-g05avyGlZUW#attachment-related-to-the-message" target="_blank">EN</a>.


    HTTP: ``GET /messaging/message-attachments/{attachmentId}``
    """
    return call_operation(
        "downloadAttachmentGET",
        {"path:attachmentId": attachmentId, "header:Accept-Language": Accept_Language},
    )
