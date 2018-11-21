#!/bin/bash
set -e

python tx-set-context.py \
    --csv probe-mobile/en/strings.csv \
    --project ooniprobe \
    --resource strings-json
