# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Additional services translations
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
def get_additional_service_group_translations(
    *,
    groupId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "getAdditionalServiceGroupTranslations", "path:groupId", "groupId"
            )
        ),
    ],
    language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdditionalServiceGroupTranslations", "query:language", "language"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdditionalServiceGroupTranslations", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get translations for specified group

    Use this resource to get translations for additional service group. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-uslug-dodatkowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#additional-services-translations" target="_blank">EN</a>.


    HTTP: ``GET /sale/offer-additional-services/groups/{groupId}/translations``
    """
    return call_operation(
        "getAdditionalServiceGroupTranslations",
        {
            "path:groupId": groupId,
            "query:language": language,
            "header:Accept-Language": Accept_Language,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def update_additional_service_group_translation(
    *,
    groupId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAdditionalServiceGroupTranslation", "path:groupId", "groupId"
            )
        ),
    ],
    language: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "updateAdditionalServiceGroupTranslation", "path:language", "language"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "updateAdditionalServiceGroupTranslation",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(
            json_schema_extra=input_schema(
                "updateAdditionalServiceGroupTranslation", "body", "body"
            )
        ),
    ],
) -> Any | ErrorResponse:
    """Create/Update translations for specified group and language

    Use this resource to create/update translation for additional service group and specified language. It is allowed to provide an incomplete list of services that belong to the group. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-uslug-dodatkowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#additional-services-translations" target="_blank">EN</a>.


    HTTP: ``PATCH /sale/offer-additional-services/groups/{groupId}/translations/{language}``
    """
    return call_operation(
        "updateAdditionalServiceGroupTranslation",
        {
            "path:groupId": groupId,
            "path:language": language,
            "header:Accept-Language": Accept_Language,
            "body": body,
        },
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_additional_service_group_translation(
    *,
    groupId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteAdditionalServiceGroupTranslation", "path:groupId", "groupId"
            )
        ),
    ],
    language: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteAdditionalServiceGroupTranslation", "path:language", "language"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteAdditionalServiceGroupTranslation",
                "header:Accept-Language",
                "Accept_Language",
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete a translation for a specified group and language

    Use this resource to delete the translation for specified additional service group and language. Read more: <a href="../../tutorials/jak-zarzadzac-ofertami-7GzB2L37ase#tlumaczenia-uslug-dodatkowych" target="_blank">PL</a> / <a href="../../tutorials/how-to-process-list-of-offers-m09BKA5v8H3#additional-services-translations" target="_blank">EN</a>.


    HTTP: ``DELETE /sale/offer-additional-services/groups/{groupId}/translations/{language}``
    """
    return call_operation(
        "deleteAdditionalServiceGroupTranslation",
        {
            "path:groupId": groupId,
            "path:language": language,
            "header:Accept-Language": Accept_Language,
        },
    )
