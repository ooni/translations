# OONI Translations

## Language priorities

The priority languages (sorted alphabetically) are:

* Arabic
* Chinese
* French
* Persian/Farsi
* Russian
* Spanish
* Turkish

Moreover, the following languages are also important to us:

* Ahmaric
* Bengali
* Hindi
* Indonesian
* Thai
* Vietnamese

## Translations

If you would like to improve the translations for OONI tools, please sign up for a Transifex account here: https://www.transifex.com/signup/

There are multiple OONI projects on Transifex that you can join:

* **[OONI Probe app](https://ooni.org/install/)**: Please [join the OONI Probe project on Transifex](https://explore.transifex.com/otf/ooniprobe/) and read the [OONI Probe localization guidelines](https://github.com/ooni/translations/blob/master/Guidelines%20for%20OONI%20Probe.md ) before working on the translation.

* **[OONI Explorer](https://explorer.ooni.org/)**: Please [join the OONI Explorer project on Transifex](https://explore.transifex.com/otf/ooni-explorer/) and read the [OONI Explorer localization guidelines](https://github.com/ooni/translations/blob/master/Guidelines%20for%20OONI%20Explorer.md) before working on the translation.

* **[OONI Run](https://run.ooni.io/)**: Please [join the OONI Run project on Transifex](https://explore.transifex.com/otf/ooni-run/).

* **[OONI Probe Mobile User Guide](https://ooni.org/support/ooni-probe-mobile)**: Please [join the OONI Probe Mobile User Guide project on Transifex](https://explore.transifex.com/otf/ooni-probe-mobile-user-guide/).

* * **[OONI Probe Desktop User Guide](https://ooni.org/support/ooni-probe-desktop)**: Please [join the OONI Probe Desktop User Guide project on Transifex](https://explore.transifex.com/otf/ooni-probe-desktop-user-guide/).

**All translations in the projects listed above are automatically synced from Transifex.**

This repository contains all the translations for OONI tools.

It requires Python 3 and has been tested on Python 3.6.1.

You are expected to have installed the [Transifex
CLI](https://docs.transifex.com/client/installing-the-client) (please don't run
`pip` or `easy_install` as root to install it!).

You should also have setup Transifex with your credentials via a
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

Strings are generated from a [Google Sheet master file](https://docs.google.com/spreadsheets/d/1GPkr_OyNhXJRTXnseyNbo2P4Du-i_W9kJdqjZG4HVkM/edit). To upload new strings you should
add the strings to the [Master Sheet](https://docs.google.com/spreadsheets/d/1GPkr_OyNhXJRTXnseyNbo2P4Du-i_W9kJdqjZG4HVkM/edit)  and then run:

```
./sync-csv-source.sh
```

This will generate `probe-mobile/en/strings.json` and push it to transifex for
you.

## Updating translations for OONI Probe iOS or Android

1) Clone the relative repository https://github.com/ooni/probe-ios or https://github.com/ooni/probe-android
2) Set the var PROJDIR inside the relative update_languages_ios.sh or update_languages_android.sh
3) Run the script


## Adding a new language to OONI Probe iOS or Android

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
