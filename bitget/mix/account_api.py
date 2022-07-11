#!/usr/bin/python

from ..client import Client
from ..consts import (GET, POST, MIX_ACCOUNT_V1_URL)


class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def account(self, symbol, marginCoin):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/account', params)
        else:
            return "pls check args"

    def leverage(self, symbol, marginCoin, leverage, holdSide=''):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setLeverage', params)
        else:
            return "pls check args"

    def margin(self, symbol, marginCoin, amount, holdSide=''):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["amount"] = amount
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMargin', params)
        else:
            return "pls check args"

    def margin_mode(self, symbol, marginCoin, marginMode):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMarginMode', params)
        else:
            return "pls check args"

    def position_mode(self, symbol, marginCoin, holdMode):
        params = {}
        if symbol and marginCoin and holdMode:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["holdMode"] = holdMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setPositionMode', params)
        else:
            return "pls check args"

    def open_count(self, symbol, marginCoin, openPrice, openAmount, leverage=20):
        params = {}
        if symbol and marginCoin and openPrice and openAmount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["openPrice"] = openPrice
            params["openAmount"] = openAmount
            params["leverage"] = leverage
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/open-count', params)
        else:
            return "pls check args"

    def accounts(self, productType):
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accounts', params)
        else:
            return "pls check args"

    def accountBill(self, symbol,marginCoin,startTime,endTime,lastEndId = '',pageSize=20,iNext=False):
        params = {}
        if symbol and marginCoin and startTime and endTime:
            params['symbol'] = symbol
            params['marginCoin'] = marginCoin
            params['startTime'] = startTime
            params['endTime'] = endTime
            params['lastEndId'] = lastEndId
            params['pageSize'] = pageSize
            params['next'] = iNext
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accountBill', params)
        else:
            return "pls check args"
