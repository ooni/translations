#!/bin/bash
# This should only be run when you need to sync source files

./sync-gsheet-csv.sh

python csv-to-json.py \
    --csv probe-mobile/en/strings.csv \
    --json probe-mobile/en/strings.json

tx push -s
