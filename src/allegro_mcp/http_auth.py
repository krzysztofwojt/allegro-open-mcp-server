"""Inbound MCP authentication, separate from the Allegro OAuth credentials."""

from __future__ import annotations

import hashlib
import hmac

from fastmcp.server.auth import AccessToken, TokenVerifier
from pydantic import SecretStr


class APIKeyVerifier(TokenVerifier):
    """Verify an operator-issued bearer key without retaining plaintext keys.

    Generate a unique random key for each account, keep it in a protected env
    file, and rotate it by restarting that account's server. HTTPS terminates
    at the reverse proxy; the Docker port must bind only to loopback.
    """

    def __init__(self, key: SecretStr) -> None:
        super().__init__()
        self._digest = hashlib.sha256(key.get_secret_value().encode()).digest()

    async def verify_token(self, token: str) -> AccessToken | None:
        candidate = hashlib.sha256(token.encode()).digest()
        if not hmac.compare_digest(candidate, self._digest):
            return None
        return AccessToken(token=token, client_id="allegro-mcp-client", scopes=[])
