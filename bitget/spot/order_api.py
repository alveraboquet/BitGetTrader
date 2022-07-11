#!/usr/bin/python
from ..client import Client
from ..consts import (POST, SPOT_ORDER_V1_URL)


class OrderApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def orders(self, symbol, quantity, side, orderType, force, price='', clientOrderId=''):
        params = {}

        if symbol and quantity and side and orderType and force:
            params["symbol"] = symbol
            params["price"] = price
            params["quantity"] = quantity
            params["side"] = side
            params["orderType"] = orderType
            params["force"] = force
            params["clientOrderId"] = clientOrderId
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/orders', params)
        else:
            return "pls check args "

    def batch_orders(self, symbol, order_data):
        params = {'symbol': symbol, 'orderList': order_data}
        return self._request_with_params(POST, SPOT_ORDER_V1_URL + "/batch-orders", params)

    def cancel_orders(self, symbol, orderId):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/cancel-order', params)
        else:
            return "pls check args "

    def cancel_batch_orders(self, symbol, orderIds):
        if symbol and orderIds:
            params = {'symbol': symbol, 'orderIds': orderIds}
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/cancel-batch-orders', params)
        else:
            return "pls check args "

    def order_info(self, symbol, orderId='', clientOrderId=''):
        params = {}
        if clientOrderId:
            params["clientOrderId"] = clientOrderId
        if symbol:
            params["symbol"] = symbol

        if orderId:
            params["orderId"] = orderId
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/orderInfo', params)
        else:
            return "pls check args "

    def open_order(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/open-orders', params)
        else:
            return "pls check args "

    def history(self, symbol, after='', before='', limit=100):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/history', params)
        else:
            return "pls check args "

    def fills(self, symbol='', orderId='', after='', before='', limit=100):
        params = {}
        if symbol:
            params["symbol"] = symbol
        if orderId:
            params["orderId"] = orderId
        if after:
            params["after"] = after
        if before:
            params["before"] = before
        if limit:
            params["limit"] = limit


        print(params)
        return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/fills', params)