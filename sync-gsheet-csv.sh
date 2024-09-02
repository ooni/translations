#!/usr/bin/env bash

app=${1:-"probe-mobile"}

if [[ "$app" != "probe-mobile" && "$app" != "news-media-scan" ]]; then
    echo "Invalid parameter. The app parameter should be either 'probe-mobile' or 'news-media-scan'."
    exit 1
fi

MOBILE_STRINGS_SHEET="https://docs.google.com/spreadsheets/d/1GPkr_OyNhXJRTXnseyNbo2P4Du-i_W9kJdqjZG4HVkM/export?format=csv"

if [[ "$app" == "news-media-scan" ]]; then
    MOBILE_STRINGS_SHEET="https://docs.google.com/spreadsheets/d/1GPkr_OyNhXJRTXnseyNbo2P4Du-i_W9kJdqjZG4HVkM/export?format=csv&gid=1838996552"
fi

CSV_FILE_PATH="${app}/en/strings.csv"

echo -n "Fetching latest source strings from spreadsheet..."

curl -fsL $MOBILE_STRINGS_SHEET -o $CSV_FILE_PATH

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to download CSV file. Curl failed with error code: $ret"
  exit $ret
fi
echo " done."
