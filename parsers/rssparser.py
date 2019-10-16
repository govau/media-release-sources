import feedparser
import string
import pytz
import csv
import sys
from dateutil import parser

in_filename = ""
if len(sys.argv) == 2:
    in_filename = str(sys.argv[1])
else:
    print('\n    Usage: python rssparser.py csv_filename\n')
    exit()

feeds = []
with open(in_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row)
        else:
            feeds.append([row[0], row[1], row[2], row[3]])
        line_count += 1

releases = []

for row in feeds:
    feed = feedparser.parse( row[2] )
    feed = feed[ "items" ]
    for release in feed:
        if "twitter" not in release[ "link" ]:
            release[ "portfolio" ] = row[0]
            release[ "published_datetime"] = parser.parse( release[ "published" ] )
            if release[ "published_datetime" ].tzinfo is None:
                release[ "published_datetime" ] = pytz.utc.localize(release[ "published_datetime" ])
            releases.append(release)

sorted_releases = sorted( releases, key=lambda release: release[ "published_datetime" ] )

for release in sorted_releases:
    if "twitter" not in release[ "link" ]:
        print( release[ "published_datetime" ].strftime("%d/%m/%Y, %H:%M:%S") + " - " + string.ljust(release[ "portfolio" ], 15) + " - " + release[ "title" ] + " - " + release[ "link" ])
