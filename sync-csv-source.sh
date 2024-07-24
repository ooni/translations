#!/bin/bash
# This should only be run when you need to sync source files

app=${1:-"probe-mobile"}

if [[ "$app" != "probe-mobile" && "$app" != "news-media-scan" ]]; then
    echo "Invalid parameter. The app parameter should be either 'probe-mobile' or 'news-media-scan'."
    exit 1
fi

./sync-gsheet-csv.sh $app

python csv-to-json.py \
    --csv $app/en/strings.csv \
    --json $app/en/strings.json

tx push -s
