#!/bin/bash
# This should only be run when you need to sync source files

python csv-to-json.py \
    --csv explorer/en/strings.csv \
    --json explorer/en/strings.json
