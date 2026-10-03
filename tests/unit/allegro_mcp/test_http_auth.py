"""Inbound HTTP authentication must never fall back to anonymous access."""

from __future__ import annotations

import asyncio

import httpx
import pytest
from fastmcp import FastMCP
from pydantic import SecretStr, ValidationError

from allegro_mcp.config import AllegroMCPConfig
from allegro_mcp.http_auth import APIKeyVerifier

PRIVATE_KEY = "private-test-key-" + "a" * 48
COMPANY_KEY = "company-test-key-" + "b" * 48


@pytest.mark.parametrize("key", [None, "", "too-short"])
def test_http_refuses_missing_or_weak_key(clean_env: None, key: str | None) -> None:
    with pytest.raises(ValidationError, match="ALLEGRO_MCP_API_KEY"):
        AllegroMCPConfig(transport="http", mcp_api_key=key)


def test_stdio_remains_default_without_inbound_key(clean_env: None) -> None:
    assert AllegroMCPConfig().transport == "stdio"


def test_http_key_is_separate_from_allegro_credentials(
    clean_env: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("ALLEGRO_CLIENT_SECRET", PRIVATE_KEY)
    with pytest.raises(ValidationError, match="ALLEGRO_MCP_API_KEY"):
        AllegroMCPConfig(transport="http")


def test_bearer_gate_and_account_isolation() -> None:
    async def run() -> None:
        for name, key, other_key in [
            ("private", PRIVATE_KEY, COMPANY_KEY),
            ("company", COMPANY_KEY, PRIVATE_KEY),
        ]:
            server = FastMCP(name, auth=APIKeyVerifier(SecretStr(key)))
            app = server.http_app(path="/mcp", stateless_http=True)
            body = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {},
                    "clientInfo": {"name": "auth-test", "version": "1"},
                },
            }
            async with (
                app.router.lifespan_context(app),
                httpx.AsyncClient(
                    transport=httpx.ASGITransport(app=app), base_url="http://testserver"
                ) as client,
            ):
                headers = {"Accept": "application/json, text/event-stream"}
                for rejected in [None, "invalid", other_key, "zażółć"]:
                    attempt = dict(headers)
                    if rejected is not None:
                        if not rejected.isascii():
                            assert await server.auth.verify_token(rejected) is None
                            continue
                        attempt["Authorization"] = f"Bearer {rejected}"
                    response = await client.post("/mcp", json=body, headers=attempt)
                    assert response.status_code == 401
                    assert "Bearer" in response.headers["www-authenticate"]
                headers["Authorization"] = f"Bearer {key}"
                response = await client.post("/mcp", json=body, headers=headers)
                assert response.status_code == 200
                assert name in response.text

    asyncio.run(run())
