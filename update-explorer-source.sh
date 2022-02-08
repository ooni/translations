#!/usr/bin/env bash

if [ "X$EXPLORER_STRINGS_SHEET" = "X" ]; then
  echo "Set environment variable EXPLORER_STRINGS_SHEET to the URL of the published CSV"
  exit 1
fi

CSV_FILE_PATH=explorer/en/strings.csv

echo -n "Fetching latest source strings from spreadsheet..."

curl -sL $EXPLORER_STRINGS_SHEET -o $CSV_FILE_PATH

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to download CSV file. Curl failed with error code: $ret"
  exit $ret
fi
echo " done."

echo "Uploading source strings to Transifex..."

tx push -s -r ooni-explorer.website

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to upload source strings."
  exit $ret
fi

