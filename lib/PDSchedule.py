import logging
import datetime as dt
from pytz import timezone
from lib import pager_requests as pd
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
    def get_schedule(start, end, id):
        """
        retrieve the scheedule from PagerDuty
        :return:
        """
        context = f"/api/v1/schedules/{id}/entries"
        logging.debug(f'context: {context}')
        payload = f"?since={start}&until={end}&overflow=true"
        logging.debug(f'payload: {payload}')

        schedule = pd.call()
        return schedule


