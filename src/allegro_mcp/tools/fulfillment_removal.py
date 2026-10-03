# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Fulfillment Removal
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
def get_fulfillment_removal_preferences(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFulfillmentRemovalPreferences", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get current active removal preference

    Use this resource to read your current removal preference. Removal preference is associated with system removal order at the moment of removal order is created. It means there can be not yet fulfilled removal orders associated with previously set removal preference. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#pobierz-aktualne-ustawienia-sposobu-usuniecia-towaru-z-magazynu" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#retrieve-current-settings-for-how-to-remove-goods-from-the-warehouse" target="_blank">EN</a>.


    HTTP: ``GET /fulfillment/removal/preferences``
    """
    return call_operation(
        "getFulfillmentRemovalPreferences", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def create_fulfillment_removal_preferences(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "createFulfillmentRemovalPreferences", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema("createFulfillmentRemovalPreferences", "body", "body")
        ),
    ],
) -> Any | ErrorResponse:
    """Create new active Fulfillment Removal Preference

    Use this resource to create new active removal preference. From the moment the preference is set, it becomes the active one, and all new system removal orders will be associated with this preference. Removal preference is associated with system removal order at the moment of removal order is created. It means there can be not yet fulfilled removal orders associated with previously set removal preference. Read more: <a href="../../tutorials/one-fulfillment-by-allegro-0ADwgOLqWSw#utworz-lub-edytuj-ustawienia-sposobu-usuniecia-towaru-z-magazynu" target="_blank">PL</a> / <a href="../../tutorials/one-fulfillment-by-allegro-4R9dXyMPlc9#create-or-edit-settings-for-how-to-remove-goods-from-the-warehouse" target="_blank">EN</a>.


    HTTP: ``PUT /fulfillment/removal/preferences``
    """
    return call_operation(
        "createFulfillmentRemovalPreferences",
        {"header:Accept-Language": Accept_Language, "body": body},
    )
