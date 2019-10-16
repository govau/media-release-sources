#!/usr/bin/python

import csv
import sys

in_filename = ""
if len(sys.argv) == 2 or len(sys.argv) == 3:
    in_filename = str(sys.argv[1])
else:
    print('\n    Usage: python csv2opml.py csv_filename [opml_filename]\n')
    exit()
feeds = []
with open(in_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            feeds.append([row[0], row[1], row[2], row[3]])
        line_count += 1

feeds = sorted(feeds, key=lambda feed: feed[0])
portfolio = ""
if len(sys.argv) == 3:
    out_filename = str(sys.argv[2])
else:
    out_filename = in_filename.split('.')[0] + '.opml'
with open(out_filename, 'w') as opml_file:
    opml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    opml_file.write('<opml version="1.0">\n')
    opml_file.write('    <head>\n')
    opml_file.write('        <title>Australian Government Media Releases</title>\n')
    opml_file.write('    </head>\n')
    opml_file.write('    <body>\n')
    for row in feeds:
        if portfolio == "":
            portfolio = row[0]
            opml_file.write('        <outline text="Media Releases - ' + portfolio + '" title="Media Releases - ' + portfolio + '">\n')
        elif portfolio != row[0]:
            portfolio = row[0]
            opml_file.write('        </outline>\n')
            opml_file.write('        <outline text="Media Releases - ' + portfolio + '" title="Media Releases - ' + portfolio + '">\n')
        opml_file.write('            <outline type="rss" text="' + row[1] + '" title="' + row[1] + '" xmlUrl="' + row[2] + '" htmlUrl="' + row[3] + '"/>\n')
    opml_file.write('        </outline>\n')
    opml_file.write('    </body>\n')
    opml_file.write('</opml>\n')
