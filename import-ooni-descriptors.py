import argparse
import requests
import json

BASE_URL = "https://api.dev.ooni.io"

TESTS = [
    {
        "name": "Test_Websites_Fullname",
        "short_description": "Dashboard_Websites_Card_Description",
        "description": "Dashboard_Websites_Overview_Paragraph",
        "nettests": [
            {
                "test_name": "web_connectivity",
            }
        ],
        "icon": "OoniWebsites",
        "color": "#4c6ef5",
    },
    {
        "name": "Test_InstantMessaging_Fullname",
        "short_description": "Dashboard_InstantMessaging_Card_Description",
        "description": "Dashboard_InstantMessaging_Overview_Paragraph",
        "nettests": [
            {
                "test_name": "whatsapp",
            },
            {
                "test_name": "telegram",
            },
            {
                "test_name": "facebook_messenger",
            },
            {
                "test_name": "signal",
            },
        ],
        "icon": "OoniInstantMessaging",
        "color": "#15aabf",
    },
    {
        "name": "Test_Circumvention_Fullname",
        "short_description": "Dashboard_Circumvention_Card_Description",
        "description": "Dashboard_Circumvention_Overview_Paragraph",
        "nettests": [
            {
                "test_name": "psiphon",
            },
            {
                "test_name": "tor",
            },
        ],
        "icon": "OoniCircumvention",
        "color": "#e64980",
    },
    {
        "name": "Test_Performance_Fullname",
        "short_description": "Dashboard_Performance_Card_Description",
        "description": "Dashboard_Performance_Overview_Paragraph",
        "nettests": [
            {
                "test_name": "ndt",
            },
            {
                "test_name": "dash",
            },
            {
                "test_name": "http_header_field_manipulation",
            },
            {
                "test_name": "http_invalid_request_line",
            },
        ],
        "icon": "OoniPerformance",
        "color": "#be4bdb",
    },
    {
        "name": "Test_Experimental_Fullname",
        "short_description": "Dashboard_Experimental_Card_Description",
        "description": "Dashboard_Experimental_Overview_Paragraph",
        "nettests": [
            {
                "test_name": "stunreachability",
            },
            {
                "test_name": "openvpn",
            },
            {
                "test_name": "vanilla_tor",
            },
        ],
        "icon": "OoniExperimental",
        "color": "#495057",
    },
]

def load_json(in_path):
    with open(in_path) as in_file:
        return json.load(in_file)

def get_item_intl(key, supported_languages):
    item_intl = {}
    for lang in supported_languages:
        item_intl[lang] = get_string_for_label(key, lang)
    return item_intl

def get_string_for_label(label,lang="en"):
    label = label.replace("_", ".")
    json_data = load_json(f"probe-mobile/{lang}/strings.json")
    return json_data[label]


def set_auth_token(token):
    global AUTH_TOKEN
    AUTH_TOKEN = token

def create_link(name, name_intl, short_description, short_description_intl, description, description_intl, expiration_date, nettests,icon,color,  author="norbel@ooni.org"):
    url = f"{BASE_URL}/api/v2/oonirun/links"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "name_intl": name_intl,
        "short_description": short_description,
        "short_description_intl": short_description_intl,
        "description": description,
        "description_intl": description_intl,
        "author": author,
        "icon": icon,
        "color": color,
        "nettests": nettests,
        "expiration_date": expiration_date
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def upload_ooni_tests(supported_languages):
    for descriptor in TESTS:

        link_name = get_string_for_label(descriptor["name"])
        name_intl =  get_item_intl(descriptor["name"], supported_languages)

        description = get_string_for_label(descriptor["description"])
        description_intl = get_item_intl(descriptor["description"], supported_languages)

        short_description = get_string_for_label(descriptor["short_description"])
        short_description_intl = get_item_intl(descriptor["short_description"], supported_languages)

        nettests = descriptor["nettests"]
        icon = descriptor["icon"]
        color = descriptor["color"]

        expiration_date = "4000-01-01T00:00:00.000000Z" 

        response = create_link(
            name=link_name,
            name_intl=name_intl,
            short_description=short_description,
            short_description_intl=short_description_intl,
            description=description,
            description_intl=description_intl,
            nettests=nettests,
            icon=icon,
            color=color,
            expiration_date=expiration_date,
        )
        print(f"Uploaded {link_name}: {response}")

def main():
    set_auth_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MzA4NTk1OTgsImlhdCI6MTczMDg1OTU5OCwiZXhwIjoxNzQ2NDExNTk4LCJhdWQiOiJ1c2VyX2F1dGgiLCJsb2dpbl90aW1lIjoxNzMwODU5NTk4LCJyb2xlIjoiYWRtaW4iLCJhY2NvdW50X2lkIjoiYmU3YmRlNGU3NTAxOTc3MTMzNzhjY2U1M2E0NzUyYjEiLCJlbWFpbF9hZGRyZXNzIjoibm9yYmVsQG9vbmkub3JnIn0.zVs2UJE11HgSUJ5bVbvlZzARTXX5XCF2MWhD-7hZBdo")
    opt = parse_args()
    upload_ooni_tests(supported_languages=opt.langs)


def parse_args():
    p = argparse.ArgumentParser(description='')
    p.add_argument('--langs', metavar='str', help='language', nargs='*', required=True)
    opt = p.parse_args()
    return opt

if __name__ == "__main__":
    main()