#!/bin/bash
set -e

PROJDIR="../probe-ios"
TOPDIR=$(cd $(dirname $0)/.. && pwd -P)

if [ ! -d ${PROJDIR}/ooniprobe/ ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-ios"
    exit 1
fi

source supported_languages_mobile.sh

./update-translations.sh
cp probe-mobile/en/Localizable.strings ${PROJDIR}/ooniprobe/Base.lproj/
for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | sed 's/zh_CN/zh-Hans/' | sed 's/zh_TW/zh-Hant/' | sed 's/pt_BR/pt-BR/')
    dst_path="${PROJDIR}/ooniprobe/${lang}.lproj/"
    if [ ! -d "$dst_path" ];then
        echo "error: $dst_path doesn't exist, remember to add the language to the project and rerun the script"
        else
            cp probe-mobile/${language}/Localizable.strings $dst_path
    fi
done
echo "Translations have been updated"
echo "Remember to commit the changes!"
