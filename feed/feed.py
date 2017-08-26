#!/usr/bin/env python
# coding: utf-8

import re
import sys
import codecs
from datetime import datetime
import feedparser


def read_feed_list(filepath):
    return open(filepath, 'r').readlines()


def read_feeds(urls):
    return map(feedparser.parse, urls)


def merge_last_entries(feeds):
    entries = []
    for feed in feeds:
        entries.append((feed.feed, feed['items'][0]))
    return sorted(entries, key=lambda entry: entry[1]["published"], reverse=True)


def format_entry(tmpl, feed, entry):
    summary_max_length = 80
    summary_text = re.sub('<[^<]+?>', '', entry.summary)
    if len(summary_text) > summary_max_length:
        summary_text = summary_text[:summary_max_length] + '...'
    publish_date = datetime.strptime(entry.published[:19], '%Y-%m-%dT%H:%M:%S').strftime('%d/%m/%Y %H:%M')
    return tmpl.format(feed=feed, entry=entry, summary=summary_text, publish_date=publish_date)


input_url_list = sys.argv[1]
output_html = sys.argv[2]

urls = read_feed_list(input_url_list)
feeds = read_feeds(urls)
entries = merge_last_entries(feeds)
tmpl = codecs.open('feed-entry-tmpl.html', 'r', 'utf-8').read()

with codecs.open(output_html, 'w', 'utf-8') as out_html:
    for feed, entry in entries:
        print('Processing {}'.format(feed.link))
        out_html.write(format_entry(tmpl, feed, entry))
