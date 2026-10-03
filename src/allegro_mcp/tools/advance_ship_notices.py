# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Advance Ship Notices
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
def get_advance_ship_notices(
    *,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getAdvanceShipNotices", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getAdvanceShipNotices", "query:limit", "limit")),
    ] = None,
    status: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getAdvanceShipNotices", "query:status", "status")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdvanceShipNotices", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get list of Advance Ship Notices

    Use this resource to get a list of Advance Ship Notices. The list is ordered by **createdAt** property. Default **offset** is 0, default **limit** is 50. A list can be filtered by statuses. Multiple status query parameters are allowed. In such cases, filters are joined with **OR** logical operator. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-przegladac-utworzone-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#how-to-get-created-advance-ship-notices" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/advance-ship-notices``
    """
    return call_operation(
        "getAdvanceShipNotices",
        {
            "query:offset": offset,
            "query:limit": limit,
            "query:status": status,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_advance_ship_notice(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createAdvanceShipNotice", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create an Advance Ship Notice

    Use this resource to create an Advance Ship Notice. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#utworz-draft-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#create-a-draft-of-the-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``POST /fulfillment/advance-ship-notices``
    """
    return call_operation(
        "createAdvanceShipNotice", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_advance_ship_notice(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getAdvanceShipNotice", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get single Advance Ship Notice

    Use this resource to get an Advance Ship Notice. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-przegladac-utworzone-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#how-to-get-created-advance-ship-notices" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/advance-ship-notices/{id}``
    """
    return call_operation(
        "getAdvanceShipNotice", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_advance_ship_notice(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("updateAdvanceShipNotice", "path:id", "id"))
    ],
    if_match: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("updateAdvanceShipNotice", "header:if-match", "if_match")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateAdvanceShipNotice", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update Advance Ship Notice

    Use this resource to update an Advance Ship Notice. Any content property update will clear labels property. Use Create labels command to create new labels for provided content. If a client wants to update read-only property, an error is returned (only in cases when sent value will be different than actual on the server). Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#uzupelnij-dane-o-awizo" target="_blank">PL</a> / <a href="../../one-fulfillment-by-allegro-4R9dXyMPlc9#complete-the-data-of-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/advance-ship-notices/{id}``
    """
    return call_operation(
        "updateAdvanceShipNotice",
        {
            "path:id": id,
            "header:if-match": if_match,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_advance_ship_notice(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("deleteAdvanceShipNotice", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete Advance Ship Notice

    Use this resource to delete an Advance Ship Notice. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#jak-usunac-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#how-to-delete-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``DELETE /fulfillment/advance-ship-notices/{id}``
    """
    return call_operation(
        "deleteAdvanceShipNotice", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def cancel_advance_ship_notice(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("cancelAdvanceShipNotice", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "cancelAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Cancel Advance Ship Notice

    Use this resource to cancel an Advance Ship Notice in IN_TRANSIT status. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#anuluj-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#cancel-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/advance-ship-notices/{id}/cancel``
    """
    return call_operation(
        "cancelAdvanceShipNotice", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_advance_ship_notice_labels(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getAdvanceShipNoticeLabels", "path:id", "id"))
    ],
    accept: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getAdvanceShipNoticeLabels", "header:accept", "accept")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdvanceShipNoticeLabels", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get labels for Advance Ship Notice

    Use this resource to get labels for Advance Ship Notice after being created with "create labels command". Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#wygeneruj-oznaczenia-na-kartony" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#create-labels-for-boxes" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/advance-ship-notices/{id}/labels``
    """
    return call_operation(
        "getAdvanceShipNoticeLabels",
        {"path:id": id, "header:accept": accept, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def submit_command(
    *,
    command_id: Annotated[
        str, Field(json_schema_extra=input_schema("submitCommand", "path:command-id", "command_id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "submitCommand", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("submitCommand", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Submit the Advance Ship Notice

    Use this resource to submit the Advance Ship Notice. After this operation, updates of the Advance Ship Notice are limited to selected properties only. See <a href="../../documentation#operation/updateSubmittedAdvanceShipNotice">PUT /fulfillment/advance-ship-notices/{id}/submitted</a>. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#zakoncz-edycje-i-wyslij-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#finish-editing-and-submit-the-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/submit-commands/{command-id}``
    """
    return call_operation(
        "submitCommand",
        {"path:command-id": command_id, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_submit_command(
    *,
    command_id: Annotated[
        str,
        Field(json_schema_extra=input_schema("getSubmitCommand", "path:command-id", "command_id")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSubmitCommand", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get submit status

    Use this resource to get submit status of the Advance Ship Notice. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#zakoncz-edycje-i-wyslij-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#finish-editing-and-submit-the-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/submit-commands/{command-id}``
    """
    return call_operation(
        "getSubmitCommand",
        {"path:command-id": command_id, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_submitted_advance_ship_notice(
    *,
    id: Annotated[
        str,
        Field(json_schema_extra=input_schema("updateSubmittedAdvanceShipNotice", "path:id", "id")),
    ],
    if_match: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateSubmittedAdvanceShipNotice", "header:if-match", "if_match"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateSubmittedAdvanceShipNotice", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("updateSubmittedAdvanceShipNotice", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Update submitted Advance Ship Notice

    Use this resource to update already submitted Advance Ship Notice. Update is allowed only when Advance Ship Notice is in "IN_TRANSIT" status. Handling unit's amount property update clears labels property. Use Create labels command to create new labels for provided content. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#edytuj-zakonczone-awizo" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#edit-advance-ship-notice" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/advance-ship-notices/{id}/submitted``
    """
    return call_operation(
        "updateSubmittedAdvanceShipNotice",
        {
            "path:id": id,
            "header:if-match": if_match,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
def get_advance_ship_notice_receiving_state(
    *,
    id: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getAdvanceShipNoticeReceivingState", "path:id", "id")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdvanceShipNoticeReceivingState", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Check current state and details of Advance Ship Notice receiving

    Use this resource to check the state of Advance Ship Notice receiving in Fulfillment Center in real time. The response contains a receiving progress and information about particular items - their quantities and conditions. While the Advance Ship Notice is in UNPACKING state, report is updated dynamically, which might result in different responses even at short time intervals. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#sprawdz-postep-odbioru-awizo-przez-magazyn" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#check-current-state-and-details-of-advance-ship-notice-receiving" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/advance-ship-notices/{id}/receiving-state``
    """
    return call_operation(
        "getAdvanceShipNoticeReceivingState",
        {"path:id": id, "header:Accept-Language": Accept_Language},
    )
