# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: Information about user
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
def get_user_ratings(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserRatingsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    recommended: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserRatingsUsingGET", "query:recommended", "recommended"
            )
        ),
    ] = None,
    lastChangedAt_gte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserRatingsUsingGET", "query:lastChangedAt.gte", "lastChangedAt_gte"
            )
        ),
    ] = None,
    lastChangedAt_lte: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserRatingsUsingGET", "query:lastChangedAt.lte", "lastChangedAt_lte"
            )
        ),
    ] = None,
    offset: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getUserRatingsUsingGET", "query:offset", "offset")),
    ] = None,
    limit: Annotated[
        int | None,
        Field(json_schema_extra=input_schema("getUserRatingsUsingGET", "query:limit", "limit")),
    ] = None,
) -> Any | ErrorResponse:
    """Get the user's ratings

    Use this resource to receive your sales ratings sorted by last change date, starting from the latest. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-informacje-o-ocenie-sprzedazy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-user-s-ratings-data" target="_blank">EN</a>.


    HTTP: ``GET /sale/user-ratings``
    """
    return call_operation(
        "getUserRatingsUsingGET",
        {
            "header:Accept-Language": Accept_Language,
            "query:recommended": recommended,
            "query:lastChangedAt.gte": lastChangedAt_gte,
            "query:lastChangedAt.lte": lastChangedAt_lte,
            "query:offset": offset,
            "query:limit": limit,
        },
    )


@mcp.tool
@allegro_call
def get_user_rating(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getUserRatingUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    ratingId: Annotated[
        str,
        Field(json_schema_extra=input_schema("getUserRatingUsingGET", "path:ratingId", "ratingId")),
    ],
) -> Any | ErrorResponse:
    """Get the user's rating by given rating id

    Use this resource to receive your sales rating by given rating id. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-informacje-o-ocenie-sprzedazy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-user-s-ratings-data" target="_blank">EN</a>.


    HTTP: ``GET /sale/user-ratings/{ratingId}``
    """
    return call_operation(
        "getUserRatingUsingGET",
        {"header:Accept-Language": Accept_Language, "path:ratingId": ratingId},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def answer_user_rating(
    *,
    ratingId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("answerUserRatingUsingPUT", "path:ratingId", "ratingId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "answerUserRatingUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("answerUserRatingUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Answer for user's rating

    Use this resource to answer for received rating. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-dodac-odpowiedz-na-ocene" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-answer-for-user-rating" target="_blank">EN</a>.


    HTTP: ``PUT /sale/user-ratings/{ratingId}/answer``
    """
    return call_operation(
        "answerUserRatingUsingPUT",
        {"path:ratingId": ratingId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def user_rating_removal(
    *,
    ratingId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("userRatingRemovalUsingPUT", "path:ratingId", "ratingId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "userRatingRemovalUsingPUT", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("userRatingRemovalUsingPUT", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Request removal of user's rating

    Use this resource to request removal of received rating. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-wyslac-prosbe-o-usuniecie-oceny" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-send-a-request-to-remove-user-rating" target="_blank">EN</a>.


    HTTP: ``PUT /sale/user-ratings/{ratingId}/removal``
    """
    return call_operation(
        "userRatingRemovalUsingPUT",
        {"path:ratingId": ratingId, "header:Accept-Language": Accept_Language, "body": body},
    )


@mcp.tool
@allegro_call
def get_sale_quality(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSaleQualityUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get sales quality

    Use this resource to get current sales quality with at most 30 days history. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jakosc-sprzedazy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#sales-quality" target="_blank">EN</a>.


    HTTP: ``GET /sale/quality``
    """
    return call_operation("getSaleQualityUsingGET", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
def me_get(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(json_schema_extra=input_schema("meGET", "header:Accept-Language", "Accept_Language")),
    ] = None,
) -> Any | ErrorResponse:
    """Get basic information about user

    Use this resource when you need basic information about authenticated user. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#informacje-o-uzytkowniku" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#information-about-user" target="_blank">EN</a>.


    HTTP: ``GET /me``
    """
    return call_operation("meGET", {"header:Accept-Language": Accept_Language})


@mcp.tool
@allegro_call
def get_list_of_additional_emails(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getListOfAdditionalEmailsUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get user's additional emails

    Use this resource to get a list of all additional email addresses assigned to account. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-adresy-e-mail" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-email-addresses" target="_blank">EN</a>.


    HTTP: ``GET /account/additional-emails``
    """
    return call_operation(
        "getListOfAdditionalEmailsUsingGET", {"header:Accept-Language": Accept_Language}
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def add_additional_email(
    *,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "addAdditionalEmailUsingPOST", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
    body: Annotated[
        dict[str, Any],
        Field(json_schema_extra=input_schema("addAdditionalEmailUsingPOST", "body", "body")),
    ],
) -> Any | ErrorResponse:
    """Add a new additional email address to user's account

    Use this resource to add a new additional email address to account. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-dodac-adres-e-mail" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-add-an-additional-email" target="_blank">EN</a>.


    HTTP: ``POST /account/additional-emails``
    """
    return call_operation(
        "addAdditionalEmailUsingPOST", {"header:Accept-Language": Accept_Language, "body": body}
    )


@mcp.tool
@allegro_call
def get_additional_email(
    *,
    emailId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema("getAdditionalEmailUsingGET", "path:emailId", "emailId")
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getAdditionalEmailUsingGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get information about a particular additional email

    Use this resource to retrieve a single additional email. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-pobrac-szczegolowe-informacje-o-adresie-e-mail" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-retrieve-e-mail-details" target="_blank">EN</a>.


    HTTP: ``GET /account/additional-emails/{emailId}``
    """
    return call_operation(
        "getAdditionalEmailUsingGET",
        {"path:emailId": emailId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
@requires_writes_enabled
def delete_additional_email(
    *,
    emailId: Annotated[
        str,
        Field(
            json_schema_extra=input_schema(
                "deleteAdditionalEmailUsingDELETE", "path:emailId", "emailId"
            )
        ),
    ],
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "deleteAdditionalEmailUsingDELETE", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Delete an additional email address

    Use this resource to delete one of additional emails. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#jak-usunac-adres-e-mail" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#how-to-remove-e-mail" target="_blank">EN</a>.


    HTTP: ``DELETE /account/additional-emails/{emailId}``
    """
    return call_operation(
        "deleteAdditionalEmailUsingDELETE",
        {"path:emailId": emailId, "header:Accept-Language": Accept_Language},
    )


@mcp.tool
@allegro_call
def get_seller_smart_classification_get(
    *,
    marketplaceId: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSellerSmartClassificationGET", "query:marketplaceId", "marketplaceId"
            )
        ),
    ] = None,
    Accept_Language: Annotated[
        str | None,
        Field(
            json_schema_extra=input_schema(
                "getSellerSmartClassificationGET", "header:Accept-Language", "Accept_Language"
            )
        ),
    ] = None,
) -> Any | ErrorResponse:
    """Get Smart! seller classification report

    Use this resource to get a full Smart! seller classification report. Read more: <a href="../../tutorials/jak-zarzadzac-kontem-danymi-uzytkownika-ZM9YAKgPgi2#kwalifikacja-sprzedawcy" target="_blank">PL</a> / <a href="../../tutorials/account-and-user-data-management-jn9vBjqjnsw#seller-qualification" target="_blank">EN</a>.


    HTTP: ``GET /sale/smart``
    """
    return call_operation(
        "getSellerSmartClassificationGET",
        {"query:marketplaceId": marketplaceId, "header:Accept-Language": Accept_Language},
    )
