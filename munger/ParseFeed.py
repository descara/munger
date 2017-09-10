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

def read_config(file):
    feed_config = json.loads(open(file).read())
    return feed_config


read_config(CONFIG_PATH)

