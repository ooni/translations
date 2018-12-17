#!/bin/bash
source supported_languages
set -e

PROJDIR="../probe-ios/"
cd $PROJDIR;
TOPDIR=$(cd $PROJDIR && pwd -P)

if [ ! -d ooniprobe/ ];then
    echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-ios"
    exit 1
fi

cd ../translations
./update-translations.sh
for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | sed 's/zh_CN/zh-Hans/' | sed 's/zh_TW/zh-Hant/')
    dst_path="${TOPDIR}/ooniprobe/${lang}.lproj/"
    if [ ! -d "$dst_path" ];then
        echo "error: $dst_path doesn't exist, remember to add the language to the project and rerun the script"
        else
            cp probe-mobile/${language}/Localizable.strings $dst_path
    fi
done
echo "Translations have been updated"
echo "Remember to commit the changes made to ooni/translations!"
