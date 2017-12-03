import logging
import datetime as dt
import json
from collections import defaultdict
import calendar

class PDSchedule:
    def __init__(self, start, end, schedule_id):
        self.START = self.convert_to_pd_date(start)
        logging.debug(f"START set to: {self.START}")

        self.END = self.convert_to_pd_date(end)
        logging.debug(f"END set to {self.END}")

    @staticmethod
    def convert_to_pd_date(date_string):
        """
        Given a string yyyymmdd, convert it to the date format expected by PagerDuty: 2016-01-08T09:00:00-05:00
        :param date_string: A string of digits in the format yyyymmdd representing a date
        :return: A date formatted as PagerDuty expects: yyyy-mm-dd
        """
        logging.debug(f'date string received: {date_string}')
        pd_date = dt.date(int(date_string[0:4]),
                          int(date_string[4:6]),
                          int(date_string[6:8]))
        return pd_date
