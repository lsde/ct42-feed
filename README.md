# CT42 Feed

## About
Show CT42 feed as desktop notifications on Linux. Takes webpage URL on which the feed is present.

## Requirements
    libnotify
    python >= 3
    BeautifulSoup4
    pyton-requests

## Usage
    $ virtualenv venv
    ..
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ..
    $ ./ct42-feed.py -h
    usage: ct42-feed.py [-h] [-u URL] [-s SLEEP]

    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     URL to page with a feed
      -s SLEEP, --sleep SLEEP
                            Refresh time
 
    $ ./ct42-feed.py -u https://ct24.ceskatelevize.cz/specialy/3037207-koronavirus
    