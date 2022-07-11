#!/usr/bin/python

from ..client import Client
from ..consts import (POST, GET, MIX_ORDER_V1_URL)


class OrderApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def place_order(self, symbol, marginCoin, size, side, orderType, price='', clientOrderId='', timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and side and orderType and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["price"] = price
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["timeInForceValue"] = timeInForceValue
            params["clientOrderId"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/placeOrder', params)
        else:
            return "pls check args "

    def batch_orders(self, symbol, marginCoin, order_data):
        params = {'symbol': symbol, 'marginCoin': marginCoin, 'orderDataList': order_data}
        return self._request_with_params(POST, MIX_ORDER_V1_URL + '/batch-orders', params)

    def cancel_orders(self, symbol, marginCoin, orderId):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-order', params)
        else:
            return "pls check args "

    def cancel_batch_orders(self, symbol, marginCoin, orderIds):
        if symbol and orderIds:
            params = {'symbol': symbol, 'marginCoin':marginCoin, 'orderIds': orderIds}
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-batch-orders', params)
        else:
            return "pls check args "

    def detail(self, symbol, orderId):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/detail', params)
        else:
            return "pls check args "

    def current(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/current', params)
        else:
            return "pls check args "

    def history(self, symbol, startTime, endTime, pageSize, lastEndId='', isPre=False):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/history', params)
        else:
            return "pls check args "

    def fills(self, symbol='', orderId=''):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/fills', params)
        else:
            return "pls check args "