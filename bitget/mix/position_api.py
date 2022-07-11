#!/usr/bin/python

from ..client import Client
from ..consts import (GET, MIX_POSITION_V1_URL)


class PositionApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def single_position(self, symbol, marginCoin):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/singlePosition', params)
        else:
            return "pls check args"

    def all_position(self, productType, marginCoin):
        params = {}
        if productType:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/allPosition', params)
        else:
            return "pls check args"