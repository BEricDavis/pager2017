import logging
import datetime as dt
from pytz import timezone

def chunk_period(self):
    pass

def convert_to_pd_date(date_string, pd_time):
    """
    Given a string yyyymmdd, convert it to the date format expected by PagerDuty: 2016-01-08T09:00:00-05:00
    :param date_string: A string of digits in the format yyyymmdd representing a date
    :return: A string formatted as PagerDuty expects: yyyy-mm-ddTHH:MM:SS-TZ
    """
    logging.debug(f'date string received: {date_string}')
    pd_date = dt.date(int(date_string[0:4]),
                      int(date_string[4:6]),
                      int(date_string[6:8]))
    pd_date = dt.datetime.combine(pd_date, pd_time)
    pd_date = make_tz_aware(pd_date)
    logging.debug(f'new tz-aware dt object: {pd_date}')
    pd_date = pd_date.strftime('%Y-%m-%dT%H:%M:%S%z')
    logging.debug(f'returning {pd_date}')

    return pd_date


def chunk_periods(start, end):
    """
    Break the request duration into monthly periods.
    :param start: String representation of a datetime in pagerduty format
    :param end: String representation of a datetime in pagerduty format
    :return: Tuple with pairs of datetime objects representing the start and end of each period.
    """

    logging.debug(f'chunking {start} to {end}')
    # convert the strings to datetime objects
    #start = dt.datetime.strptime(''.join(start.rsplit(':', 1)), '%Y-%m-%dT%H:%M:%S-%z')
    start = dt.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S-%z')
    logging.debug(f'start: {start}')
    periods = []

    # if the year and month of the period are the same, just return the dates as we got them



    return periods


def make_tz_aware(local_dt):
    """
    Make a local DateTime object timezone aware with pytz.timezone
    :param local_dt:
    :return:
    """
    aware_dt = timezone('US/Eastern').localize(local_dt)
    return aware_dt


def local_to_utc(localtime, offset):
    return localtime + dt.timedelta(hours=offset)


def utc_to_local(utc, offset):
    return utc - dt.timedelta(hours=offset)