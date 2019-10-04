import argparse
import json
import csv
import sys
import re

def consistency_check(json_a, json_b):
    a_set = set(json_a.keys())
    b_set = set([v['Key'] for v in json_b])

    obsolete_keys = a_set - b_set
    if len(obsolete_keys) > 0:
        print("=================================")
        print("ERROR: obsolete keys detected in copy:")
        print("\n".join(list(sorted(obsolete_keys))))

    missing_keys = b_set - a_set
    if len(missing_keys) > 0:
        print("=================================")
        print("ERROR: Following keys missing from copy: ")
        print("\n".join(list(sorted(missing_keys))))

    if (len(missing_keys) or len(obsolete_keys)):
        print("=================================")
        print("Summary")
        print("* Obsolete Keys: {}".format(len(obsolete_keys)))
        print("* Missing Keys: {}".format(len(missing_keys)))
    else:
        print("No error detected")
    return

def load_json(in_path):
    with open(in_path) as in_file:
        return json.load(in_file)

def parse_args():
    p = argparse.ArgumentParser(description='translations: KEYVALUESJSON consistency check')
    p.add_argument('--json-strings', metavar='PATH', help='path json strings generated from the CSV', required=True)
    p.add_argument('--json-code', metavar='PATH', help='path to the JSON keys extracted from the code', required=True)
    opt = p.parse_args()
    return opt

def main():
    opt = parse_args()
    consistency_check(load_json(opt.json_strings), load_json(opt.json_code))

if __name__ == "__main__":
    main()
