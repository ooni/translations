import argparse
import json
import csv
import sys
import re

def consistency_check(json_a, json_b):
    a_set = set(json_a.keys())
    b_set = set([v['Key'] for v in json_b])
    diff = b_set - a_set
    if len(diff) > 0:
        print("ERROR: inconsistent keys detected")
        print("Missing keys: ")
        print("\n".join(list(diff)))
        raise Exception("Invalid keys")

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
    print("{} written".format(opt.strings))

if __name__ == "__main__":
    main()
