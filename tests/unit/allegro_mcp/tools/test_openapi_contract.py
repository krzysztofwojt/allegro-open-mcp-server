"""Contract tests against the pinned official spec and real MCP transport."""

from __future__ import annotations

import asyncio
import base64
import importlib.util
import json
import re
from pathlib import Path

import httpx
import pytest
import yaml
from fastmcp import Client
from jsonschema import Draft4Validator
from pydantic import SecretStr

from allegro_client import AllegroClient, AllegroClientConfig, AllegroError
from allegro_mcp.config import AllegroMCPConfig
from allegro_mcp.tools import _request
from allegro_mcp.tools._runtime import close_client, init_client, mcp

ROOT = Path(__file__).resolve().parents[4]
SPEC = yaml.safe_load((ROOT / "specs/swagger.yaml").read_text())


def test_every_official_operation_has_exactly_one_tool() -> None:
    official = {
        (m.upper(), p)
        for p, item in SPEC["paths"].items()
        for m in item
        if m in {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
    }
    generated = _request._CONTRACT["operations"]
    assert {(o["method"], o["path"]) for o in generated.values()} == official
    names = [o["tool"] for o in generated.values()]
    assert len(names) == len(set(names))
    registered = {tool.name: tool for tool in asyncio.run(mcp.list_tools())}
    assert set(names) | {"auth_status", "auth_login_device", "auth_revoke"} == set(registered)
    for name, tool in registered.items():
        assert re.fullmatch(r"[A-Za-z0-9_-]{1,64}", name)
        Draft4Validator.check_schema(tool.parameters)


def test_required_tracking_query_is_exposed_and_constrained() -> None:
    tools = {t.name: t for t in asyncio.run(mcp.list_tools())}
    schema = tools["get_parcel_tracking"].parameters
    assert "waybill" in schema["required"]
    assert schema["properties"]["waybill"]["maxItems"] == 20
    assert schema["properties"]["waybill"]["items"]["type"] == "string"
    with pytest.raises(AllegroError, match="Invalid query:waybill"):
        _request.call_operation(
            "getParcelTrackingUsingGET",
            {
                "path:carrierId": "DHL",
                "query:waybill": ["x"] * 21,
            },
        )


def test_product_offer_body_exposes_nested_contract_and_validates_before_io() -> None:
    tools = {t.name: t for t in asyncio.run(mcp.list_tools())}
    schema = tools["create_product_offers"].parameters
    assert "body" in schema["required"]
    assert "productSet" in json.dumps(schema["properties"]["body"])
    with pytest.raises(AllegroError, match="Invalid body"):
        _request.call_operation("createProductOffers", {"body": {"productSet": "invalid"}})


@pytest.fixture
def captured(monkeypatch: pytest.MonkeyPatch) -> list[httpx.Request]:
    requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == "/sale/images":
            return httpx.Response(
                201, json={"location": "https://a.allegroimg.com/original/mock-image"}
            )
        if "/labels" in request.url.path:
            return httpx.Response(
                200, content=b"^XA^XZ", headers={"Content-Type": "x-application/zpl"}
            )
        if request.url.path.endswith("/file"):
            return httpx.Response(204)
        return httpx.Response(200, json={"ok": True})

    config = AllegroClientConfig(
        client_id="test", client_secret=SecretStr("test"), auth_flow="device"
    )
    client = AllegroClient(config, transport=httpx.MockTransport(handler))
    close_client()
    init_client(config, AllegroMCPConfig(enable_writes=True), client=client)
    monkeypatch.setattr(_request, "get_client", lambda: client)
    yield requests
    close_client()


def test_binary_invoice_upload_uses_raw_pdf(captured: list[httpx.Request]) -> None:
    pdf = b"%PDF-1.7\nmock invoice"
    result = _request.call_operation(
        "uploadOrderInvoiceFile",
        {
            "path:id": "order",
            "path:invoiceId": "invoice",
            "content_base64": base64.b64encode(pdf).decode(),
            "content_type": "application/pdf",
        },
    )
    assert result is None
    assert captured[0].content == pdf
    assert captured[0].headers["Content-Type"] == "application/pdf"


def test_labels_preserve_binary_and_required_accept(captured: list[httpx.Request]) -> None:
    result = _request.call_operation(
        "getAdvanceShipNoticeLabels",
        {
            "path:id": "00000000-0000-0000-0000-000000000000",
            "header:accept": "x-application/zpl",
        },
    )
    assert base64.b64decode(result["content_base64"]) == b"^XA^XZ"
    assert result["content_type"] == "x-application/zpl"
    assert captured[0].headers["accept"] == "x-application/zpl"


def test_array_serialization_and_path_escaping(captured: list[httpx.Request]) -> None:
    _request.call_operation(
        "getParcelTrackingUsingGET",
        {
            "path:carrierId": "a/b",
            "query:waybill": ["first", "second"],
        },
    )
    assert captured[0].url.params.get_list("waybill") == ["first", "second"]
    assert b"a%2Fb" in captured[0].url.raw_path


def test_invalid_binary_is_rejected_without_io(captured: list[httpx.Request]) -> None:
    with pytest.raises(AllegroError, match="Invalid base64"):
        _request.call_operation(
            "uploadOrderInvoiceFile",
            {
                "path:id": "order",
                "path:invoiceId": "invoice",
                "content_base64": "%%%",
                "content_type": "application/pdf",
            },
        )
    assert not captured


def test_real_mcp_protocol_lists_and_calls_tools(captured: list[httpx.Request]) -> None:
    async def run() -> None:
        async with Client(mcp) as session:
            tools = await session.list_tools()
            assert len(tools) == len(_request._CONTRACT["operations"]) + 3
            result = await session.call_tool(
                "get_parcel_tracking", {"carrierId": "DHL", "waybill": ["123"]}
            )
            assert not result.is_error

    asyncio.run(run())
    assert captured[0].url.path == "/order/carriers/DHL/tracking"


def test_write_tools_refuse_io_by_default(captured: list[httpx.Request]) -> None:
    from allegro_mcp.tools import _runtime

    _runtime._MCP_CONFIG = AllegroMCPConfig()

    async def run() -> None:
        async with Client(mcp) as session:
            result = await session.call_tool("delete_flexible_bundle", {"bundleId": "example"})
            assert "WRITES_DISABLED" in str(result)

    asyncio.run(run())
    assert not captured


def test_generator_name_collisions_and_array_types() -> None:
    spec = importlib.util.spec_from_file_location("gen_tools", ROOT / "scripts/gen_tools.py")
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module._python_type_for({"type": "array", "items": {"type": "integer"}}) == "list[int]"
    assert module._camel_to_snake("a" * 80 + "One") != module._camel_to_snake("a" * 80 + "Two")
    assert len(module._camel_to_snake("a" * 80 + "One")) <= 64
    assert module._parameters(
        {"parameters": [{"in": "query", "name": "x", "required": True}]},
        {"parameters": [{"in": "query", "name": "x"}]},
    )[0]["required"]


def test_auth_status_uses_actual_httpx_strategy_without_network() -> None:
    from allegro_client.auth import DeviceCodeAuth, InMemoryTokenStore, TokenSet
    from allegro_mcp.tools.auth import auth_status

    config = AllegroClientConfig(
        client_id="test", client_secret=SecretStr("test"), auth_flow="device"
    )
    auth = DeviceCodeAuth(config, InMemoryTokenStore())
    auth._tokens = TokenSet(access_token="mock", refresh_token="mock-refresh", scope="scope")
    close_client()
    client = AllegroClient(
        config, auth=auth, transport=httpx.MockTransport(lambda r: pytest.fail("Unexpected I/O"))
    )
    try:
        init_client(config, AllegroMCPConfig(), client=client)
        status = auth_status()
        assert status.has_access_token
        assert status.has_refresh_token
        assert status.scope == "scope"
        assert "mock-refresh" not in status.model_dump_json()
    finally:
        close_client()


def test_separate_accounts_have_separate_token_stores(tmp_path: Path) -> None:
    from allegro_client.auth import FileTokenStore, TokenSet

    private = FileTokenStore(tmp_path / "private/tokens.json")
    company = FileTokenStore(tmp_path / "company/tokens.json")
    private.save(TokenSet(access_token="private", refresh_token="private-refresh"))
    company.save(TokenSet(access_token="company", refresh_token="company-refresh"))
    private.clear()
    assert private.load() is None
    assert company.load().access_token == "company"


def test_json_endpoints_do_not_silently_accept_binary(monkeypatch: pytest.MonkeyPatch) -> None:
    config = AllegroClientConfig(
        client_id="test", client_secret=SecretStr("test"), auth_flow="device"
    )
    with AllegroClient(
        config,
        transport=httpx.MockTransport(
            lambda r: httpx.Response(
                200, content=b"unexpected HTML", headers={"Content-Type": "text/html"}
            )
        ),
    ) as client:
        monkeypatch.setattr(_request, "get_client", lambda: client)
        with pytest.raises(AllegroError, match="Non-JSON response"):
            _request.call_operation("meGET", {})


@pytest.mark.parametrize(
    "arguments",
    [
        {"url": "https://example.org/offer.jpg"},
        {"body": {"url": "https://example.org/offer.jpg"}},
        {
            "body_base64": base64.b64encode(b"\xff\xd8mock jpeg\xff\xd9").decode(),
            "content_type": "image/jpeg",
        },
        {"content_base64": base64.b64encode(b"\xff\xd8mock jpeg\xff\xd9").decode()},
    ],
)
def test_offer_image_upload_accepts_payload_through_real_mcp(
    captured: list[httpx.Request], arguments: dict
) -> None:
    async def run() -> None:
        async with Client(mcp) as session:
            result = await session.call_tool("upload_offer_image", arguments)
            assert not result.is_error
            assert result.data["location"] == "https://a.allegroimg.com/original/mock-image"

    asyncio.run(run())
    assert len(captured) == 1
    request = captured[0]
    assert request.url.host == "upload.allegro.pl"
    assert request.url.path == "/sale/images"
    if "url" in arguments or "body" in arguments:
        assert json.loads(request.content) == arguments.get("body", {"url": arguments.get("url")})
    else:
        assert request.content == base64.b64decode(
            arguments.get("body_base64", arguments.get("content_base64"))
        )
        assert request.headers["Content-Type"] == "image/jpeg"


def test_offer_image_upload_schema_exposes_all_payload_forms() -> None:
    tools = {t.name: t for t in asyncio.run(mcp.list_tools())}
    properties = tools["upload_offer_image"].parameters["properties"]
    assert {"url", "body", "body_base64", "content_base64", "content_type"} <= properties.keys()
    assert "url" in json.dumps(properties["body"])


@pytest.mark.parametrize(
    "arguments",
    [
        {},
        {
            "body:url": "https://example.org/image.jpg",
            "body_base64": "YWJj",
            "content_type": "image/jpeg",
        },
        {"body_base64": "not base64", "content_type": "image/jpeg"},
        {"body_base64": "", "content_type": "image/jpeg"},
        {"body_base64": "YWJj", "content_type": "text/html"},
        {"body_base64": "YWJj", "content_base64": "YWJj", "content_type": "image/jpeg"},
        {"body": {}},
    ],
)
def test_offer_image_upload_rejects_invalid_payload_before_io(
    captured: list[httpx.Request], arguments: dict
) -> None:
    with pytest.raises(AllegroError):
        _request.call_operation("uploadOfferImageUsingPOST", arguments)
    assert captured == []


def test_referenced_request_bodies_are_resolved() -> None:
    for operation in _request._CONTRACT["operations"].values():
        assert "$ref" not in operation["requestBody"]


@pytest.mark.parametrize(
    ("environment", "host"),
    [("production", "upload.allegro.pl"), ("sandbox", "upload.allegro.pl.allegrosandbox.pl")],
)
def test_binary_upload_uses_environment_specific_host(environment: str, host: str) -> None:
    requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(201, json={"location": "https://a.allegroimg.com/image"})

    config = AllegroClientConfig(
        client_id="test",
        client_secret=SecretStr("test"),
        environment=environment,
        auth_flow="device",
    )
    with AllegroClient(config, transport=httpx.MockTransport(handler)) as client:
        client.request_json(
            "POST",
            "/sale/images",
            content=b"jpeg",
            headers={"Content-Type": "image/jpeg"},
            upload=True,
        )
    assert requests[0].url.host == host
    assert requests[0].content == b"jpeg"
