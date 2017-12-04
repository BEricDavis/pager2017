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
    :param start: The yyyy-mm-dd of the starting day.  Method assumes start time of 00:00:00
    :param end: The yyyy-mm-dd of the endind day.  Method assumes end time of 23:59:59
    :return: Tuple with pairs of datetime objects representing the start and end of each period.
    """
    pass


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