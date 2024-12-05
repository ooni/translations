#!/bin/bash
set -e

source utils.sh

app=${1:-"probe-mobile"}

validate_app_param $app

PROJDIR="../probe-multiplatform"

if [ ! -d ${PROJDIR}/composeApp/src/commonMain/composeResources ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-multiplatform"
    exit 1
fi

if [ "$app" != "probe-mobile" ] && [ ! -d ${PROJDIR}/composeApp/src/ooniMain/composeResources/values/ ];then
    echo "Check your current branch, it should contain the ooni res directory"
    exit 1
fi

if [ "$app" != "news-media-scan" ] && [ ! -d ${PROJDIR}/composeApp/src/dwMain/composeResources/values/ ];then
    echo "Check your current branch, it should contain the dw res directory"
    exit 1
fi

source supported_languages_mobile.sh $app

./update-translations.sh $app

## We want to avoid copying unrequired strings.
## Read `${PROJDIR}/composeApp/src/commonMain/composeResources/values/strings-common.xml` and extract all the keys.
## Then, for each language, read the corresponding `strings.xml` and remove all the keys that are not in the common keys.
## Finally, copy the resulting `strings.xml` to the destination directory.

## loop through the languages

for language in ${SUPPORTED_LANGUAGES[@]};do

    lang=$(basename ${language} | sed 's/zh_CN/zh_rCN/' | sed 's/zh_TW/zh_rTW/' | sed 's/pt_BR/pt_rBR/' | tr '_' '-' )
    echo "Processing language $lang"

    if [ "$app" == "probe-mobile" ];then
        # OONI Resources
        output_dir=${PROJDIR}/composeApp/src/ooniMain/composeResources/values-${lang}/

        # Common Resources
        output_file=${output_dir}/strings-common.xml

        mkdir -p $(dirname ${output_file})

        python convert-from-app-string.py \
            --source ${PROJDIR}/composeApp/src/commonMain/composeResources/values/strings-common.xml \
            --json probe-mobile/${language}/strings.json \
            --destination ${output_file} \
            --lang ${language}

        # Common Resources
        output_file=${output_dir}/strings-organization.xml

        python convert-from-app-string.py \
            --source ${PROJDIR}/composeApp/src/ooniMain/composeResources/values/strings-organization.xml \
            --json probe-mobile/${language}/strings.json \
            --destination ${output_file} \
            --lang ${language}

    fi

    if [ "$app" == "news-media-scan" ];then
        # DW Resources
        output_dir=${PROJDIR}/composeApp/src/dwMain/composeResources/values-${lang}/

          # Common Resources
        output_file=${output_dir}/strings-common.xml

        mkdir -p $(dirname ${output_file})

        mkdir -p ${PROJDIR}/composeApp/src/commonMain/composeResources/values-${lang}/

        python convert-from-app-string.py \
            --source ${PROJDIR}/composeApp/src/commonMain/composeResources/values/strings-common.xml \
            --json probe-mobile/${language}/strings.json \
            --destination ${output_file} \
            --lang ${language}

        # Common Resources
        output_file=${output_dir}/strings-organization.xml

        python convert-from-app-string.py \
            --source ${PROJDIR}/composeApp/src/dwMain/composeResources/values/strings-organization.xml \
            --json probe-mobile/${language}/strings.json \
            --destination ${output_file} \
            --lang ${language}
    fi

done