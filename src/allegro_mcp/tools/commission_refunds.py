# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Commission refunds
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
def get_refund_application(
    *,
    claimId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getRefundApplication", "path:claimId", "claimId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundApplication", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a refund application details

    Use this resource to get refund application details. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-pojedynczy-wniosek-o-rabat-transakcyjny" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-retrieve-single-sale-commission-refund" target="_blank">EN</a>.


    HTTP: ``GET /order/refund-claims/{claimId}``
    """
    return call_operation(
        "getRefundApplication", {"path:claimId": claimId, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def cancel_refund_application(
    *,
    claimId: Annotated[
        str,
        Field(json_schema_extra=input_schema("cancelRefundApplication", "path:claimId", "claimId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "cancelRefundApplication", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Cancel a refund application

    Use this resource to cancel a refund application. This cannot be undone. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-anulowac-wniosek-o-rabat-transakcyjny" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-cancel-sale-commission-refund" target="_blank">EN</a>.


    HTTP: ``DELETE /order/refund-claims/{claimId}``
    """
    return call_operation(
        "cancelRefundApplication",
        {"path:claimId": claimId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_refund_applications(
    *,
    lineItem_offer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundApplications", "query:lineItem.offer.id", "lineItem_offer_id"
            )
        ),
    ] = None,
    buyer_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getRefundApplications", "query:buyer.id", "buyer_id")
        ),
    ] = None,
    status: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getRefundApplications", "query:status", "status")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getRefundApplications", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getRefundApplications", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundApplications", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of refund applications

    Use this resource to get a list of refund applications based on the provided query parameters. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-liste-utworzonych-wnioskow-o-rabat-transakcyjny" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-retrieve-list-of-sale-commission-refunds" target="_blank">EN</a>.


    HTTP: ``GET /order/refund-claims``
    """
    return call_operation(
        "getRefundApplications",
        {
            "query:lineItem.offer.id": lineItem_offer_id,
            "query:buyer.id": buyer_id,
            "query:status": status,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_refund_application(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createRefundApplication", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createRefundApplication", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Create a refund application

    Use this resource to create a refund application. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-utworzyc-wniosek-o-rabat-transakcyjny" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-create-a-sale-commission-refund-application" target="_blank">EN</a>.


    HTTP: ``POST /order/refund-claims``
    """
    return call_operation(
        "createRefundApplication", {"header:Accept-Language": Accept_Language, "body": body}
    )
