#!/bin/bash
set -e

source utils.sh

app=${1:-"probe-mobile"}

validate_app_param $app

PROJDIR="../probe-android"
TOPDIR=$(cd $(dirname $0)/.. && pwd -P)

if [ ! -d ${PROJDIR}/app/src/main/res/ ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-android"
    exit 1
fi

if [ "$app" != "probe-mobile" ] && [ ! -d ${PROJDIR}/app/src/ooni/res/values/ ];then
    echo "Check your current branch, it should contain the ooni res directory"
    exit 1
fi

if [ "$app" != "news-media-scan" ] && [ ! -d ${PROJDIR}/app/src/dw/res/values/ ];then
    echo "Check your current branch, it should contain the dw res directory"
    exit 1
fi

source supported_languages_mobile.sh $app

./update-translations.sh $app

cp probe-mobile/en/strings.xml ${PROJDIR}/app/src/main/res/values/
if [[ $app == "news-media-scan" ]]; then
    cp "$app/en/strings.xml" "${PROJDIR}/app/src/dw/res/values/"
fi

for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | sed 's/zh_CN/zh_rCN/' | sed 's/zh_TW/zh_rTW/' | sed 's/pt_BR/pt_rBR/' | tr '_' '-' )

    dst_path="${PROJDIR}/app/src/main/res/values-${lang}/"
    if [[ $app == "probe-mobile" ]]; then
        dst_path="${PROJDIR}/app/src/ooni/res/values-${lang}/"
    fi
    if [[ $app == "news-media-scan" ]]; then
        dst_path="${PROJDIR}/app/src/dw/res/values-${lang}/"
    fi
    mkdir -p $dst_path
    cp probe-mobile/${language}/strings.xml $dst_path
done

echo "Translations have been updated"
echo "Remember to commit the changes!"
