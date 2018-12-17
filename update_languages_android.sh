#!/bin/bash
source supported_languages
set -e

PROJDIR="../probe-android/"
cd $PROJDIR;
TOPDIR=$(cd $PROJDIR && pwd -P)

if [ ! -d app/src/main/res/ ];then
echo "check your PROJDIR variable, it should be the directory where you cloned https://github.com/ooni/probe-android"
exit 1
fi

cd ../translations
./update-translations.sh
for language in "${SUPPORTED_LANGUAGES[@]}";do
    lang=$(basename ${language} | tr '_' '-')
    dst_path="${TOPDIR}/app/src/main/res/values-${lang}/"
    mkdir -p $dst_path
    cp probe-mobile/${language}/strings.xml $dst_path
done
echo "Translations have been updated"
echo "Remember to commit the changes made to ooni/translations!"
