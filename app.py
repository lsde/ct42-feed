#!/usr/bin/env -S python3 -u

from bs4 import BeautifulSoup
import argparse
import os
import requests
import time

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL to page with a feed')
parser.add_argument('-s', '--sleep', type=int, default=30)
args = parser.parse_args()

global old_msg
livetext_url = BeautifulSoup(requests.get(args.url), 'html.parser').find(class_='livetext').iframe['src']

while True:
    r = requests.get(livetext_url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    when = soup.find('dt').p.get_text()
    what = soup.find('dd').p.get_text()

    msg = when + what
    if msg != old_msg:
        os.system('notify-send "{0} : {1}"'.format(when, what))
    old_msg = msg

    time.sleep(args.sleep)

