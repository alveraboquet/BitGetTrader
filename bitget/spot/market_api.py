#!/usr/bin/python

from ..client import Client
from ..consts import (GET, SPOT_MARKET_V1_URL)


class MarketApi(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def fills(self, symbol, limit=100):
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/fills', params)
        else:
            return "pls check args"

    def depth(self, symbol, limit='150', iType='step0'):
        params = {}
        if symbol and limit and iType:
            params["symbol"] = symbol
            params["limit"] = limit
            params["type"] = iType
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/depth', params)
        else:
            return "pls check args"

    def ticker(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/ticker', params)
        else:
            return "pls check args"

    def tickers(self):
        return self._request_without_params(GET, SPOT_MARKET_V1_URL + '/tickers')

    def candles(self, symbol, period, after='', before='', limit=100):
        params = {}
        if symbol and period:
            params["symbol"] = symbol
            params["period"] = period
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/candles', params)
        else:
            return "pls check args"