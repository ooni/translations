#!/usr/bin/env bash

PROBE_MOBILE_STRINGS_SHEET="https://docs.google.com/spreadsheets/d/1GPkr_OyNhXJRTXnseyNbo2P4Du-i_W9kJdqjZG4HVkM/export?format=csv"

CSV_FILE_PATH=probe-mobile/en/strings.csv

echo -n "Fetching latest source strings from spreadsheet..."

curl -sL $PROBE_MOBILE_STRINGS_SHEET -o $CSV_FILE_PATH

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to download CSV file. Curl failed with error code: $ret"
  exit $ret
fi
echo " done."