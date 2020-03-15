#!/usr/bin/env -S python3 -u

from bs4 import BeautifulSoup
import argparse
import os
import requests
import time
import traceback

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL to page with a feed', required=True)
parser.add_argument('-s', '--sleep', type=int, help='Refresh time', default=30)
args = parser.parse_args()

old_msg = ''

try:
    r = requests.get(args.url, allow_redirects=True)
    assert r.status_code < 400, "ERROR: HTTP status code {0} for URL {1}".format(r.status_code, r.url)
    livetext_url = BeautifulSoup(r.text, 'html.parser').find(class_='livetext').iframe['src']

    while True:
        r = requests.get(livetext_url, allow_redirects=True)
        assert r.status_code < 400, "ERROR: HTTP status code {0} for URL {1}".format(r.status_code, r.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        when = soup.find('dt').p.get_text()
        what = soup.find('dd').p.get_text()

        msg = when + what
        if msg != old_msg:
            os.system('notify-send "{0}" "{1} : {2}"'.format(what[:68], when, what))
        old_msg = msg

        time.sleep(args.sleep)
except KeyboardInterrupt:
    exit(0)
except Exception as err:
    traceback.print_exc()
    exit(1)

