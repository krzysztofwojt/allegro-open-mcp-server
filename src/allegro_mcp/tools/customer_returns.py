# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Customer returns
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
def get_customer_returns(
    *,
    customerReturnId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:customerReturnId", "customerReturnId"
            )
        ),
    ] = None,
    orderId: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCustomerReturns", "query:orderId", "orderId")),
    ] = None,
    buyer_email: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getCustomerReturns", "query:buyer.email", "buyer_email")
        ),
    ] = None,
    buyer_login: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getCustomerReturns", "query:buyer.login", "buyer_login")
        ),
    ] = None,
    items_offerId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:items.offerId", "items_offerId"
            )
        ),
    ] = None,
    items_name: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getCustomerReturns", "query:items.name", "items_name")
        ),
    ] = None,
    parcels_waybill: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:parcels.waybill", "parcels_waybill"
            )
        ),
    ] = None,
    parcels_transportingWaybill: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns",
                "query:parcels.transportingWaybill",
                "parcels_transportingWaybill",
            )
        ),
    ] = None,
    parcels_carrierId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:parcels.carrierId", "parcels_carrierId"
            )
        ),
    ] = None,
    parcels_transportingCarrierId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns",
                "query:parcels.transportingCarrierId",
                "parcels_transportingCarrierId",
            )
        ),
    ] = None,
    parcels_sender_phoneNumber: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns",
                "query:parcels.sender.phoneNumber",
                "parcels_sender_phoneNumber",
            )
        ),
    ] = None,
    referenceNumber: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:referenceNumber", "referenceNumber"
            )
        ),
    ] = None,
    from_: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCustomerReturns", "query:from", "from_")),
    ] = None,
    createdAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:createdAt.gte", "createdAt_gte"
            )
        ),
    ] = None,
    createdAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:createdAt.lte", "createdAt_lte"
            )
        ),
    ] = None,
    marketplaceId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    status: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCustomerReturns", "query:status", "status")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCustomerReturns", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getCustomerReturns", "query:offset", "offset")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturns", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """[BETA] Get customer returns by provided query parameters

    Use this resource to get all customer returns filtered by query parameters. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-liste-zwrotow" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-retrieve-customer-returns-list" target="_blank">EN</a>. This resource is limited to 25 requests per second for a single user and 50 requests per second for clientId.


    HTTP: ``GET /order/customer-returns``
    """
    return call_operation(
        "getCustomerReturns",
        {
            "query:customerReturnId": customerReturnId,
            "query:orderId": orderId,
            "query:buyer.email": buyer_email,
            "query:buyer.login": buyer_login,
            "query:items.offerId": items_offerId,
            "query:items.name": items_name,
            "query:parcels.waybill": parcels_waybill,
            "query:parcels.transportingWaybill": parcels_transportingWaybill,
            "query:parcels.carrierId": parcels_carrierId,
            "query:parcels.transportingCarrierId": parcels_transportingCarrierId,
            "query:parcels.sender.phoneNumber": parcels_sender_phoneNumber,
            "query:referenceNumber": referenceNumber,
            "query:from": from_,
            "query:createdAt.gte": createdAt_gte,
            "query:createdAt.lte": createdAt_lte,
            "query:marketplaceId": marketplaceId,
            "query:status": status,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_customer_return_by_id(
    *,
    customerReturnId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturnById", "path:customerReturnId", "customerReturnId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCustomerReturnById", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """[BETA] Get customer return by id

    Use this resource to get customer returns by its identifier. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-szczegolowe-informacje-o-zwrocie" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-retrieve-detailed-information-about-customer-return" target="_blank">EN</a>.


    HTTP: ``GET /order/customer-returns/{customerReturnId}``
    """
    return call_operation(
        "getCustomerReturnById",
        {"path:customerReturnId": customerReturnId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def reject_customer_return_refund(
    *,
    customerReturnId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "rejectCustomerReturnRefund", "path:customerReturnId", "customerReturnId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "rejectCustomerReturnRefund", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("rejectCustomerReturnRefund", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """[BETA] Reject customer return refund

    Use this resource to reject customer return refund with provided reason. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-odmowic-zwrotu-wplaty" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-reject-customer-return-refund" target="_blank">EN</a>.


    HTTP: ``POST /order/customer-returns/{customerReturnId}/rejection``
    """
    return call_operation(
        "rejectCustomerReturnRefund",
        {
            "path:customerReturnId": customerReturnId,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )
