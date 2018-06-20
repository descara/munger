#
# ParseFeed
# Author: Reuben Joseph <reubenej@gmail.com>
#
# -*- coding:utf-8 -*-

import feedparser
import json
import os.path

# Basic configuration details
ROOT_DIR = os.path.dirname(os.path.abspath('conf/'))
CONFIG_PATH = os.path.join(ROOT_DIR, 'conf/feeds.conf')

def read_config():
    config = []
    file = open(CONFIG_PATH, "r")
    for line in file:
        config.append(line)

    return config

# Takes an rss feed as input and returns the list of articles
def fetch_feed(feed):
    rss = feedparser.parse(feed)
    articles = rss['feed']['title']
    return articles

def main():
    feeds = read_config()
    # print(type(feeds))
    print(fetch_feed(feeds[1]))
    print(fetch_feed(feeds[2]))



if __name__ == "__main__":
    main()
