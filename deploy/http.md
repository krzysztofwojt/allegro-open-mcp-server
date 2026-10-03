# Public HTTPS deployment template

This guide and [the Compose example](compose.http.yaml.example) describe a
possible NAS deployment. The image tag `allegro-mcp:http-20261003` is a
placeholder; this repository change does not confirm that an image, container,
DNS record, TLS certificate, or reverse-proxy rule exists on the NAS.

## Endpoints and keys

| Allegro account | Public MCP URL | NAS loopback upstream |
| --- | --- | --- |
| Private | `https://allegro-prywatne-mcp.kwojt.net/mcp` | `http://127.0.0.1:3030` |
| Company | `https://allegro-firmowe-mcp.kwojt.net/mcp` | `http://127.0.0.1:3031` |

Each protected NAS env file must contain its own random
`ALLEGRO_MCP_API_KEY` with at least 32 characters, plus that account's existing
Allegro OAuth settings. Keep the files under
`/volume1/docker/allegro-mcp/config/`, with directory mode `0700` and file mode
`0600`. The sample Compose file loads these files at runtime and contains no
key values. Never commit, paste into chat, or reuse either inbound API key.

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
accessible only to `certadmin`. The two new ACME certificate directories must
also belong to this account and use mode `0700`, with files mode `0600`.
Create an enabled daily DSM Task Scheduler script task, owned by `certadmin`,
running this script at 00:15. It renews and deploys only the two Allegro
certificates, treats ACME's not-due status separately, and fails on renewal or
deployment errors or certificates expiring within 14 days. Existing certificate
tasks remain separate. Verify the task's exit status and served TLS certificates.
