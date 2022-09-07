# Guidelines: Translating the OONI Probe apps

[OONI Probe](https://ooni.org/install/) is free and open source
software designed to measure internet censorship and other forms of network
interference. Since 2012, hundreds of thousands of users have run OONI Probe in 240 countries and territories, contributing millions of network measurements that shed light on internet censorship worldwide.

**By translating the app, you are enabling your communities to measure their
networks and to increase transparency of internet censorship!**

Translating OONI Probe is therefore important, and the OONI team can't
thank you enough.

We hope the following brief guidelines are helpful. If they're not, please reach
out to us at contact@openobservatory.org.

* [Install the OONI Probe apps](#install-the-ooni-probe-apps)

  * [Install the OONI Probe public beta](#install-the-ooni-probe-public-beta)

* [Strings for translation](#strings-for-translation)

* [General recommendations](#general-recommendations)

* [Style of translation](#style-of-translation)

* [Translation of technical terms](#translation-of-technical-terms)

* [Things to watch out for](#things-to-watch-out-for)

## Install the OONI Probe apps

Before getting started with the translation, we kindly ask that you first **[install both the OONI Probe mobile and desktop apps](https://ooni.org/install)** (as each app has a slightly different interface, and different features) to see where your translation would appear in the apps.

**OONI Probe Mobile** is available on: 

* [Android](https://play.google.com/apps/testing/org.openobservatory.ooniprobe)
* [iOS](https://apps.apple.com/us/app/id1199566366)
* [F-Droid](https://f-droid.org/packages/org.openobservatory.ooniprobe/)

**OONI Probe Desktop** is available on:

* [Windows](https://ooni.org/install/desktop)
* [MacOS](https://ooni.org/install/desktop)

### Install the OONI Probe public beta

We also recommend installing the OONI Probe public beta, particularly if you're translating new strings that haven't been shipped as part of an OONI Probe Mobile release yet. This will enable you to see where your translation would appear in the app.

**Android**

* Sign up to the beta:
https://play.google.com/apps/testing/org.openobservatory.ooniprobe

* Update your OONI Probe mobile app (to get the public beta) from Google Play

**iOS**

* Tap on this link from your device and follow the instructions:
https://testflight.apple.com/join/rh3Ig7fE

## General recommendations

Please do not use machine translation as a foundation of your translation. If you are not sure about the terms, ask for advice from someone with technological expertise or from our [Slack community](https://slack.ooni.org/). Do not fear to communicate with other translators through Transifex — you can leave comments, questions and suggestions in the comments of strings. 

Check [Localization Lab's Wiki](https://wiki.localizationlab.org/index.php/Translation_and_Review_Guidelines) for more detailed recommendations.

## Strings for translation

Thanks to support from the [Localization Lab](https://www.localizationlab.org/),
the translation of the OONI Probe Mobile and Desktop apps is coordinated on **Transifex**.

To translate the OONI Probe Mobile and Desktop apps, please sign-up with Transifex to the OONI project:
https://www.transifex.com/otf/ooniprobe/

Once you've been added, you can translate the strings included in the following
2 files:

* App store description: https://www.transifex.com/otf/ooniprobe/description/

* In-app strings: https://www.transifex.com/otf/ooniprobe/strings-json/

## Style of translation

The content in the apps is meant to be **informal and direct (but still polite)**.

We therefore share the following recommendations:

* Use the informal form when referring to the user (for example, you can use the singular
form of "you", instead of the plural form for formality -- if you think it is acceptable in your language)

* Use gender-neutral terminology when referring to the user

* Be concise (but clear) to fit the translation within the character limits
(many of which are set by the app stores)

* Avoid direct translation (such as that of "Heads-up!") if it doesn't make
sense in the translated language

* When/if possible, think about localization beyond translation (for example, you can include "GR"
as the country code for "Greece" in the Greek translation) - without changing
the meaning or adding any new information that may be inaccurate

## Translation of technical terms

OONI Probe has a fair amount of technical terminology.

Here are some tips:

1. Please **avoid translating** the OONI Probe test names (you can keep the
English versions), such as:

* Web Connectivity
* WhatsApp
* Facebook Messenger
* Telegram
* Signal
* HTTP Header Field Manipulation
* HTTP Invalid Request Line
* NDT
* DASH
* Psiphon
* Tor
* Tor Snowflake
* Vanilla Tor
* RiseupVPN
* DNS Check
* STUN Reachability
* URL Getter

2. You can consider **avoiding the translation of "middleboxes"**, since this
term is often used *as is* by the international tech community.

3. Not all technical terms (such as caching, ping, endpoints, etc) are
translated by tech communities around the world (particularly if their
translation does not make much sense). **Often, such terms are used in English,
or they're Englishized.** If you're unsure how specific technical terms are used
in your language by technologists, you can try Googling in your language for
those terms (for example, by checking relevant publications), or reach out to a
technologist (if you know one).

4. We also advise against the translation of "OONI", "OONI Probe", and "OONI Explorer".

## Things to watch out for

*  **Character limits:** Some strings have character limits because they are
either required by the app stores, or by the UX of OONI Probe (only a
certain amount of characters, for example, can fit in a button). We
therefore kindly ask that you try to be concise, while still clearly and
accurately conveying the meaning in the translation.

* **Use of singular & plural forms:** Once you get started with the translation,
you'll probably notice that several strings appear to have duplicate copy
(such as those for terms like "tested", "blocked", "accessible"). These
aren't duplicates, as they are meant to support both the singular and plural
forms of verbs (for many languages, other than English). Please pay
attention to the comments provided inside the strings, indicating whether a
term should be translated to singular or plural form.

* **Composite strings:** You'll come across certain strings that include
variables, such as: `{{Count}} categories enabled`. This means that a number (or
another variable) will appear in the app in the place of `{[Count}}` (for
example, `3 categories enabled`). Please do *not* translate these variables, but
position them in the location where they would make sense in the translated sentence.

* **New lines:** You'll notice that some blue arrows are included in some
strings. These arrows indicate that the next sentence will be in a new line.
Please preserve these arrows in your translation in the same order as
provided in the original copy.

* **Punctuation marks:** Please try (to the degree possible) to preserve the
same punctuation marks (commas, exclamation marks, etc.) as those included
in the original copy.



Questions? You can reach the OONI team for real-time discussion on
[Slack](https://slack.ooni.org/), or you can drop us an email at
contact@openobservatory.org.

**Thank you for your support! We are extremely grateful!**
