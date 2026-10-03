# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Payments
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
def get_payments_operation_history(
    *,
    wallet_type: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:wallet.type", "wallet_type"
            )
        ),
    ] = None,
    wallet_paymentOperator: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory",
                "query:wallet.paymentOperator",
                "wallet_paymentOperator",
            )
        ),
    ] = None,
    payment_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:payment.id", "payment_id"
            )
        ),
    ] = None,
    participant_login: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:participant.login", "participant_login"
            )
        ),
    ] = None,
    occurredAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:occurredAt.gte", "occurredAt_gte"
            )
        ),
    ] = None,
    occurredAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:occurredAt.lte", "occurredAt_lte"
            )
        ),
    ] = None,
    group: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema("getPaymentsOperationHistory", "query:group", "group")
        ),
    ] = None,
    marketplaceId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    currency: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "query:currency", "currency"
            )
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getPaymentsOperationHistory", "query:limit", "limit")
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getPaymentsOperationHistory", "query:offset", "offset")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPaymentsOperationHistory", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Payment operations history

    Use this endpoint to get the list of the seller payment operations. Read more: <a href="../../tutorials/jak-sprawdzic-oplaty-nn9DOL5PASX#historia-operacji-platniczych" target="_blank">PL</a> / <a href="../../tutorials/how-to-check-the-fees-3An6Wame3Um#payment-operations" target="_blank">EN</a>.


    HTTP: ``GET /payments/payment-operations``
    """
    return call_operation(
        "getPaymentsOperationHistory",
        {
            "query:wallet.type": wallet_type,
            "query:wallet.paymentOperator": wallet_paymentOperator,
            "query:payment.id": payment_id,
            "query:participant.login": participant_login,
            "query:occurredAt.gte": occurredAt_gte,
            "query:occurredAt.lte": occurredAt_lte,
            "query:group": group,
            "query:marketplaceId": marketplaceId,
            "query:currency": currency,
            "query:limit": limit,
            "query:offset": offset,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def initiate_refund(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "initiateRefund", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None,
        Field(json_schema_extra=input_schema("initiateRefund", "body", "body")),
    ] = None,
) -> Any | ErrorResponse:
    """Initiate a refund of a payment

    Use this endpoint to initiate a refund of a payment. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-wykonac-zwrot-platnosci" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-refund-a-payment" target="_blank">EN</a>.


    HTTP: ``POST /payments/refunds``
    """
    return call_operation(
        "initiateRefund", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_refunded_payments(
    *,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getRefundedPayments", "query:limit", "limit")),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getRefundedPayments", "query:offset", "offset")),
    ] = None,
    id: Annotated[
        str | None, Field(json_schema_extra=input_schema("getRefundedPayments", "query:id", "id"))
    ] = None,
    payment_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getRefundedPayments", "query:payment.id", "payment_id")
        ),
    ] = None,
    order_id: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getRefundedPayments", "query:order.id", "order_id")),
    ] = None,
    occurredAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundedPayments", "query:occurredAt.gte", "occurredAt_gte"
            )
        ),
    ] = None,
    occurredAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundedPayments", "query:occurredAt.lte", "occurredAt_lte"
            )
        ),
    ] = None,
    status: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getRefundedPayments", "query:status", "status")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getRefundedPayments", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of refunded payments

    Get a list of refunded payments. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-liste-zwrotow-platnosci" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-retrieve-a-list-of-refunded-payment" target="_blank">EN</a>.


    HTTP: ``GET /payments/refunds``
    """
    return call_operation(
        "getRefundedPayments",
        {
            "query:limit": limit,
            "query:offset": offset,
            "query:id": id,
            "query:payment.id": payment_id,
            "query:order.id": order_id,
            "query:occurredAt.gte": occurredAt_gte,
            "query:occurredAt.lte": occurredAt_lte,
            "query:status": status,
            "header:Accept-Language": Accept_Language,
        },
    )
