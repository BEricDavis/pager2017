#!/usr/bin/env python
# This is the main script for creating a PagerDuty report

import logging
import json
import argparse
import datetime as dt
from lib import PDSchedule as pds
from lib import DateTimeHandler as dth
from collections import defaultdict

log_level = 'DEBUG'
sod = dt.time(hour=0, minute=0, second=0)
eod = dt.time(hour=23, minute=59, second=59)
default_start = '20170101'
default_end = '20170331'

def main(start=default_start, end=default_end):
    configure_logging(log_level)
    domain, services = load_config()

    # TODO: maybe delay this conversion until after chunking, as we immediately turn the strings back to dt objs
    pd_start = dth.convert_to_pd_date(start, sod)
    pd_end = dth.convert_to_pd_date(end, eod)

    periods = dth.chunk_periods(pd_start, pd_end)



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