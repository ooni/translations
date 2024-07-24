# -*- coding: utf-8 -*-

import os
import sys
import xml.dom.minidom as md

title_tmpl = u"{title-android}"
subtitle_tmpl = u"{subtitle-ios}"
promotionaltext_tmpl = u"{promotionaltext-ios}"

full_description_tmpl = u"""
{intro}

{intro2}

{intro3}

{intro4}

▶ {evidence-title}
{evidence-description}

▶ {systems-title}
{systems-description}

▶ {speed-title}
{speed-description}

▶ {opendata-title}
{opendata-description}

▶ {freesoftware-title}
{freesoftware-description}

{social-links}
"""
screenshots_tmpl = u"""
# Screnshot 1
{screenshot1}
# Screnshot 2
{screenshot2}
# Screnshot 3
{screenshot3}
# Screnshot 4
{screenshot4}
# Screnshot 5
{screenshot5}
# Feature Graphic
{feature-graphic}
"""
keywords_tmpl = u"{keywords}"

def get_ids(lang_code='en', app_variant='probe-mobile'):
    ids = {}
    dom = md.parse('{app_variant}/{lang_code}/description.xlf'.format(lang_code=lang_code, app_variant=app_variant))
    units = dom.getElementsByTagName('trans-unit')
    for unit in units:
        unit_id = unit.getAttribute('id')
        target = unit.getElementsByTagName('target')
        if len(target) == 0:
            target = unit.getElementsByTagName('source')
        assert len(target) == 1
        target = target[0]
        assert len(target.childNodes) == 1
        value = target.childNodes[0].nodeValue
        if unit_id in ids and ids[unit_id] != value:
            raise Exception("Duplicate ID")
        ids[unit_id] = value
    return ids

def print_frmt(name, value):
    title = "%s (%d chars)" % (name, len(value))
    print(title)
    print("-"*len(title))
    print(value)
    print("\n\n")

def print_tmpls(lang_code='en', app_variant='probe-mobile'):
    ids = get_ids(lang_code, app_variant)

    title = title_tmpl.format(**ids)
    print_frmt("Title", title)

    subtitle = subtitle_tmpl.format(**ids)
    print_frmt("subitle", subtitle)

    promotionaltext = promotionaltext_tmpl.format(**ids)
    print_frmt("Promotional text", promotionaltext)

    if app_variant == 'probe-mobile':
        full_description = full_description_tmpl.format(**ids)
        print_frmt("Full description", full_description)

        screenshots = screenshots_tmpl.format(**ids)
        print_frmt("Screenshots", screenshots)

    elif app_variant == 'news-media-scan':
        full_description = u"{fulldescription}".format(**ids)
        print_frmt("Full description", full_description)

    keywords = keywords_tmpl.format(**ids)
    print_frmt("Keywords", keywords)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s [lang_code]  [app_variant]" % sys.argv[0])
        sys.exit(1)
    if not os.path.exists(os.path.join("{appVariant}/en/description.xlf".format(appVariant=sys.argv[2]))):
        print("ERROR")
        print("This script must be run from the root of the repository")
        sys.exit(1)

    target = sys.argv[1]
    app_variant = sys.argv[2]

    print_tmpls(target, app_variant)
