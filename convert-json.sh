#!/bin/bash
set -e
source utils.sh

app=${1:-"probe-mobile"}

validate_app_param $app

source supported_languages_mobile.sh $app

echo "$(basename "$0") : Supported languages ${SUPPORTED_LANGUAGES[*]}"

for dir in ${app}/*/;do
    echo "$(basename "$0") : Converting $dir"
    if [[ $app == "probe-mobile" ]]; then
        python json-to-strings.py \
            --json ${dir}strings.json \
            --strings ${dir}Localizable.strings
        python json-to-android-xml.py \
            --json ${dir}strings.json \
            --xml ${dir}strings.xml
    fi

    if [[ $app == "news-media-scan" ]]; then
        language_code=$(basename $dir)
        base_translation="probe-mobile/${language_code}/strings.json"
        echo "$(basename "$0") : Base translation $base_translation"
        if [ -f "$base_translation" ]; then
            python json-to-nms-android-xml.py \
                --json ${dir}strings.json \
                --xml ${dir}strings.xml \
                --base "${base_translation}"
        fi
    fi
done
