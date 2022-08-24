# Guidelines: Translating the OONI Explorer

[OONI Explorer](https://explorer.ooni.org/) is an open data resource on Internet censorship around the world consisting of millions of measurements on network inteference. Since 2012, more than 800 million of network measurements have been collected from more than 240 countries. OONI Explorer sheds light on internet censorship and other forms of network interference worldwide.

**By translating the OONI Explorer interface, you are enabling researchers, journalists, activists and users to track Internet censorship in their countries!**

Translating OONI Explore is therefore important, and the OONI team can't
thank you enough.

We hope the following brief guidelines are helpful. If they're not, please reach
out to us at contact@openobservatory.org.

* [Open the OONI Explorer](#open-the-ooni-explorer)

* [Strings for translation](#strings-for-translation)

* [General recommendations](#general-recommendations)

* [Style of translation](#style-of-translation)

* [Translation of technical terms](#translation-of-technical-terms)

* [Things to watch out for](#things-to-watch-out-for)


## Open the OONI Explorer

Before you get started with the translation, we kindly ask that you first open the [OONI Explorer](https://explorer.ooni.org/) to see where your translation would appear in the service.

## General recommendations

Please do not use machine translation as a foundation of your translation. If you are not sure about the terms, ask for advice from someone with technological expertise or from our [Slack community](https://slack.openobservatory.org/). Do not fear to communicate with other translators through Transifex — leave comments, questions and suggestions in the comments to the string. 

Check our [Wiki](https://wiki.localizationlab.org/index.php/Translation_and_Review_Guidelines) for more detailed recommendations.

## Strings for translation

Thanks to support from the [Localization Lab](https://www.localizationlab.org/),
the translation of the OONI Probe Mobile and Desktop apps is coordinated on Transifex.

To translate the OONI Explorer, please sign-up with Transifex to the OONI project:
https://www.transifex.com/otf/ooni-explorer/

## Style of translation

The content in the OONI Explorer is meant to be **informal and direct (but still polite)**.

We therefore share the following recommendations:

* Use the formal form when referring to the user (for example, use the plural
form of "you", instead of the singular form)

* Use gender-neutral terminology when referring to the user

* Be concise (but clear) to fit the translation within the character limits

* When/if possible, think about localization beyond translation (for example, you can include "GR"
as the country code for "Greece" in the Greek translation) - without changing
the meaning or adding any new information that may be inaccurate

## Translation of technical terms

OONI Explorer has a fair amount of technical terminology.

Here are some tips:

1. Please **avoid translating** the OONI Explorer test names (you can keep the
English versions):

* Web Connectivity
* WhatsApp
* Facebook Messenger
* Telegram
* HTTP Header Field Manipulation
* HTTP Invalid Request Line
* NDT
* DASH

2. You can consider **avoiding the translation of "middleboxes"**, since this
term is often used *as is* by the international tech community.

3. Not all technical terms (such as caching, ping, endpoints, etc) are
translated by tech communities around the world (particularly if their
translation does not make much sense). **Often, such terms are used in English,
or they're Englishized.** If you're unsure how specific technical terms are used
in your language by technologists, you can try Googling in your language for
those terms (for example, by checking relevant publications), or reach out to a
technologist (if you know one).

4. We also advise against the translation of "OONI", "OONI Probe" and "Open Observatory Network Interference" and names of instruments, e.g. "OONI MAT" (OONI Measurement Aggregation Toolkit)

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
variables, such as: `OONI Probe users in **{countryName}** have collected [**{measurementCount}** measurements]⏎`. This means that a number (or
another variable) will appear in the app in the place of `{[measurementCount}}` (for
example, `801045`) and a name of the country will appear instead of `{countryName}`(for example. `Canada`). Please do *not* translate these variables, but
position them in the location where they would make sense in the translated sentence.

* **New lines:** You'll notice that some blue arrows are included in some
strings. These arrows indicate that the next sentence will be in a new line.
Please preserve these arrows in your translation in the same order as
provided in the original copy.

* **Punctuation marks:** Please try (to the degree possible) to preserve the
same punctuation marks (commas, exclamation marks, etc.) as those included
in the original copy.



Questions? You can reach the OONI team for real-time discussion on
[Slack](https://slack.openobservatory.org/), or you can drop us an email at
contact@openobservatory.org.

**Thank you for your support! We are extremely grateful!**