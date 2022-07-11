#!/usr/bin/python

from ..client import Client
from ..consts import (SPOT_ACCOUNT_V1_URL, POST, GET)


class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def assets(self):
        return self._request_without_params(GET, SPOT_ACCOUNT_V1_URL + '/assets')

    def bills(self, coinId='', groupType='', bizType='', after='', before='', limit=100):
        params = {}

        if coinId:
            params["coinId"] = coinId
        if groupType:
            params["groupType"] = groupType
        if bizType:
            params["bizType"] = bizType
        if after:
            params["after"] = after
        if before:
            params["before"] = before


        params["limit"] = limit
        return self._request_with_params(POST, SPOT_ACCOUNT_V1_URL + '/bills', params)