import requests
import logging
import sys

class PagerRequests:
    def __init__(self):
        self.APIKEY = open('../conf/apikey.txt').read().rstrip()
        self.HEADERS = {
            'Authorization': 'Token token={0}'.format(self.APIKEY),
            'Content-type': 'application/json',
        }

    def call(self, domain, context, payload):
        """
        Given a properly formatted domain, context, and payload, make a request to pagerduty.com and return the JSON-formatted
        response.
        :param domain: The company-specific PagerDuty domain.  ex. mycompany.pagerduty.com
        :param context: A properly-formatted uri. ex: --put one here--
        :param payload: A PagerDuty payload.
        :return: A JSON response
        """
        try:
            url = f"https://{domain}/{context}/{payload}"
            logging.debug(f'url: {url}')
            response = "response"
            #response = requests.get(url=url, headers=self.HEADERS).json()
            return response
        except Exception as e:
            logging.error(str(e))
            sys.exit()
