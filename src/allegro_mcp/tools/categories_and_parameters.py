# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Categories and parameters
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
def get_categories(
    *,
    parent_id: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema("getCategoriesUsingGET", "query:parent.id", "parent_id")
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoriesUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get IDs of Allegro categories

    Use this resource to traverse the Allegro categories tree. It returns the list of the given category's children or a list of the main Allegro categories. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#kategorie-oraz-parametry" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#categories-and-parameters" target="_blank">EN</a>.


    HTTP: ``GET /sale/categories``
    """
    return call_operation(
        "getCategoriesUsingGET",
        {"query:parent.id": parent_id, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_category_using_get_1(
    *,
    categoryId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getCategoryUsingGET_1", "path:categoryId", "categoryId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryUsingGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get a category by ID

    Use this resource to get the details of a specific category. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#jak-utworzyc-nowy-produkt" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#how-to-create-a-product" target="_blank">EN</a>.


    HTTP: ``GET /sale/categories/{categoryId}``
    """
    return call_operation(
        "getCategoryUsingGET_1",
        {"path:categoryId": categoryId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_flat_parameters_using_get_2(
    *,
    categoryId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getFlatParametersUsingGET_2", "path:categoryId", "categoryId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getFlatParametersUsingGET_2", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get parameters supported by a category

    Use this resource to get the list of parameters that are supported by the given category. Read more: <a href="../../tutorials/jak-jednym-requestem-wystawic-oferte-powiazana-z-produktem-D7Kj9gw4xFA#parametry-ofertowe" target="_blank">PL</a> / <a href="../../tutorials/list-offer-assigned-product-one-request-D7Kj9M71Bu6#offer-parameters" target="_blank">EN</a>.


    HTTP: ``GET /sale/categories/{categoryId}/parameters``
    """
    return call_operation(
        "getFlatParametersUsingGET_2",
        {"path:categoryId": categoryId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_category_parameters_scheduled_changes_using_get_1(
    *,
    scheduledFor_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1",
                "query:scheduledFor.gte",
                "scheduledFor_gte",
            )
        ),
    ] = None,
    scheduledFor_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1",
                "query:scheduledFor.lte",
                "scheduledFor_lte",
            )
        ),
    ] = None,
    scheduledAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1",
                "query:scheduledAt.gte",
                "scheduledAt_gte",
            )
        ),
    ] = None,
    scheduledAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1",
                "query:scheduledAt.lte",
                "scheduledAt_lte",
            )
        ),
    ] = None,
    type_: Annotated[
        list[str] | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1", "query:type", "type_"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1", "query:offset", "offset"
            )
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1", "query:limit", "limit"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryParametersScheduledChangesUsingGET_1",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get planned changes in category parameters

    Use this resource to get information about planned changes in category parameters. Please note that in some cases, the returned events may finally not happen in the future. At present we support the following changes: - REQUIREMENT_CHANGE - the parameter will be required in the category. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#jak-sprawdzic-przyszle-zmiany-w-parametrach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#how-to-check-future-changes-in-parameters" target="_blank">EN</a>.


    HTTP: ``GET /sale/category-parameters-scheduled-changes``
    """
    return call_operation(
        "getCategoryParametersScheduledChangesUsingGET_1",
        {
            "query:scheduledFor.gte": scheduledFor_gte,
            "query:scheduledFor.lte": scheduledFor_lte,
            "query:scheduledAt.gte": scheduledAt_gte,
            "query:scheduledAt.lte": scheduledAt_lte,
            "query:type": type_,
            "query:offset": offset,
            "query:limit": limit,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def get_category_events_using_get_1(
    *,
    from_: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("getCategoryEventsUsingGET_1", "query:from", "from_")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(
            json_schema_extra=input_schema("getCategoryEventsUsingGET_1", "query:limit", "limit")
        ),
    ] = None,
    type_: Annotated[
        list[str] | None,
        Field(json_schema_extra=input_schema("getCategoryEventsUsingGET_1", "query:type", "type_")),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getCategoryEventsUsingGET_1", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get changes in categories

    Use this resource to get information about changes in categories. It returns changes that occurred in the last 3 months. At present we support the following changes: - CATEGORY_CREATED - new category was created. - CATEGORY_RENAMED - category name has been changed. - CATEGORY_MOVED - category has been moved to a different place in category tree, category parent id field is changed. - CATEGORY_DELETED - category is no longer available, category from redirectCategory field should be used instead. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#dziennik-zmian-w-kategoriach" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#event-journal-in-categories" target="_blank">EN</a>.


    HTTP: ``GET /sale/category-events``
    """
    return call_operation(
        "getCategoryEventsUsingGET_1",
        {
            "query:from": from_,
            "query:limit": limit,
            "query:type": type_,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
def category_suggestion(
    *,
    name: Annotated[
        str,
        Field(json_schema_extra=input_schema("categorySuggestionUsingGET", "query:name", "name")),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "categorySuggestionUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get categories suggestions

    Use this resource to receive suggested categories for given phrase. This resource is rate limited to 5 requests per second. Read more: <a href="../../news/udostepnilismy-nowy-zasob-dzieki-ktoremu-sprawdzisz-sugerowane-kategorie-dla-podanej-frazy-4RAl9jwX1FW" target="_blank">PL</a> / <a href="../../news/we-have-introduced-a-new-resource-that-allows-you-to-retrieve-the-suggested-categories-for-the-given-phrase-v8Wdy1EOyF0" target="_blank">EN</a>.


    HTTP: ``GET /sale/matching-categories``
    """
    return call_operation(
        "categorySuggestionUsingGET",
        {"query:name": name, "header:Accept-Language": Accept_Language},
    )
