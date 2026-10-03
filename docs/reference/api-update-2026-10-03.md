# Aktualizacja Allegro API — 2026-10-03

Fork: `krzysztofwojt/allegro-open-mcp-server`, branch
`update-allegro-api-2026-10-03`. Punkt odniesienia upstream: commit
`0d026c9` (2026-05-05). Pobrano oficjalny
[Swagger Allegro](https://developer.allegro.pl/swagger.yaml), zapisując oryginalne
bajty w `specs/swagger.yaml`.

| Pomiar | Upstream | Po aktualizacji |
| --- | ---: | ---: |
| Operacje REST / wygenerowane tools | 265 | 269 |
| Ręczne tools OAuth | 3 | 3 |
| Wszystkie tools MCP | 268 | 272 |
| Moduły wygenerowanych tools | 50 | 53 |
| Klasy w wygenerowanym pliku modeli | 1144 | 1194 |

Stary checksum: `ae1672a032520d0668952395dfed25e05ff74e48ee6edec833fd8645a912e369`.
Nowy checksum: `c3849d2bc296e79c9abeb6962e11fedc4f0b54dc320f086431eacaf322e549bb`.

**Granica porównania:** upstream nie przechowuje historycznego Swaggera, tylko
checksumę, kod modeli i tools. Historia oficjalnego repo `allegro/allegro-api`
nie udostępniała `swagger.yaml` pod tym path. Nie udało się odzyskać oryginalnego
YAML potwierdzonego starą checksumą. Poniższe różnice porównują aktualną oficjalną
specyfikację z zachowanym kodem upstream. Nie są pełnym semantycznym diffem dwóch
oryginalnych specyfikacji. Dawnych enumów, zakresów, scope'ów i wszystkich
wymagań parametrów nie można rzetelnie odtworzyć z wcześniejszego generatora.
Snapshot jest teraz commitowany, aby następna aktualizacja miała pełną bazę.

## Nowe operacje — 9

| Metoda | Endpoint | Znaczenie |
| --- | --- | --- |
| GET | `/sale/flexible-bundles` | Lista elastycznych zestawów |
| POST | `/sale/flexible-bundles` | Tworzenie zestawu |
| GET | `/sale/flexible-bundles/{bundleId}` | Szczegóły zestawu |
| PUT | `/sale/flexible-bundles/{bundleId}` | Aktualizacja zestawu |
| DELETE | `/sale/flexible-bundles/{bundleId}` | Usunięcie zestawu |
| GET | `/fulfillment/warehouse` | Dane magazynu fulfillment |
| GET | `/shipment-management/delivery-proposals/{orderId}` | Propozycje dostawy dla zamówienia |
| POST | `/order/checkout-forms/{id}/serial-numbers` | Numery seryjne pozycji zamówienia |
| POST | `/ingredients/parse` | Parsowanie składników |

## Operacje nieobecne w nowej specyfikacji — 5

- `GET /sale/allegro-prices-account-eligibility`
- `GET /sale/allegro-prices-offer-consents/{offerId}`
- `PUT /sale/allegro-prices-account-consent`
- `PUT /sale/allegro-prices-offer-consents/{offerId}`
- `POST /sale/bundles`

Ich tools i odpowiednie nieużywane modele zostały usunięte przez generatory.
Brak w Swaggerze nie jest dowodem konkretnego zachowania HTTP starego endpointu
na prawdziwym koncie. Potwierdza jednak usunięcie z obecnego oficjalnego kontraktu.

Szczegółowe porównanie routes, parametrów i wszystkich pól modeli znajduje się w
[raporcie JSON](api-update-2026-10-03.json). To zapis porównania AST, nie historyczna specyfikacja.

## Parametry i modele

Trzy zachowane routes mają nowe nazwy parametrów query względem kodu upstream:

- `POST /sale/images`: `isAiCoCreated`.
- `GET /messaging/threads`: `orderId`, `page.id`, `read`, `status`, `type`.
- `GET /messaging/threads/{threadId}/messages`: `page.id`.

Najważniejsze zmiany obserwowane w zachowanym kodzie modeli:

- `CheckoutFormLineItem.serialNumbers` oraz numery seryjne w `CustomerReturnItem`.
- `CheckoutForm.codBookedPayments` — płatności pobraniowe.
- `CheckoutFormsOrderInvoiceFile.verification` i modele szczegółów weryfikacji pliku faktury.
- `CheckoutFormsOrderInvoices.orderMode`.
- `BillingEntry.asset` (`DEBIT`/`CREDIT`) i `marketplaceId`.
- Modele elastycznych zestawów, propozycji dostawy, magazynu i składników.
- `SaleProductOfferRequestV1.aiCoCreatedContent`, `OfferImageLinkUploadRequest.isAiCoCreated`
  oraz AI content w propozycjach produktów.
- `SaleProductOfferRequestV1.compatibilityList` korzysta z `CompatibilityListManualRequest`.
- `ShippingRatesSet.dispatchCountry` i `type`; brak dawnego `ShippingRate.nextItemRate`.
- Brak dawnego `customCost` w request/response ustawień dostawy.
- `AiCoCreatedContent`: `images` zastępuje dawną listę `paths`.

Porównanie nazw klas AST: 69 dodanych, 19 usuniętych, 1125 wspólnych.
73 wspólne klasy mają różnice pól/metadanych; szczegóły są w raporcie JSON.
Bieżące sygnatury wystawiają wszystkie 707 parametrów path/query/header bez braków,
w tym 14 wymaganych parametrów query i 14 wymaganych nagłówków.
Wymagane JSON bodies: 72 (69 na routes zachowanych z upstream). Część nazw
klas inline z przyrostkami numerycznymi zależy od kolejności generowania; ich
zmiana nie dowodzi zmiany modelu biznesowego. Drobne zmiany opisów/przykładów
(np. `SaleProductOffer.images`) nie są breaking changes.

## Breaking changes i zmiany kontraktu MCP

Pewne zmiany względem wcześniejszego serwera:

- Znikają tools pięciu operacji niewystępujących w obecnej specyfikacji.
- Wymagane parametry query i JSON bodies są teraz wymagane także w sygnaturach MCP.
  Dotychczasowy generator prezentował je jako opcjonalne. To poprawka MCP,
  nie dowód, że Allegro dopiero teraz wprowadziło obowiązek tych pól.
- JSON bodies i parametry są walidowane z enumami, ograniczeniami, wymaganymi
  polami i formatami przed HTTP I/O. Nieprawidłowe argumenty zwracają `INVALID_INPUT`.
- Tools uploadu plików przyjmują `content_base64` i `content_type`, zamiast
  błędnego JSON body. Do uploadu potrzebna jest zawartość pliku, także tam, gdzie
  Swagger nie ustawia jawnie `requestBody.required`.
- Odpowiedzi binarne mają `content_base64`, `content_type`, `content_length`.
  Endpointy zadeklarowane jako JSON nadal odrzucają niepoprawne odpowiedzi nie-JSON.
- Nagłówki są wystawione jako argumenty. `if_match` i `accept` są wymagane tam,
  gdzie wymaga ich API; opcjonalne `Accept_Language` pozwala nadpisać język.
- Usunięcie dawnych pól modeli, np. `nextItemRate`, `customCost` i zastąpienie
  `paths` przez `images`, wymaga przeglądu kodu konsumentów. Dokładnych dat
  usunięcia i pełnego zachowania serwera nie potwierdzano na koncie Allegro.

Nie pominięto żadnej z 269 operacji obecnego oficjalnego Swaggera.
Test porównuje komplet operacji z rejestrem MCP, a nie tylko minimalną liczbę tools.
Nazwy mieszczą się w 64 znakach; skracanie długich nazw używa stabilnego hasha,
a kolizje powodują błąd generowania zamiast nadpisywania toola.

## Deprecated — 9 operacji

Zachowane, ale oznaczone `DEPRECATED` w opisach tools:

- `GET /sale/bundles`
- `GET /sale/bundles/{bundleId}`
- `DELETE /sale/bundles/{bundleId}`
- `PUT /sale/bundles/{bundleId}/discount`
- `PUT /sale/turnover-discount/{marketplaceId}`
- `GET /sale/turnover-discount`
- `PUT /sale/turnover-discount/{marketplaceId}/deactivate`
- `GET /shipment-management/delivery-services`
- `DELETE /messaging/messages/{messageId}`

Dla nowych integracji zestawów preferować nowe elastyczne zestawy. Konkretne
zamienniki pozostałych usług należy dobierać według opisów obecnego Swaggera;
nie zakładać, że każdy deprecated endpoint ma dokładny zamiennik jeden do jednego.

## Ważne obszary

Wszystkie obecne w Swaggerze operacje poniższych obszarów występują w registry.
Pełna lista jest w [katalogu tools](tool-catalog.md).

| Obszar | Pokrycie i szczególna kontrola |
| --- | --- |
| Oferty | Tworzenie/edycja product-offers, publikacja, usuwanie, zestawy; JSON body walidowany |
| Produkty, kategorie, parametry | Lista/szczegóły/propozycje produktów, parametry kategorii; schematy wejścia |
| Ceny i stany | Zmiany cen i stock, komendy zbiorcze, pricing; zapisy za bramką |
| Zamówienia | Checkout forms, statusy, przesyłki, numery seryjne |
| Faktury | Metadane, listowanie i upload PDF; weryfikacja pliku w nowych modelach |
| Przesyłki, etykiety, tracking | Propozycje dostawy; PDF/ZPL jako binaria; wymagane query trackingu i nagłówki |
| Wiadomości | Threads/messages, nowe filtry i paginacja, załączniki binarne |
| Zwroty | Customer returns, odrzucenie, fulfillment returns |
| Refundy | Payments refunds oraz commission refunds; operacje mutujące zablokowane domyślnie |
| Billing/opłaty | Billing entries/types, fee preview; nowe asset/marketplaceId |
| Użytkownik/sprzedawca | `/me`, dane publiczne, rating, quality, marketplaces |

## Generowanie i walidacja

Naprawiono target `make gen-tools`, który wskazywał na nieistniejący
`gen_tool_inventory.py`. Nie edytowano ręcznie wyników generowania.
`specs/swagger.yaml` jest źródłem dla obu generatorów; `_contract.json` to
pakietowany, wygenerowany kontrakt parametrów i request bodies.
Zachowano separację `allegro_client` i `allegro_mcp`.

| Kontrola | Wynik lokalny |
| --- | --- |
| Upstream baseline | 249 tests passed, 268 tools |
| `make gen-models` | OK |
| `make gen-tools` + format | OK, 269 operacji w 53 modułach |
| `make test` | 267 passed |
| Python 3.10 / 3.11 / 3.12 / 3.13 | 267 passed na każdej wersji |
| `make lint` | Ruff check/format oraz strict mypy OK |
| Schematy MCP | Wszystkie poprawne; test przez rzeczywisty klient/protokół MCP |
| Schematy modeli | Wszystkie 1194 wygenerowane klasy poprawnie budują schematy |
| `make check-generated` | Identyczne modele, tools i kontrakt po ponownym generowaniu |
| `make check-models-freshness` | Pinned i live spec zgodne z checksumą modeli |
| `uv build` | Wheel i sdist OK; kontrakt JSON obecny w wheel |
| `make build` | Runtime Docker image OK, lokalny ARM64 |
| Smoke kontenera | 272 tools, writes False, bez konfiguracji OAuth |
| `make docs-build` / `make docs-coverage` | Strict MkDocs build i pokrycie 272 tools OK |

Generator modeli ostrzega o niestandardowych formatach w oficjalnym Swaggerze
(np. `ISO 4217`, `ISO format`) i używa bazowych typów zgodnie z istniejącym
mechanizmem codegen. Walidator JSON Schema sprawdza rozpoznawane standardowe
formaty; nie nadaje własnego znaczenia niestandardowym formatom Allegro.
Nie wyłączono testów ani walidacji w celu uzyskania zielonego builda.

Naprawiono też błąd lokalnych tools OAuth i guardu scope: rzeczywista strategia
jest w kliencie httpx, a nie w nieistniejącym `AllegroClient._auth`.
Test statusu używa mock-tokenów i sprawdza, że token bytes nie są ujawniane.

## Czego nie zweryfikowano

Nie autoryzowano żadnego konta i nie wykonano rzeczywistych operacji konta Allegro.
Nie potwierdzono scope'ów, uprawnień/aktywowanych usług sprzedawcy, realnej rotacji
OAuth, zachowania zapisów, limitów Allegro, uploadu rzeczywistej faktury ani
wydruku etykiety. NAS, jego architektura, woluminy i transport SSH zostaną
zweryfikowane podczas późniejszego wdrożenia. Wszystkie testy HTTP korzystają
z mocków. Domyślne `ALLEGRO_ENABLE_WRITES=false` jest zachowane.

[Następny krok: dwie instancje i osobne OAuth na kiciserwerze](../how-to/two-accounts-kiciserwer.md).
