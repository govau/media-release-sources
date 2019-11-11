# Australian Government Media Releases
> The purpose of this repository is to track sources of Australian Government media releases.

Online sources are tracked in a CSV file which can be converted to OPML. The OPML file can be imported into feed readers such as [Feedly](https://feedly.com/) or Microsoft Outlook. The outcome is a feed of the most recent media releases from the available sources.

## Usage

### View recent media releases

Use converters/csv2opml.py to convert the current CSV file into an OPML file.
```python
python csv2opml.py ../media-release-rss.csv
```

Use the newly created OPML file in your feed reader.

In Feedly you can upload using [feedly.com/i/cortex](https://feedly.com/i/cortex)

![Feedly upload: Choose OPML file or drag OPML file here](/docs/images/feedly01.png)
![Feedly upload: New sources successfully added to Feedly from media-release-rss.opml](/docs/images/feedly02.png)
![Feedly upload: All personal feeds showing newly added media releases](/docs/images/feedly03.png)

Note: You can view which Australian Government websites the media releases are coming from in the media-release-rss.csv file.

### Update the sources

The media-release-rss.csv file can be updated to include any missing Australian Government RSS feeds that contain media releases.

When updating:
1. All fields should be encapsulated in double quotes (") and seperated by a comma (,)
2. Each line should have 5 fields:
    - Portfolio<br />The name of the ministry portfolio the feed belongs to.
    - Feed name<br />The name of the individual feed.
    - Feed URL<br />The address of the RSS feed containing the media releases.
    - HTML URL<br />The address where the media releases can be viewed on the website.
    - Notes<br />Any notes concerning the content of the feed (for example if the feed may contain non-media release items).

The parsers/rssparser.py file will read a CSV file containing RSS feeds with all necessary fields, fetch all of the items from each of the feeds and output some of the key details from each item.
```python
python rssparser.py csv_filename
```

## Future development

1. Updates to media-release-rss.csv will trigger csv2opml.py to be run against it and the resulting OPML file will be updated in the repository.
2. Subscription service for media releases. Initial designs can be viewed in the "ui" folder.

![User interface design for subscribing to Australian Government media releases as seen in ui/subscribe.html](/docs/images/ui.png)

## Guidance for publishing your media releases

Optimising your media releases by including metadata helps to make it more discoverable. This metadata can be used in future developments.

### Benefits of including metadata with your media releases

- Your audience can find your media releases more easily through search engines.
- Third-party aggregators can help their audiences to find your media releases by:
    - delivering content based on their needs
    - providing a summary of the media release
    - providing detailed filtering options
    - highlighting important information

### What metadata to include

- title of media release
- description of content
- key topics addressed 
- publication date
- revised date
- authorised by
- location
- contact details for enquiries

### How to include metadata

Use standard terms to include metadata with each media release. Best practice standards are shown here, using extension values for the HTML meta tag from [the Web Hypertext Application Technology Working Group (WHATWG)](https://wiki.whatwg.org/wiki/MetaExtensions).

Include metadata in the head of the HTML page using these meta tag names:

```html
<!-- title of media release -->
<meta name="dc.title" content="Title of this media release">
<!-- description of content -->
<meta name="description" content="This is a description of the content in the media release.">
<!-- key topics addressed  -->
<meta name="keywords" content="keyword1, keyword2, keyword3, keyword4">
<!-- publication date -->
<meta name="dc.created" content="Tuesday, October 15th, 2019, 9:22 am">
<!-- revised date -->
<meta name="dc.modified" content="Thursday, October 17th, 2019, 11:15 am">
<!-- authorised by -->
<meta name="dc.creator" content="Name of Minister">
<!-- location -->
<meta name="dcterms.coverage" content="Location covered by media release">
<!-- contact details for enquiries -->
<meta name="contact" content="Government agency, email@agency.gov.au">
```

Best practice is to include this data in an RSS feed of your media releases.

## Disclaimer

Guidance provided in this repository is not official policy of the Australian Government or the Digital Transformation Agency.

## Authors

- [Gordon Grace](https://github.com/gordongrace)
- [Toby Harper](https://github.com/tobyfu)
- [Anthony McKerron](https://github.com/anthonymckerron)
- [Igor Nedeski](https://github.com/nedeskiigor)
- [Kate Newbown](https://github.com/kNewbown)