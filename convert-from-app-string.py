import argparse
import json
import csv
import sys
import re
import xml.etree.ElementTree as ET

assert sys.version_info >= (3, 6), "Python >= 3.6 is required"


def parse_args():
    p = argparse.ArgumentParser(description="translations: CSV to KEYVALUEJSON")
    p.add_argument(
        "--source", metavar="PATH", help="path to multiplatform source", required=True
    )
    p.add_argument(
        "--destination",
        metavar="PATH",
        help="path to multiplatform source",
        required=True,
    )
    p.add_argument(
        "--json", metavar="PATH", help="path to multiplatform source", required=True
    )
    p.add_argument("--app", metavar="STRING", help="app", required=True)
    p.add_argument(
        "--base", metavar="PATH", help="ooni base json input path", required=False
    )
    p.add_argument("--lang", metavar="STRING", help="language", required=True)
    opt = p.parse_args()
    return opt


def load_json(in_path):
    with open(in_path) as in_file:
        return json.load(in_file)


def load_xml_keys(in_path):
    tree = ET.parse(in_path)
    root = tree.getroot()
    result = {}
    for string in root.findall("string"):
        key = string.get("name")
        value = string.text
        result[key] = value
    return result


def dict_to_android_xml(d, out_path, app):
    resources = ET.Element("resources")

    comment = ET.Comment(
        "This file is generated from https://github.com/ooni/translations. Please do not modify unless you know what youre doing"
    )
    resources.insert(0, comment)

    for key, text in d.items():
        key = key.replace(".", "_")
        if key == "Dashboard_Runv2_Overview_Description":
            text = text.replace("\\n\\n%s", "")
            # replace first `%s` with `%1$s` and second `%s` with `%2$s`
            text = text.replace("%s", "%1$s", 1)
            text = text.replace("%s", "%2$s", 1)

        if key == "Dashboard_Experimental_Overview_Paragraph":
            # replace first `{experimental_test_list}` with `%1$s`
            text = text.replace("{experimental_test_list}", "%1$s", 1)

        if (
            key == "Settings_Websites_Categories_Description"
            or key == "TestResults_Overview_Websites_Blocked_Singular"
            or key == "TestResults_Overview_Websites_Blocked_Plural"
            or key == "TestResults_Overview_Websites_Tested_Singular"
            or key == "TestResults_Overview_Websites_Tested_Plural"
            or key == "TestResults_Overview_InstantMessaging_Blocked_Singular"
            or key == "TestResults_Overview_InstantMessaging_Available_Singular"
            or key == "TestResults_Overview_InstantMessaging_Available_Plural"
            or key == "TestResults_Overview_InstantMessaging_Blocked_Plural"
            or key == "TestResults_Overview_Circumvention_Blocked_Singular"
            or key == "TestResults_Overview_Circumvention_Blocked_Plural"
            or key == "TestResults_Overview_Circumvention_Available_Singular"
            or key == "TestResults_Overview_Circumvention_Available_Plural"

        ):
            # replace first `{Count}` with `%1$s`
            text = text.replace("{Count}", "%1$s", 1)
            print(text)

        if key == "Modal_ResultsNotUploaded_Uploading":
            # replace first `{testNumber}` with `%1$s`
            text = text.replace("{testNumber}", "%1$s", 1)

        if key == "Modal_ReRun_Websites_Title":
            # replace first `{experimental_test_list}` with `%1$s`
            text = text.replace("{websitesNumber}", "%1$s", 1)

        if key == "Modal_UploadFailed_Paragraph":
            # replace first `{numberFailed}` with `%1$s` and second `{totalUploads}` with `%2$s`
            text = text.replace("{numberFailed}", "%1$s", 1)
            text = text.replace("{totalUploads}", "%2$s", 1)

        if key == "Settings_AutomatedTesting_RunAutomatically_Number":
            # replace first `{testsNumber}` with `%1$s`
            text = text.replace("{testsNumber}", "%1$s", 1)

        if key == "Settings_AutomatedTesting_RunAutomatically_DateLast":
            # replace first `{testDate}` with `%1$s`
            text = text.replace("{testDate}", "%1$s", 1)

        if app == "news-media-scan" and key == "Modal_EnableNotifications_Paragraph":
            # replace `OONI Probe` with `News Media Scan`
            text = text.replace("OONI Probe", "News Media Scan", 1)

        string_element = ET.SubElement(resources, "string", name=key)
        string_element.text = text

    tree = ET.ElementTree(resources)
    ET.indent(tree)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def main():
    opt = parse_args()
    source_keys = load_xml_keys(opt.source).keys()
    json_data = load_json(opt.json)

    filtered_data = {}
    for key, text in json_data.items():
        key = key.replace(".", "_")
        if key in source_keys:
            filtered_data[key] = text

    if opt.base is not None:
        base_data = load_json(opt.base)

        for key, text in base_data.items():
            key = key.replace(".", "_")
            if key == "Modal_EnableNotifications_Paragraph":
                filtered_data[key] = text

    dict_to_android_xml(filtered_data, opt.destination, opt.app)


if __name__ == "__main__":
    main()
