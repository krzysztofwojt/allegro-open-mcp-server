# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Order management
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
def get_order_events(
    *,
    from_: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getOrderEventsUsingGET", "query:from", "from_")),
    ] = None,
    type_: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getOrderEventsUsingGET", "query:type", "type_")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getOrderEventsUsingGET", "query:limit", "limit")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrderEventsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get order events

    Use this resource to return events that allow you to monitor actions which clients perform, i.e. making a purchase, filling in the checkout form (FOD), finishing payment process, making a surcharge. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#dziennik-zdarzen" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#event-log" target="_blank">EN</a>.


    HTTP: ``GET /order/events``
    """
    return call_operation(
        "getOrderEventsUsingGET",
        {
            "query:from": from_,
            "query:type": type_,
            "query:limit": limit,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_order_events_statistics(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrderEventsStatisticsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get order events statistics

    Use this resource to returns object that contains event id and occurrence date of the latest event. It gives you current starting point for reading events. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-znalezc-najnowsze-zdarzenie" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-find-the-newest-event" target="_blank">EN</a>.


    HTTP: ``GET /order/event-stats``
    """
    return call_operation(
        "getOrderEventsStatisticsUsingGET", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_list_of_orders(
    *,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getListOfOrdersUsingGET", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getListOfOrdersUsingGET", "query:limit", "limit")),
    ] = None,
    status: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getListOfOrdersUsingGET", "query:status", "status")),
    ] = None,
    fulfillment_status: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:fulfillment.status", "fulfillment_status"
            )
        ),
    ] = None,
    fulfillment_provider_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET",
                "query:fulfillment.provider.id",
                "fulfillment_provider_id",
            )
        ),
    ] = None,
    fulfillment_shipmentSummary_lineItemsSent: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET",
                "query:fulfillment.shipmentSummary.lineItemsSent",
                "fulfillment_shipmentSummary_lineItemsSent",
            )
        ),
    ] = None,
    lineItems_boughtAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:lineItems.boughtAt.lte", "lineItems_boughtAt_lte"
            )
        ),
    ] = None,
    lineItems_boughtAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:lineItems.boughtAt.gte", "lineItems_boughtAt_gte"
            )
        ),
    ] = None,
    payment_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:payment.id", "payment_id"
            )
        ),
    ] = None,
    surcharges_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:surcharges.id", "surcharges_id"
            )
        ),
    ] = None,
    delivery_method_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:delivery.method.id", "delivery_method_id"
            )
        ),
    ] = None,
    buyer_login: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:buyer.login", "buyer_login"
            )
        ),
    ] = None,
    marketplace_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:marketplace.id", "marketplace_id"
            )
        ),
    ] = None,
    updatedAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:updatedAt.lte", "updatedAt_lte"
            )
        ),
    ] = None,
    updatedAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "query:updatedAt.gte", "updatedAt_gte"
            )
        ),
    ] = None,
    sort: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getListOfOrdersUsingGET", "query:sort", "sort")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfOrdersUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's orders

    Use this resource to get an order list. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#lista-zamowien" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#order-list" target="_blank">EN</a>.


    HTTP: ``GET /order/checkout-forms``
    """
    return call_operation(
        "getListOfOrdersUsingGET",
        {
            "query:offset": offset,
            "query:limit": limit,
            "query:status": status,
            "query:fulfillment.status": fulfillment_status,
            "query:fulfillment.provider.id": fulfillment_provider_id,
            "query:fulfillment.shipmentSummary.lineItemsSent": fulfillment_shipmentSummary_lineItemsSent,
            "query:lineItems.boughtAt.lte": lineItems_boughtAt_lte,
            "query:lineItems.boughtAt.gte": lineItems_boughtAt_gte,
            "query:payment.id": payment_id,
            "query:surcharges.id": surcharges_id,
            "query:delivery.method.id": delivery_method_id,
            "query:buyer.login": buyer_login,
            "query:marketplace.id": marketplace_id,
            "query:updatedAt.lte": updatedAt_lte,
            "query:updatedAt.gte": updatedAt_gte,
            "query:sort": sort,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_orders_details(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getOrdersDetailsUsingGET", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrdersDetailsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get an order's details

    Use this resource to get an order details. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#szczegoly-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#order-details" target="_blank">EN</a>.


    HTTP: ``GET /order/checkout-forms/{id}``
    """
    return call_operation(
        "getOrdersDetailsUsingGET", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
def get_orders_carriers(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrdersCarriersUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of available shipping carriers

    Shipping carriers are essential to provide accurate tracking experience for customers. Use this resource to get a list of all available shipping carriers. This resource is rate limited to 50 requests per second. The response of this resource can be stored in accordance with returned caching headers. Read more: <a href="../../news/nowy-zasob-do-pobrania-identyfikatorow-przewoznikow-8dmljjGRGUE" target="_blank">PL</a> / <a href="../../news/new-resource-to-retrieve-available-delivery-company-id-VL6zDDdr4hk" target="_blank">EN</a>.


    HTTP: ``GET /order/carriers``
    """
    return call_operation("getOrdersCarriersUsingGET", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
def get_order_shipments(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getOrderShipmentsUsingGET", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrderShipmentsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a list of parcel tracking numbers

    Get a list of parcel tracking numbers currently assigned to the order. Orders can be retrieved using REST API resource GET /order/checkout-forms. Please note that the shipment list may contain parcel tracking numbers added through other channels such as Moje Allegro or by the carrier that delivers the parcel. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-numery-przesylek-dodane-do-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#retrieving-tracking-numbers" target="_blank">EN</a>. This resource is rate limited to 50 requests per second.


    HTTP: ``GET /order/checkout-forms/{id}/shipments``
    """
    return call_operation(
        "getOrderShipmentsUsingGET", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_order_shipments(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("createOrderShipmentsUsingPOST", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createOrderShipmentsUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("createOrderShipmentsUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Add a parcel tracking number

    Add a parcel tracking number (shipment) to given order line items. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-dodac-numer-przesylki-do-przedmiotu-w-zamowieniu" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#add-tracking-number-to-order" target="_blank">EN</a>. This resource is rate limited to 50 requests per second.


    HTTP: ``POST /order/checkout-forms/{id}/shipments``
    """
    return call_operation(
        "createOrderShipmentsUsingPOST",
        {"path:id": id, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def set_order_fulfillment(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("setOrderFulfillmentUsingPUT", "path:id", "id"))
    ],
    checkoutForm_revision: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "setOrderFulfillmentUsingPUT",
                "query:checkoutForm.revision",
                "checkoutForm_revision",
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "setOrderFulfillmentUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("setOrderFulfillmentUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Set seller order status

    Use to set seller order status. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#zmiana-statusu-realizacji-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#order-fulfillment-status-change" target="_blank">EN</a>.


    HTTP: ``PUT /order/checkout-forms/{id}/fulfillment``
    """
    return call_operation(
        "setOrderFulfillmentUsingPUT",
        {
            "path:id": id,
            "query:checkoutForm.revision": checkoutForm_revision,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def set_order_line_items_serial_numbers(
    *,
    id: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "setOrderLineItemsSerialNumbersUsingPOST", "path:id", "id"
            )
        ),
    ],
    checkoutForm_revision: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "setOrderLineItemsSerialNumbersUsingPOST",
                "query:checkoutForm.revision",
                "checkoutForm_revision",
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "setOrderLineItemsSerialNumbersUsingPOST",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None,
        Field(
            json_schema_extra=input_schema(
                "setOrderLineItemsSerialNumbersUsingPOST", "body", "body"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Set line items' serial numbers

    Use to set serial numbers in the given line items of seller order. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#zmiana-statusu-realizacji-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#order-fulfillment-status-change" target="_blank">EN</a>.


    HTTP: ``POST /order/checkout-forms/{id}/serial-numbers``
    """
    return call_operation(
        "setOrderLineItemsSerialNumbersUsingPOST",
        {
            "path:id": id,
            "query:checkoutForm.revision": checkoutForm_revision,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
def get_order_invoices_details(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("getOrderInvoicesDetails", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getOrderInvoicesDetails", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get order invoices details

    Use to get invoices details including antivirus scan results and EPT invoice verification status. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-pobrac-informacje-o-dokumentach-rozliczeniowych-dodanych-do-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-download-information-about-billing-documents-added-to-orders" target="_blank">EN</a>.


    HTTP: ``GET /order/checkout-forms/{id}/invoices``
    """
    return call_operation(
        "getOrderInvoicesDetails", {"path:id": id, "header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def add_order_invoices_metadata(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("addOrderInvoicesMetadata", "path:id", "id"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "addOrderInvoicesMetadata", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("addOrderInvoicesMetadata", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Post new invoice

    Use to add new invoice metadata. Before you send an invoice file, you need to initialize the invoice instance with the required parameters. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-dodac-fakture-do-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#how-to-add-an-invoice-to-orders" target="_blank">EN</a>.


    HTTP: ``POST /order/checkout-forms/{id}/invoices``
    """
    return call_operation(
        "addOrderInvoicesMetadata",
        {"path:id": id, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_order_invoice_file(
    *,
    id: Annotated[
        str, Field(json_schema_extra=input_schema("uploadOrderInvoiceFile", "path:id", "id"))
    ],
    invoiceId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("uploadOrderInvoiceFile", "path:invoiceId", "invoiceId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadOrderInvoiceFile", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    content_base64: str,
    content_type: str = "application/pdf",
) -> Any | ErrorResponse:
    """Upload invoice file

    Use to upload invoice file to match created invoice metadata. Read more: <a href="../../tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR#jak-dodac-fakture-do-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/process-orders-PgPMlWDr8Cv#add-an-invoice-to-the-order" target="_blank">EN</a>.


    HTTP: ``PUT /order/checkout-forms/{id}/invoices/{invoiceId}/file``
    """
    return call_operation(
        "uploadOrderInvoiceFile",
        {
            "path:id": id,
            "path:invoiceId": invoiceId,
            "header:Accept-Language": Accept_Language,
            "content_base64": content_base64,
            "content_type": content_type,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def upload_order_billing_document_link(
    *,
    orderId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "uploadOrderBillingDocumentLink", "path:orderId", "orderId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "uploadOrderBillingDocumentLink", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any] | None,
        Field(json_schema_extra=input_schema("uploadOrderBillingDocumentLink", "body", "body")),
    ] = None,
) -> Any | ErrorResponse:
    """Upload URL to billing documents

    Used to upload a URL to a billing document. You can add up to 10 links.


    HTTP: ``POST /order/{orderId}/billing-documents/links``
    """
    return call_operation(
        "uploadOrderBillingDocumentLink",
        {"path:orderId": orderId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_allegro_pickup_drop_off_points_get(
    *,
    carriers: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getAllegroPickupDropOffPointsGET", "query:carriers", "carriers"
            )
        ),
    ] = None,
    If_Modified_Since: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAllegroPickupDropOffPointsGET", "header:If-Modified-Since", "If_Modified_Since"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAllegroPickupDropOffPointsGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get Allegro pickup drop off points

    Get a list of Allegro pickup drop off points. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-liste-punktow-allegro" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-list-of-allegro-pickup-drop-off-points" target="_blank">EN</a>.


    HTTP: ``GET /order/carriers/ALLEGRO/points``
    """
    return call_operation(
        "getAllegroPickupDropOffPointsGET",
        {
            "query:carriers": carriers,
            "header:If-Modified-Since": If_Modified_Since,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_parcel_tracking(
    *,
    carrierId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getParcelTrackingUsingGET", "path:carrierId", "carrierId"
            )
        ),
    ],
    waybill: Annotated[
        list[str],
        Field(
            json_schema_extra=input_schema("getParcelTrackingUsingGET", "query:waybill", "waybill")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getParcelTrackingUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get carrier parcel tracking history

    Get tracking history for parcels. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-historie-statusow-przesylek" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-parcels-statuses-history" target="_blank">EN</a>.


    HTTP: ``GET /order/carriers/{carrierId}/tracking``
    """
    return call_operation(
        "getParcelTrackingUsingGET",
        {
            "path:carrierId": carrierId,
            "query:waybill": waybill,
            "header:Accept-Language": Accept_Language,
        },
    )
