#!/bin/bash
set -e

for dir in probe-mobile/*/;do
    echo "Converting $dir"
    python json-to-strings.py \
        --json ${dir}strings.json \
        --strings ${dir}Localizable.strings
    python json-to-android-xml.py \
        --json ${dir}strings.json \
        --xml ${dir}strings.xml
done
