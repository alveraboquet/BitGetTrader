#!/usr/bin/python

from ..client import Client
from ..consts import (GET, MIX_MARKET_V1_URL)


class MarketApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def contracts(self, productType):
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/contracts', params)

    def depth(self, symbol, limit='150'):
        params = {}
        if symbol and limit and type:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/depth', params)
        else:
            return "pls check args"

    def ticker(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/ticker', params)
        else:
            return "pls check args"

    def tickers(self,productType):
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/tickers', params)

    def fills(self, symbol, limit=100):
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/fills', params)
        else:
            return "pls check args"

    def candles(self, symbol, granularity, startTime='', endTime='', iPrint=False):
        params = {}
        if symbol and granularity:
            params["symbol"] = symbol
            params["granularity"] = granularity
            params["startTime"] = startTime
            params["endTime"] = endTime
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/candles', params, iPrint)
        else:
            return "pls check args"

    def index(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/index', params)
        else:
            return "pls check args"

    def funding_time(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/funding-time', params)
        else:
            return "pls check args"

    def market_price(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/mark-price', params)
        else:
            return "pls check args"

    def history_fund_rate(self, symbol, pageSize=20, pageNo=1, nextPage=False):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            params["nextPage"] = nextPage
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/history-fundRate', params)
        else:
            return "pls check args"

    def current_fund_rate(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/current-fundRate', params)
        else:
            return "pls check args"

    def open_interest(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/open-interest', params)
        else:
            return "pls check args"
