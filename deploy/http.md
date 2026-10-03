# Public HTTPS deployment

This guide and [the Compose example](compose.http.yaml.example) describe a
NAS deployment. On 2026-10-03, `allegro-mcp:http-20261003` was built on
kiciserwer from commit `ec394d168d1355f632d1da6b95ad2db21733a9ad` and both
services were started from `/volume1/docker/allegro-mcp/http/compose.yaml`.
The image ID is
`sha256:bf6f35bd23adb1fe3986863602598a62ac0a02389da05d7f03c93f00d3aede2c`.

## Endpoints and keys

| Allegro account | Public MCP URL | NAS loopback upstream |
| --- | --- | --- |
| Company | `https://allegro-firmowe-mcp.kwojt.net/mcp` | `http://127.0.0.1:3031` |

Each protected NAS env file must contain its own random
`ALLEGRO_MCP_API_KEY` with at least 32 characters, plus that account's existing
Allegro OAuth settings. Keep the files under
`/volume1/docker/allegro-mcp/config/`, with directory mode `0700` and file mode
`0600`. The sample Compose file loads these files at runtime and contains no
key values. Never commit, paste into chat, or reuse either inbound API key.

For client configuration, protected files containing only the MCP key are
available at `/volume1/docker/allegro-mcp/config/client-access/firmowe.key`.
This contains no Allegro OAuth credentials. Copy this key into the client's secret field. If rotating a key, update both its env file
and client key file, then recreate only that account's container.

The inbound `ALLEGRO_MCP_API_KEY` protects bot-to-MCP requests. It is separate
from Allegro's OAuth credentials and token store. Keep the two token volumes
separate. Only one running process may own a token volume: stop the old stdio
client/container before starting the matching HTTP service, and stop that
service before using a separate stdio process to complete an OAuth grant.

## NAS proxy and network

1. Build and tag the HTTP-enabled image as `allegro-mcp:http-20261003`, then
   copy this Compose example to the NAS deployment directory. Confirm the
   protected env files and the two external token volumes exist before starting
   Compose. Leave `ALLEGRO_ENABLE_WRITES=false` for both services.
2. Configure DSM reverse-proxy rules that preserve `/mcp` and forward each
   hostname to its matching loopback upstream in the table. Attach certificates
   for both names using the existing ACME DNS-01 renewal process.
3. Create the two DNS records in Cloudflare. The public firewall should accept
   TCP 443 for the DSM reverse proxy; keep ports 3030, 3031, and 8000 private.
   The Compose port bindings intentionally listen on loopback only.
4. Start the services and verify each public endpoint independently: an
   unauthenticated MCP request returns `401`, a request with the matching
   `Authorization: Bearer <key>` can initialize MCP, and `me_get` identifies
   the intended Allegro account. Check that writes remain disabled.

## Bot connections

For an MCP client that supports Streamable HTTP and a custom authorization
header, use the matching URL above and send
`Authorization: Bearer <ALLEGRO_MCP_API_KEY>`. Give each bot only the account
key it needs. Bot setup is performed by the account owner after deployment.

ChatGPT cannot present a custom API key to a remote MCP server, so this
Bearer-key endpoint cannot be connected directly that way. A direct remote
ChatGPT connection requires OAuth, which this template does not provide; an
OpenAI Secure MCP Tunnel can instead forward to the local HTTP service with
its Bearer header, as the existing NAS connectors do. The account owner must
configure the tunnel in ChatGPT. See [OpenAI's authentication
documentation](https://developers.openai.com/plugins/build/auth#client-identification).

## Certificate renewal

Install [renew-certificates.sh](renew-certificates.sh) under
`/usr/local/share/acme.sh/allegro-mcp-ops/`, with that directory and script
accessible only to `certadmin`. The company ACME certificate directory must
also belong to this account and use mode `0700`, with files mode `0600`.
Create an enabled daily DSM Task Scheduler script task, owned by `certadmin`,
running this script at 00:15. It renews and deploys only the company Allegro
certificate, treats ACME's not-due status separately, and fails on renewal or
deployment errors or certificates expiring within 14 days. Existing certificate
tasks remain separate. Verify the task's exit status and served TLS certificates.

## Verified deployment (2026-10-03)

- Only the company MCP is deployed. Its DNS-only A record is in Cloudflare's
  `kwojt.net` zone; DSM terminates HTTPS and forwards to `127.0.0.1:3031`.
  Its ZeroSSL certificate expires on 2027-01-01 and HSTS is enabled.
- Enabled DSM task 20, `Renew Allegro MCP HTTPS certificates`, runs daily at
  00:15 as `certadmin`. Its script now targets only the company certificate.
- DSM's IPv4 and IPv6 firewall retains its default drop policy and existing
  TCP 443 allowance. The Docker upstream is bound only to loopback.
  Synology Tailscale userspace forwarding still requires the MCP key.
- Local HTTP and public HTTPS reject missing and invalid keys with 401.
  The company key initializes MCP, lists 272 tools (maximum name length 62),
  and reads the expected company account identity.
- Company writes are enabled with the approved management OAuth scopes;
  buyer-payment refunds remain excluded. No real write was used for validation.
  Direct ChatGPT OAuth is not implemented by this deployment.
- The private service, token volume, env file, inbound key, Cloudflare record,
  DSM proxy route, TLS certificate and ACME files were removed at the operator's
  request. Its OAuth association was also removed from the private Allegro account.
  The shared OAuth application remains registered for the company service.
- Previous implementation validation passed all 274 tests, lint, mypy,
  generated-output checks, package/NAS Docker builds and GitHub CI.
  Retirement was verified by resource absence and a fresh company read smoke.
