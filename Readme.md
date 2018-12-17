# OONI Translations

This repository contains all the translations for OONI software.

It requires python 3 and has been tested on `Python 3.6.1`.

You are expected to have installed the [transifex
CLI](https://docs.transifex.com/client/installing-the-client) (please don't run
`pip` or `easy_install` as root to install it!).

You should also have setup transifex with you credentials via a
`~/.transifexrc` file (see: [client-configuration
docs](https://docs.transifex.com/client/client-configuration#~/-transifexrc)).

## Updating translations

This is the process by which you pull the latest translations and generate the
OS specific localization strings.

Usually you will run this as part of the app workflow, but you can also do it
in here via:

```
./update-translations.sh
```

## Uploading new strings

Strings are generated from a csv master file. To upload new strings you should
copy the strings csv file to `probe-mobile/en/strings.csv` and then run:

```
./sync-csv-source.sh
```

This will generate `probe-mobile/en/strings.json` and push it to transifex for
you.

## Updating translations for OONI Probe iOS or Android

1) Clone the relative repository https://github.com/ooni/probe-ios or https://github.com/ooni/probe-android
2) Set the var PROJDIR inside the relative update_languages_ios.sh or update_languages_android.sh
3) Run the script


## Adding new language to OONI Probe iOS or Android

1) Add the new language code to the file supported_languages
2) iOS only: Add the new language in the XCode project tab
3) Run the update_languages_ios.sh or update_languages_android.sh script

## Generating descriptions for market

To generate translated descriptions for the markets run:

```
python scripts/gen-descriptions.py [lang_code]
```

Where `lang_code` is the language code for the description you want to
generate.

This will print to standard output the translated text that you can then copy
and paste into the market descriptions.

If a string is not translated it will print the source for the text.
