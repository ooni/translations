import argparse
import requests
import json
import csv
import sys
import os
import re

from hashlib import md5

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

def gen_source_string_hash(string_key):
    string_key = string_key.replace('.', '\\.')
    keys = [string_key, '']
    return md5(':'.join(keys).encode('utf-8')).hexdigest()

def load_transifexrc():
    config = ConfigParser()
    config.read(os.path.expanduser("~/.transifexrc"))
    username = config.get('https://www.transifex.com', 'username')
    password = config.get('https://www.transifex.com', 'password')
    return (username, password)

def put_resource(source_string_hash,
                 project_slug,
                 resource_slug,
                 auth=None,
                 character_limit=None,
                 comment=None,
                 tags=None):
    url = "https://www.transifex.com/api/2/project/{}/resource/{}/source/".format(project_slug, resource_slug)
    payload = {
        'source_string_hash': source_string_hash
    }
    if character_limit:
        payload['character_limit'] = character_limit
    if comment:
        payload['comment'] = comment
    if tags:
        payload['tags'] = tags
    return requests.put(url, json=[payload], auth=auth)

def tx_set_context(in_path, project_slug, resource_slug, auth):
    d = {}
    with open(in_path) as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip header
        next(csv_reader)
        for row in csv_reader:
            comment = None
            character_limit = None
            key, text, max_len = row

            if key in d:
                raise RuntimeError("Duplicate key {}".format(key))

            if key.endswith('Plural'):
                comment = 'This is the plural form'
            if key.endswith('Singular'):
                comment = 'This is the singular form'

            if max_len != "":
                character_limit = int(max_len)

            source_string_hash = gen_source_string_hash(key)
            if character_limit is not None or comment is not None:
                print("Updating {}".format(key))
                if character_limit and character_limit < len(text):
                    print("WARNING: character limit too short for {}".format(key))
                    print("Setting it to len() + 1")
                    character_limit = len(text) + 1
                resp = put_resource(
                        source_string_hash=source_string_hash,
                        project_slug=project_slug,
                        resource_slug=resource_slug,
                        auth=auth,
                        character_limit=character_limit,
                        comment=comment)
                if resp.status_code != 200:
                    raise RuntimeError("Failed to update string")

            d[key] = None
    return d

def parse_args():
    p = argparse.ArgumentParser(description='translations: CSV to KEYVALUEJSON')
    p.add_argument('--csv', metavar='PATH', help='path to the input CSV file', required=True)
    p.add_argument('--project', metavar='PROJECT_SLUG', help='the name of the project on transifex (ex. ooniprobe)', required=True)
    p.add_argument('--resource', metavar='RESOURCE_SLUG', help='the name of the project on transifex (ex. strings-json)', required=True)
    opt = p.parse_args()
    return opt

def main():
    opt = parse_args()
    auth = load_transifexrc()
    tx_set_context(in_path=opt.csv, project_slug=opt.project, resource_slug=opt.resource, auth=auth)

if __name__ == "__main__":
    main()
