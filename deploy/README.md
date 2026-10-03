# Synology deployment templates

The MCP server uses stdio over SSH. The MCP client starts a container when it
connects; `ssh -T` keeps a terminal from altering the protocol stream, and
`docker run --rm -i` removes the container when the client stops it. The two
named token volumes persist separately at `/home/mcp/.allegro-mcp`. No daemon
or network port is required.

Build the image on kiciserwer from this repository revision and create the
two persistent volumes:

```sh
DOCKER_BUILDKIT=0 /usr/local/bin/docker build -f docker/Dockerfile -t allegro-mcp:0af314e-synology-v1 .
/usr/local/bin/docker volume create allegro-prywatne-tokens
/usr/local/bin/docker volume create allegro-firmowe-tokens
```

Copy each `.env.example` to its matching `.env` under
`/volume1/docker/allegro-mcp/config/`, outside the repository, and fill in that
Allegro application's Device Flow OAuth client credentials. Keep the two
files and token volumes separate. Merge `mcp-servers.json.example` into the
MCP client's `mcpServers` configuration.

## First OAuth and account check

Run this once per account before connecting the MCP client. Use a separate
browser profile for each account and verify the printed Allegro `id` and
`login`. This command performs only `GET /me` and prints no token data:

```sh
/usr/local/bin/docker run --rm -i \
  --env-file /volume1/docker/allegro-mcp/config/prywatne.env \
  -v allegro-prywatne-tokens:/home/mcp/.allegro-mcp \
  --entrypoint python allegro-mcp:0af314e-synology-v1 -c '
from allegro_client import AllegroClient, AllegroClientConfig
from allegro_client.auth import build_auth
config = AllegroClientConfig()
with AllegroClient(config, auth=build_auth(config)) as client:
    me = client.get_json("/me")
    print({"id": me.get("id"), "login": me.get("login")})
'
```

Complete the device authorization using the URL and code shown on stderr.

For the company account, change `prywatne.env` to `firmowe.env` and
`allegro-prywatne-tokens` to `allegro-firmowe-tokens`, then authorize it in
the company browser profile. Both example environments keep
`ALLEGRO_ENABLE_WRITES=false`.

On Synology, disable BuildKit if the Buildx component is absent. The Dockerfile
uses standard RUN instructions; cache mounts are unnecessary. Protect the
new config directory with mode 0700 and credential files with mode 0600.
Remove inherited Synology ACLs granting everyone access on this new directory
before writing credentials. Templates contain no real credentials.
