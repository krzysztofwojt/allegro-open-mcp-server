# Upload offer images

`upload_offer_image` requires writes to be enabled and an authorized Allegro
session. It sends requests to Allegro's dedicated upload host for the configured
production or sandbox environment.

Use exactly one payload form. For a public image URL:

```json
{"url": "https://example.org/product.jpg"}
```

The equivalent JSON body form is:

```json
{"body": {"url": "https://example.org/product.jpg"}}
```

For local image bytes, base64-encode the file without a data-URL prefix:

```json
{"body_base64": "<base64-encoded image bytes>", "content_type": "image/jpeg"}
```

`content_base64` is an equivalent argument; use only one of the two names.
Supported binary media types are `image/jpeg`, `image/png`, and `image/webp`.
The default is `image/jpeg`. The server decodes base64 and sends raw bytes,
not a JSON object containing base64. Empty, malformed, conflicting, or
unsupported payloads are rejected before contacting Allegro.

The response contains `location`, a URL on Allegro's image CDN. Copy that value
into `productSet[0].product.images` and the offer's top-level `images` list when
calling `create_product_offers`. Uploading an image does not create an offer.
Images not used in offers may expire at the response's `expiresAt` time.

## Required GTIN

An uploaded image does not bypass product validation. On 2026-10-03, Allegro's
category and product parameter endpoints both reported EAN/GTIN parameter
`225693` as required for category `64493` (Przyborniki), with length 8–14.
Neither response provided a conditional exemption or a "no GTIN" value.
The MCP therefore does not invent an opt-out or substitute a fabricated EAN.
Use a genuine identifier, an appropriate existing catalog product, or obtain
an officially supported exemption from Allegro before creating the product.
