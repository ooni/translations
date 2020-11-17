#!/bin/bash
set -e

PROJDIR="../probe-desktop"
TRANSDIR="./probe-mobile"

if [ ! -d ${PROJDIR}/lang ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-desktop"
    exit 1
fi

# We support the same languages supported on mobile
source supported_languages_desktop.sh

# ./update-translations.sh

cp probe-mobile/en/strings.json ${PROJDIR}/lang/en.json

for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | sed 's/zh_CN/zh_rCN/' | sed 's/zh_TW/zh_rTW/' | sed 's/pt_BR/pt_rBR/' | tr '_' '-' )
    dst_path="${PROJDIR}/lang/${lang}.json"
    cp probe-mobile/${language}/strings.json $dst_path
done
echo "Translations have been updated in ${PROJDIR}/lang"

echo "Remember to commit the changes!"
