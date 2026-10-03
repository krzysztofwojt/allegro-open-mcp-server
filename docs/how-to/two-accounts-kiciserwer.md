# Dwa konta Allegro na kiciserwerze

Projekt używa MCP przez **stdio**. Nie otwiera portu HTTP/SSE. Klient MCP
uruchamia proces na NAS przez SSH; stdin/stdout połączenia SSH przenoszą MCP.
Nie należy dodawać `-t` do połączenia MCP, ponieważ terminal zmienia strumień.
Kontener pozostaje uruchomiony przez czas połączenia klienta.

Każde konto ma osobny proces, plik konfiguracji i wolumin tokenów.
`ALLEGRO_TOKEN_STORE_PATH` już obsługuje dowolną ścieżkę. Osobne woluminy
zapewniają izolację także wtedy, gdy ścieżka wewnątrz obu kontenerów jest taka sama.
Nie uruchamiaj dwóch procesów używających tego samego token store: rotacja
refresh tokenów wymaga jednego właściciela pliku. Zalogowanie drugiego konta
wymaga drugiego store, a nie przełączania konta w istniejącym store.

## Przygotowanie NAS

Obraz AMD64 został zbudowany na NAS z commitu `62d1dbb`; test rejestru
potwierdził 272 tools, nazwy do 62 znaków i wyłączone zapisy. OAuth obu kont
zostało osobno zatwierdzone, a `GET /me` potwierdziło różne tożsamości. Aktualne szablony i instrukcje przygotowania są w
[deploy/README.md](../../deploy/README.md).

NAS nie ma Git ani Buildx: źródła przesyłamy jako `git archive` przez SSH,
a build wykonujemy z `DOCKER_BUILDKIT=0`. Konfiguracja jest poza repozytorium,
w katalogu `config/` z uprawnieniami 0700 i bez odziedziczonych ACL Synology;
pliki mają 0600. Oba osobne wolumeny tokenów są przygotowane.

Dla powtarzalnego wdrożenia przypnij commit wskazany w raporcie aktualizacji,
a następnie zachowaj tag obrazu. Nie pobieraj ruchomej gałęzi przy każdym starcie.
Lokalny build na Macu sprawdza architekturę ARM64; build na NAS przygotuje
obraz dla jego architektury. Dostęp do Dockera zależy od uprawnień operatora NAS.

Zarejestruj aplikację OAuth z Device Flow w panelu Allegro. Przygotuj poza
repozytorium `/volume1/docker/allegro-mcp/config/prywatne.env` i `firmowe.env`,
z uprawnieniami `0600`. W każdym pliku ustaw:

```env
ALLEGRO_CLIENT_ID=UZUPELNIJ_POZA_REPO
ALLEGRO_CLIENT_SECRET=UZUPELNIJ_POZA_REPO
ALLEGRO_AUTH_FLOW=device
ALLEGRO_ENVIRONMENT=production
ALLEGRO_ENABLE_WRITES=false
ALLEGRO_TOKEN_STORE_PATH=/home/mcp/.allegro-mcp/tokens.json
ALLEGRO_ACCEPT_LANGUAGE=pl-PL
ALLEGRO_USER_AGENT=Registered-App-Name/2026.10.03 (+https://example.org/app-documentation)
```

Sekrety aplikacji mogą być wspólne dla dwóch grantów, jeśli konfiguracja aplikacji
Allegro na to pozwala; autoryzacje i token stores muszą być osobne.
Jeśli ograniczasz zakresy, `ALLEGRO_SCOPES` przyjmuje listę rozdzieloną przecinkami.
Dobierz aktualne zakresy w oficjalnej dokumentacji i panelu aplikacji; dostęp
poszczególnych endpoints zależy też od roli konta i aktywowanych usług.
Nie wpisuj sekretów w argumenty procesu ani do konfiguracji klienta MCP.

## Pierwsze OAuth i weryfikacja właściciela

