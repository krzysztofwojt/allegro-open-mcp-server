# Company-account management

The generated MCP already exposes offer creation and editing, price and stock
changes, customer messages, sales settings, order handling and shipments.
These operations need both the MCP write gate and the appropriate Allegro
OAuth grant. The default deployment remains read-only for both accounts.

## Prepared company-only opt-in

Use [the company override](compose.firmowe-writes.yaml.example) with the base
HTTP Compose configuration after approving activation. It changes only
`allegro-firmowe`; do not enable writes on `allegro-prywatne`.

Keep the company account's existing read and messaging scopes and additionally
request these scopes in its protected `firmowe.env`:

```text
allegro:api:sale:offers:write
allegro:api:sale:settings:write
allegro:api:orders:write
allegro:api:shipments:write
```

The shared OAuth application's Developer Apps settings must allow these scopes.
The private MCP keeps its explicit read scopes and its disabled write gate.
Messaging already uses the combined `allegro:api:messaging` scope; Allegro does
not split it into separate read/write permissions. The buyer-payment refund
scope `allegro:api:payments:write` is not part of this profile. Commission-refund
applications and customer-return decisions belong to the broader orders scope
in Allegro's API. Fulfillment warehouse management is also separate.

Relevant existing tools include `create_product_offers`, `edit_product_offers`,
`change_publication_status`, `quantity_modification_command`,
`new_message_in_thread_post`, `new_message_post`, `set_order_fulfillment`
and `create_new_shipment`. Tool generation already covers these endpoints;
enabling company management does not require editing generated files.

## Authorization and validation

1. Back up the protected company environment, Compose configuration and company
   token store outside the checkout. Restrict backups to the operator.
2. Allow the four scopes in Allegro Developer Apps. Allegro may require another
   sign-in before editing this application. Never expose the Client Secret.
3. Stop only the company HTTP container before a separate OAuth process accesses
   its token volume. Obtain a new company grant requesting the expanded scope
   list, verify `/me` belongs to the company account, then start the company
   container with the override. Keep the private service running unchanged.
4. Verify effective company/private write flags and granted scopes, protected
   HTTPS authentication, `tools/list`, and a read-only `/me` call for each.
   Unit tests exercise write gating with mocked calls. Enabling a capability
   does not authorize creating a test offer or sending a real customer message.

Changing requested scopes in an env file alone does not grant permissions.
Treat the returned token scope set as authoritative. See [Allegro's scope
documentation](https://developer.allegro.pl/news/zarzadzanie-lista-scopeow-aplikacji-allegro-v8WDrwvnXF2).
