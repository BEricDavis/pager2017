#!/usr/bin/env python
# This is the main script for creating a PagerDuty report

import logging
import json
import argparse
import datetime as dt
from collections import defaultdict

log_level = 'DEBUG'
def main():
    configure_logging(log_level)
    load_config()

def configure_logging(level):
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    logging.basicConfig(level=level,
                        format='%(asctime)s %(levelname)s %(funcName)s: %(lineno)d %(message)s')

def load_config():
    # read a config file to retrieve the domain and the schedules
    with open('conf/pd_info.json') as config:
        config_json = json.load(config)
        URL = config_json['Config']['URL']
        services = config_json['Service']

    logging.debug(f'URL: {URL}')
    logging.debug(f'services: {services}')

if __name__ == '__main__':
    main()