Poniższy krok wykonuje wyłącznie `GET /me` po autoryzacji. Nie zmienia ofert,
zamówień ani płatności. Uruchom go osobno dla każdego konta, przed podłączeniem MCP.
Użyj osobnych profili przeglądarki, żeby świadomie zatwierdzić właściwe konto.
Wklej w terminalu NAS:

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

Adres autoryzacji i kod pojawią się na stderr. Otwórz adres w profilu konta
prywatnego, zatwierdź grant i sprawdź wyświetlony `id`/`login`. Token zostanie
zapisany w jego woluminie. Powtórz komendę ze zmianą `prywatne.env` na `firmowe.env`
i `allegro-prywatne-tokens` na `allegro-firmowe-tokens`, autoryzując konto firmowe.
Jeśli konto jest niewłaściwe, zatrzymaj proces i usuń wyłącznie token tego konta
przed ponowną autoryzacją. Nie udostępniaj zawartości tokenów ani kopii woluminów.

## Dwa wpisy w kliencie MCP

Przykład konfiguracji klienta obsługującego `mcpServers` (SSH bez TTY):

```json
{
  "mcpServers": {
    "allegro-prywatne": {
      "command": "ssh",
      "args": [
        "-T", "kiciserwer",
        "/usr/local/bin/docker run --rm -i --name allegro-prywatne --env-file /volume1/docker/allegro-mcp/config/prywatne.env -v allegro-prywatne-tokens:/home/mcp/.allegro-mcp allegro-mcp:0af314e-synology-v1"
      ]
    },
    "allegro-firmowe": {
      "command": "ssh",
      "args": [
        "-T", "kiciserwer",
        "/usr/local/bin/docker run --rm -i --name allegro-firmowe --env-file /volume1/docker/allegro-mcp/config/firmowe.env -v allegro-firmowe-tokens:/home/mcp/.allegro-mcp allegro-mcp:0af314e-synology-v1"
      ]
    }
  }
}
```

Najpierw sprawdź na każdej instancji `auth_status`, `me_get` (`GET /me`) oraz
listę narzędzi. Potwierdź odrębne konta i właściwe zakresy. Zachowaj
`ALLEGRO_ENABLE_WRITES=false`. Zapisy wymagają późniejszej świadomej zmiany
konfiguracji i restartu tylko wybranej instancji. Odczyty realizowane POST
(kalkulacja opłat, pobranie etykiet/protokołu i parsowanie składników) są
wyjątkami od bramki zapisów.

PDF, ZPL i inne odpowiedzi binarne narzędzi są zwracane jako `content_base64`,
`content_type` i `content_length`. Uploady przyjmują `content_base64` oraz
`content_type` z oficjalnej listy typów dla endpointu. Nie przekazuj ścieżek
lokalnych plików jako treści uploadu. Wymagane nagłówki, np. `if_match` i `accept`,
są argumentami odpowiednich tools; opcjonalne `Accept-Language` to
`Accept_Language`. Nazwy identyfikatorów camelCase pozostają zgodne z upstream.

## Granice obecnej walidacji

Testy używają mocków HTTP i lokalnego protokołu MCP. Nie potwierdzają prawdziwych
scope'ów/grantów, praw kont, limitów Allegro, rzeczywistej zawartości etykiet,
akceptacji faktur, przewoźników, usług fulfillment ani zachowania konta po zapisie.
Uruchomienie i transport SSH na kiciserwerze będą sprawdzone podczas wdrożenia.
Pełne listowanie 272 tools może przekroczyć budżet narzędzi niektórych klientów;
takie ograniczenie klienta wymaga filtrowania po stronie klienta lub późniejszego
profilu narzędzi, nie pomijania endpoints w generatorze.

Nagłówek `ALLEGRO_USER_AGENT` wygeneruj dla zarejestrowanej aplikacji w
https://apps.developer.allegro.pl/user-agent . Przykładowa wartość wymaga zastąpienia.
