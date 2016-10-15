"""
A rather simplistic wrapper around Slack's API, kinda bad not gonna lie.
"""

import sys
import urllib
import requests

BASE = "https://slack.com/api/{}"

class Slack(object):
    """
    A wrapper around requests to make accessing the Slack API easier
    """
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.session = requests.Session()
        python_v = "{0}.{1}.{2} {3}".format(sys.version_info.major,
                                            sys.version_info.minor,
                                            sys.version_info.micro,
                                            sys.platform)
        request_v = requests.__version__
        self.session.headers.update({
            "User-Agent": "Karen's ReactSpammer v0.0.1 (Python {0}, Requests {1})".format(python_v,
                                                                                          request_v)
        })
    def __send_req__(self, endpoint, method, **kwargs):
        # I know slack only allows 2 really, but I just don't care anymore
        if method.lower() in ['get', 'post', 'head', 'options']:
            func = getattr(self.session, method)
            url = BASE.format(endpoint)
            resp = func("{0}?{1}".format(url, urllib.urlencode(kwargs)))
            return resp
    # From here on out we only really need for our reaction spamming
    def emoji_list(self):
        """
        Lists all emoji for a given team.
        """
        resp = self.__send_req__('emoji.list', 'get', token=self.auth_token)
        return resp.json()
    def add_response(self, name):
        """
        Adds a response to something.
        """
        raise NotImplementedError()
    def channel_list(self, exclude_archived=0):
        """
        Lists all channels for a given team
        """
        resp = self.__send_req__('channels.list', 'get', exclude_archived=exclude_archived)
        return resp.json()
