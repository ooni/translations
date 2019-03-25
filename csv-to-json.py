import argparse
import json
import csv
import sys
import re

assert sys.version_info >= (3, 6), "Python >= 3.6 is required"

def csv_to_dict(in_path):
    d = {}
    with open(in_path) as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip header
        next(csv_reader)
        for line_num, row in enumerate(csv_reader):
            key, text, max_len = row
            text = re.sub(
                r'\{\{(\w+)\}\}',
                r'{\1}',
                text,
            )
            if key in d:
                raise RuntimeError("Duplicate key {} at line: {}".format(key, line_num))
            d[key] = text.strip()
    return d

def write_json(d, out_path):
    with open(out_path, 'w') as out_file:
        json.dump(d, out_file, indent=2)

def parse_args():
    p = argparse.ArgumentParser(description='translations: CSV to KEYVALUEJSON')
    p.add_argument('--csv', metavar='PATH', help='path to the input CSV file', required=True)
    p.add_argument('--json', metavar='PATH', help='json output path', required=True)
    opt = p.parse_args()
    return opt


def main():
    opt = parse_args()
    write_json(csv_to_dict(opt.csv), opt.json)
    print("{} written".format(opt.json))

if __name__ == "__main__":
    main()
