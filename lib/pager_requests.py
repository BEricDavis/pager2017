import requests
import logging
import sys

class PagerRequests:
    def __init__(self, pd_domain):
        self.DOMAIN = pd_domain
        self.APIKEY = open('../conf/apikey.txt').read().rstrip()
        self.HEADERS = {
            'Authorization': 'Token token={0}'.format(self.APIKEY),
            'Content-type': 'application/json',
        }

    def call(self, uri, payload):
        """
        Given a properly formatted uri and payload, make a request to pagerduty.com and return the JSON-formatted
        response.
        :param pd_domain: The company-specific PagerDuty domain.  ex. mycompany.pagerduty.com
        :param uri: A properly-formatter uri. Ex: --put one here--
        :param payload: A PagerDuty payload.
        :return: A JSON response
        """
        try:
            url = f"https://{self.DOMAIN}/{uri}/{payload}"
            logging.debug(f'url: {url}')
            response = requests.get(url=url, headers=self.HEADERS).json()
            return response
        except Exception as e:
            logging.error(str(e))
            sys.exit()
