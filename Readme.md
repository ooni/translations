# OONI Translations

This repository contains all the translations for OONI software.

## Developer setup

If you are a developer you should have a working python environment (3.x is
recommended, but should not be required).

You should then setup a venv in this directory like so:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can then convert the json source files to the Android and iOS format by
running:

```
tx pull -a
./convert-json.sh
```

To upload to transifex the source strings run:

```
tx push -s
```
