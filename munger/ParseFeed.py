#
# ParseFeed
# Author: Reuben Joseph <reubenej@gmail.com>
#
# -*- coding:utf-8 -*-

import feedparser
import json
import os.path
#import configparser

# Basic configuration details
ROOT_DIR = os.path.dirname(os.path.abspath('conf/'))
CONFIG_PATH = os.path.join(ROOT_DIR, 'conf/feeds.conf')

def main():
    with open(CONFIG_PATH) as file:
        feed_config = json.loads(file.read())

    print(feed_config['*']['link'].values())

if __name__ == "__main__":
    main()
