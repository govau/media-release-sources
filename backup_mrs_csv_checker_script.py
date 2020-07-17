import requests
import csv

# To Run:
# Open CLI and enter python backup_mrs_csv_checker_script.py

def rss_feeds():
    rssFeeds = []

    with open('rss_feeds.csv') as f:
        f_csv = csv.reader(f)

        for row in f_csv:
            rssFeeds.append(row[2])

    rssFeeds.remove(rssFeeds[0])

    return rssFeeds


def url_ok(url):
    r = requests.head(url)

    return r.status_code


def check_urls():
    rss = rss_feeds()
    successUrls = []
    redirectUrls = []
    errorUrls = []
    serverErrorUrls = []
    response = ""

    for row in rss:
        code = url_ok(row)
        stringCode = str(code)

        if stringCode.startswith('2'):
            successUrls.append(row)

        if stringCode.startswith('3'):
            redirectUrls.append(row.strip())

        if stringCode.startswith('4'):
            errorUrls.append(row.strip())

        if stringCode.startswith('5'):

            serverErrorUrls.append(row.strip())

    response = "Valids: " + str(len(successUrls)) + ", Redirects: " + \
        str(len(redirectUrls)) + ", Errors: " + str(len(errorUrls)) + \
        ", Server errors: " + str(len(serverErrorUrls))

    if len(errorUrls) != 0:
        response = response + "\n 3XXs: " + (str(redirectUrls)[1:-1]) + "\n"

    if len(errorUrls) != 0:
        response = response + " 4XXs: " + (str(errorUrls)[1:-1]) + "\n"

    if len(serverErrorUrls) != 0:
        response = response + " 5XXs: " + str(serverErrorUrls)[1:-1]

    if len(redirectUrls) == 0 and len(serverErrorUrls) == 0 \
            and len(errorUrls) == 0:
        response = response + "All URLs valid."

    return (response)

print (check_urls())
