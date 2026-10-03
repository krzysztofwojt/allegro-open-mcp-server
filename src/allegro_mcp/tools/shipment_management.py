# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Shipment management
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
def get_delivery_proposals(
    *,
    orderId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getDeliveryProposals", "path:orderId", "orderId")),
    ],
) -> Any | ErrorResponse:
    """Get available delivery options

    Use this resource to retrieve two order characteristics. The first is a pre-populated request body for creating a shipment in SwA. The second is a list of possible delivery types for processing the order, including their limits. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-proponowane-dane-i-ustawienia-dostawy-dla-zamowienia" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-the-proposed-delivery-details-and-settings-for-an-order" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/delivery-proposals/{orderId}``
    """
    return call_operation("getDeliveryProposals", {"path:orderId": orderId})


@mcp.tool
@allegro_call
def get_delivery_services(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getDeliveryServices", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get available delivery services

    Use this resource to get delivery services available for user. It returns services provided by Allegro and contracts with carriers owned by user and configured by GUI. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-liste-uslug-dostawy" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-a-list-of-delivery-services" target="_blank">EN</a>.<br/> This resource is deprecated and will be removed in Q1 2027. Consider using the new resource '/shipment-management/delivery-proposals/{orderId}' resource instead.


    HTTP: ``GET /shipment-management/delivery-services``

    DEPRECATED by Allegro; prefer the documented replacement.
    """
    return call_operation("getDeliveryServices", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_new_shipment(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createNewShipment", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("createNewShipment", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Create new shipment

    Use this resource to create shipment for delivery. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-utworzyc-nowa-paczke" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-create-a-new-shipment" target="_blank">EN</a>. Please check also new resource '/shipment-management/delivery-proposals/{orderId}' to get prefilled request body for this resource.


    HTTP: ``POST /shipment-management/shipments/create-commands``
    """
    return call_operation(
        "createNewShipment", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_shipment_creation_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getShipmentCreationStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShipmentCreationStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get shipment creation command status

    Use this resource to get shipment creation status. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-sprawdzic-status-utworzenia-paczki" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-check-the-creation-status-of-a-shipment" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/shipments/create-commands/{commandId}``
    """
    return call_operation(
        "getShipmentCreationStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def cancel_shipment(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "cancelShipment", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("cancelShipment", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Cancel shipment

    Use this resource to cancel parcel. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-anulowac-paczke" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-cancel-a-shipment" target="_blank">EN</a>.


    HTTP: ``POST /shipment-management/shipments/cancel-commands``
    """
    return call_operation(
        "cancelShipment", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_shipment_cancellation_status(
    *,
    commandId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getShipmentCancellationStatus", "path:commandId", "commandId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShipmentCancellationStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get shipment cancellation status

    Use this resource to get parcel cancellation status. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-sprawdzic-status-anulowania-paczki" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-check-shipment-cancellation-status" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/shipments/cancel-commands/{commandId}``
    """
    return call_operation(
        "getShipmentCancellationStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_shipment_details(
    *,
    shipmentId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getShipmentDetails", "path:shipmentId", "shipmentId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShipmentDetails", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get shipment details

    Use this resource to get parcel details. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-szczegolowe-informacje-o-paczce" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-shipment-details" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/shipments/{shipmentId}``
    """
    return call_operation(
        "getShipmentDetails",
        {"path:shipmentId": shipmentId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_shipment_labels(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShipmentLabels", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("getShipmentLabels", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Get shipments labels

    Use this resource to get label for created shipment. <br/>Returned content type depends on created shipment. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-utworzyc-etykiete-na-paczke" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-create-a-label-for-shipment" target="_blank">EN</a>.


    HTTP: ``POST /shipment-management/label``
    """
    return call_operation(
        "getShipmentLabels", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_shipment_protocol(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getShipmentProtocol", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("getShipmentProtocol", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Get shipments protocol

    Protocol availability depends on Carrier. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-pobrac-protokol-nadania-przesylek" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-retrieve-shipment-protocol" target="_blank">EN</a>.


    HTTP: ``POST /shipment-management/protocol``
    """
    return call_operation(
        "getShipmentProtocol", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def get_pickup_proposals(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPickupProposals", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("getPickupProposals", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Get shipments pickup proposals

    Use this resource to get parcels pickup date proposals. Pickup takes place, when courier arrives to take parcels for shipment. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-sprawdzic-proponowana-date-odbioru-paczek-przez-kuriera" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-check-pickup-date-proposals" target="_blank">EN</a>.


    HTTP: ``POST /shipment-management/pickup-proposals``
    """
    return call_operation(
        "getPickupProposals", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_pickup(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createPickup", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any], Field(json_schema_extra=input_schema("createPickup", "body", "body"))
    ],
) -> Any | ErrorResponse:
    """Request shipments pickup

    Use this resource to request a pickup of shipments. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-zamowic-odbior-paczek-przez-kuriera" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-request-shipment-pickup-by-a-courier" target="_blank">EN</a>.


    HTTP: ``POST /shipment-management/pickups/create-commands``
    """
    return call_operation("createPickup", {"header:Accept-Language": Accept_Language, "body": body})


@mcp.tool
@allegro_call
def create_pickup_status(
    *,
    commandId: Annotated[
        str,
        Field(json_schema_extra=input_schema("createPickupStatus", "path:commandId", "commandId")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createPickupStatus", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Create pickup command status

    Use this resource to get pickup request status. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-sprawdzic-status-zamowienia-odbioru-paczek" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-check-shipment-pickup-request-status" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/pickups/create-commands/{commandId}``
    """
    return call_operation(
        "createPickupStatus",
        {"path:commandId": commandId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_pickup_details(
    *,
    pickupId: Annotated[
        str, Field(json_schema_extra=input_schema("getPickupDetails", "path:pickupId", "pickupId"))
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getPickupDetails", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get pickup details

    Use this resource to get pickup details. Read more: <a href="../../tutorials/jak-zarzadzac-przesylkami-przez-wysylam-z-allegro-LRVjK7K21sY#jak-sprawdzic-status-zamowienia-odbioru-paczek" target="_blank">PL</a> / <a href="../../tutorials/how-to-manage-parcels-via-ship-with-allegro-ZM9YAyGKWTV#how-to-check-shipment-pickup-request-status" target="_blank">EN</a>.


    HTTP: ``GET /shipment-management/pickups/{pickupId}``
    """
    return call_operation(
        "getPickupDetails", {"path:pickupId": pickupId, "header:Accept-Language": Accept_Language}
    )
