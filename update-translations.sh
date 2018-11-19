#!/bin/bash
set -e

tx pull -a
./convert-json.sh
