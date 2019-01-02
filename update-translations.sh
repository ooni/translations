#!/bin/bash
set -e

tx pull -af
./convert-json.sh
