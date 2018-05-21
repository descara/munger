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

def main():
    file = open(CONFIG_PATH, 'r')
    feed_config = json.loads(open(file).read())
    print(feed_config)

if __name__ == "__main__":
    main()
