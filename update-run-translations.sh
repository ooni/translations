#!/bin/bash
set -e

MINIMUM_TRANSLATION_NEEDED=${1:-90}

echo "Fetching translations for languages with at least ${MINIMUM_TRANSLATION_NEEDED}% completion..."

tx pull -a \
  -r ooni-run.website \
  --minimum-perc=${MINIMUM_TRANSLATION_NEEDED}