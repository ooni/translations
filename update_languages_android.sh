#!/bin/bash
set -e

PROJDIR="../probe-android"
TOPDIR=$(cd $(dirname $0)/.. && pwd -P)

if [ ! -d ${PROJDIR}/app/src/main/res/ ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-android"
    exit 1
fi

source supported_languages_mobile.sh

./update-translations.sh
for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | sed 's/zh_CN/zh_rCN/' | sed 's/zh_TW/zh_rTW/' | sed 's/pt_BR/pt_rBR/' | tr '_' '-' )
    dst_path="${PROJDIR}/app/src/main/res/values-${lang}/"
    mkdir -p $dst_path
    cp probe-mobile/${language}/strings.xml $dst_path
done
echo "Translations have been updated"
echo "Remember to commit the changes!"
