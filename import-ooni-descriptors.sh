#!/bin/bash
set -e

source utils.sh

app=${1:-"probe-mobile"}

source supported_languages_mobile.sh $app

python import-ooni-descriptors.py \
    --langs ${SUPPORTED_LANGUAGES[@]}