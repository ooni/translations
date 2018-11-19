import argparse
import json
import cgi
import csv
import sys
import re

# Special replacement class that counts the matches
class ReplaceCounter(object):
    def __init__(self):
        self.idx = 0
    def __call__(self, match):
        self.idx += 1
        return "%{}$s".format(self.idx)

def dict_to_android_xml(d, out_path):
    with open(out_path, 'w') as out_file:
        out_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
        out_file.write('<resources>\n')
        for key, text in d.items():
            key = key.replace('.', '_')
            # We need to increase a counter for every match
            text = re.sub(
                r'\{(\w+)\}',
                ReplaceCounter(),
                text,
            )
            text = cgi.escape(text)
            # Escape `'` with `\'`
            text = text.replace("'", "\\'")
            text = text.replace("\n", "\\n")
            out_file.write('  <string name="{}">{}</string>'.format(key, text))
            out_file.write('\n')
        out_file.write('</resources>\n')

def load_json(in_path):
    with open(in_path) as in_file:
        return json.load(in_file)

def parse_args():
    p = argparse.ArgumentParser(description='translations: CSV to KEYVALUEJSON')
    p.add_argument('--json', metavar='PATH', help='json input path', required=True)
    p.add_argument('--xml', metavar='PATH', help='android XML output path', required=True)
    opt = p.parse_args()
    return opt


def main():
    opt = parse_args()
    dict_to_android_xml(load_json(opt.json), opt.xml)
    print("{} written".format(opt.xml))

if __name__ == "__main__":
    main()
