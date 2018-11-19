import argparse
import json
import csv
import sys
import re

def dict_to_strings(d, out_path):
    with open(out_path, 'w') as out_file:
        for key, text in d.items():
            text = re.sub(
                r'\{(\w+)\}',
                r'%@',
                text,
            )
            out_file.write('"{}" = "{}";'.format(key, text))
            out_file.write('\n')

def load_json(in_path):
    with open(in_path) as in_file:
        return json.load(in_file)

def parse_args():
    p = argparse.ArgumentParser(description='translations: CSV to KEYVALUEJSON')
    p.add_argument('--json', metavar='PATH', help='json input path', required=True)
    p.add_argument('--strings', metavar='PATH', help='strings output path', required=True)
    opt = p.parse_args()
    return opt


def main():
    opt = parse_args()
    dict_to_strings(load_json(opt.json), opt.strings)
    print("{} written".format(opt.strings))

if __name__ == "__main__":
    main()
