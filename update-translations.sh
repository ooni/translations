#!/bin/bash
set -e

source utils.sh

app=${1:-"probe-mobile"}

validate_app_param $app

tx pull -af
./convert-json.sh $app
