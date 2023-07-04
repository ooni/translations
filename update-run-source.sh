#!/usr/bin/env bash

RUN_STRINGS_SHEET='https://docs.google.com/spreadsheets/d/e/2PACX-1vTbPW12s3uzs-HZOWJGCIdKpuhsMZZCSy33Iv179yyWqf2ipEVDODuLzZQCz4q0aOnr-buc0BjvEoGz/pub?gid=0&single=true&output=csv'
CSV_FILE_PATH=run/en/strings.csv
JSON_FILE_PATH=run/en/strings.json

echo -n "Fetching latest source strings from spreadsheet..."

curl -sL $RUN_STRINGS_SHEET -o $CSV_FILE_PATH

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to download CSV file. Curl failed with error code: $ret"
  exit $ret
fi
echo " done."

echo "Converting from CSV format to KEYVALUEJSON"

python csv-to-json.py --csv $CSV_FILE_PATH --json $JSON_FILE_PATH

ret=$?
if [ $ret -ne 0 ]; then
  echo "Failed to convert CSV file to JSON format: $ret"
  exit $ret
fi

echo "Uploading source strings to Transifex..."

tx push -s -r ooni-run.website

ret=$?

if [ $ret -ne 0 ]; then
  echo "Failed to upload source strings."
  exit $ret
fi

echo "✅ Uploaded source strings to Transifex."
