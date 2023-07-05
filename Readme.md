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

If you would like to improve translations for OONI software, please sign up for a Transifex account here: https://www.transifex.com/signup/

There are multiple projects on Transifex that you can join.

If you want to translate **[OONI Probe applications](https://ooni.org/install/)**, please join this project: [https://app.transifex.com/otf/ooniprobe/](https://app.transifex.com/otf/ooniprobe/)

Please read the guidelines for OONI Probe application localization before working on the translation here: https://github.com/ooni/translations/blob/master/Guidelines%20for%20OONI%20Probe.md 

If you want to translate **[OONI Explorer](https://explorer.ooni.org/)** and **[MAT](https://explorer.ooni.org/chart/mat?test_name=web_connectivity&axis_x=measurement_start_day&since=2023-06-06&until=2023-07-06&time_grain=day)** tools, please join this project: [https://app.transifex.com/otf/ooniprobe/](https://app.transifex.com/otf/ooni-explorer/)

Please read the guidelines for OONI Explorer localization before working on the translation here: [https://github.com/ooni/translations/blob/master/Guidelines%20for%20OONI%20Probe.md](https://github.com/ooni/translations/blob/master/Guidelines%20for%20OONI%20Explorer.md)

If you want to translate **[OONI Run](https://run.ooni.io/)** tool, please join this project: [https://app.transifex.com/otf/ooni-run/](https://app.transifex.com/otf/ooni-run/)

If you want to translate **[OONI Probe user guides](https://ooni.org/install/mobile)**, please join this project to translate OONI Probe Mobile application user guide: [https://app.transifex.com/otf/ooni-probe-mobile-user-guide/](https://app.transifex.com/otf/ooni-probe-mobile-user-guide/), and this project to translate OONI Probe Desktop application user guide: [https://app.transifex.com/otf/ooni-probe-desktop-user-guide/](https://app.transifex.com/otf/ooni-probe-desktop-user-guide/).

**All translations in the projects listed above are automatically synched from Transifex.**

This repository contains all the translations for OONI software.

It requires Python 3 and has been tested on Python 3.6.1.

You are expected to have installed the [Transifex
CLI](https://docs.transifex.com/client/installing-the-client) (please don't run
`pip` or `easy_install` as root to install it!).

You should also have setup Transifex with you credentials via a
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
