#!/bin/bash
# This should only be run when you need to sync source files

python csv-to-json.py \
    --csv probe-mobile/en/strings.csv \
    --json probe-mobile/en/strings.json

python json-to-strings.py \
    --json probe-mobile/en/strings.json \
    --strings probe-mobile/en/Localizable.strings

python json-to-android-xml.py \
    --json probe-mobile/en/strings.json \
    --xml probe-mobile/en/strings.xml
