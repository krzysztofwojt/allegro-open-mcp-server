#!/bin/sh
# Install outside the release checkout and run daily as the ACME owner.
set -eu
umask 077
ACME=/usr/local/share/acme.sh/acme.sh
ACME_HOME=/usr/local/share/acme.sh/.acme.sh
LOG_DIR=/usr/local/share/acme.sh/allegro-mcp-ops
status=0
for domain in allegro-firmowe-mcp.kwojt.net; do
    result=0
    "$ACME" --renew -d "$domain" --home "$ACME_HOME" >"$LOG_DIR/$domain.renew.log" 2>&1 || result=$?
    case "$result" in
        0)
            if SYNO_CERTIFICATE="$domain" "$ACME" -d "$domain" --deploy --deploy-hook synology_dsm --home "$ACME_HOME" >>"$LOG_DIR/$domain.renew.log" 2>&1; then
                echo "$domain: renewed and deployed"
            else
                echo "$domain: deploy FAILED"
                status=1
            fi
            ;;
        2) echo "$domain: renewal not due" ;;
        *) echo "$domain: renewal FAILED ($result)"; status=1 ;;
    esac
    if ! openssl x509 -in "$ACME_HOME/${domain}_ecc/$domain.cer" -noout -checkend 1209600 >/dev/null 2>&1; then
        echo "$domain: certificate expires within 14 days or is unreadable"
        status=1
    fi
done
exit "$status"
