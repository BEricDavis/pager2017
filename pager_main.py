#!/usr/bin/env python
# This is the main script for creating a PagerDuty report

import logging
import json
import argparse
import datetime as dt
from collections import defaultdict

log_level = 'DEBUG'
sod = dt.time(hour=0, minute=0, second=0)
eod = eod = dt.time(hour=23, minute=59, second=59)
default_start = '20170101'
default_end = '20170331'

def main():
    configure_logging(log_level)
    domain, services = load_config()



def configure_logging(level):
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    logging.basicConfig(level=level,
                        format='%(asctime)s %(levelname)s %(funcName)s: %(lineno)d %(message)s')
    logging.info(f'setting log level to {level}')


def load_config():
    """
    Read a config file to retrieve the PagerDuty domain and the services
    :return url as a string, services as a dict
    """
    with open('conf/pd_info.json') as config:
        config_json = json.load(config)
        domain = config_json['Config']['URL']
        services = config_json['Service']

    logging.debug(f'setting domain: {domain}')
    logging.debug(f'setting services: {services}')
    return domain, services



if __name__ == '__main__':
    main()