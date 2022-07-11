#!/usr/bin/python

from ..client import Client
from ..consts import (POST, GET, MIX_PLAN_V1_URL)


class PlanApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def place_plan(self, symbol, marginCoin, size, side, orderType, triggerPrice, triggerType, executePrice='', clientOrderId='', timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and side and orderType and triggerPrice and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["triggerPrice"] = triggerPrice
            params["executePrice"] = executePrice
            params["triggerType"] = triggerType
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["timeInForceValue"] = timeInForceValue
            params["clientOrderId"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placePlan', params)
        else:
            return "pls check args "

    def modify_plan(self, symbol, marginCoin, orderId, orderType, triggerPrice, triggerType, executePrice=''):
        params = {}
        if symbol and marginCoin and orderType and orderId and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["triggerPrice"] = triggerPrice
            params["executePrice"] = executePrice
            params["triggerType"] = triggerType
            params["orderType"] = orderType
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlan', params)
        else:
            return "pls check args "

    def modify_plan_preset(self, symbol, marginCoin, orderId, planType='normal_plan', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and orderId and planType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["orderId"] = orderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlanPreset', params)
        else:
            return "pls check args "

    def modify_tpsl_plan(self, symbol, marginCoin, orderId, triggerPrice ):
        params = {}
        if symbol and marginCoin and orderId and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["triggerPrice"] = triggerPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyTPSLPlan', params)
        else:
            return "pls check args "

    def place_tpsl(self, symbol, marginCoin, triggerPrice, planType, holdSide ):
        params = {}
        if symbol and marginCoin and planType and holdSide and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["holdSide"] = holdSide
            params["triggerPrice"] = triggerPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placeTPSL', params)
        else:
            return "pls check args "

    def cancel_plan(self, symbol, marginCoin, orderId, planType):
        params = {}
        if symbol and marginCoin and planType and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/cancelPlan', params)
        else:
            return "pls check args "

    def current_plan(self, symbol, isPlan='plan'):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/currentPlan', params)
        else:
            return "pls check args "

    def history_plan(self, symbol, startTime, endTime, pageSize, lastEndId='', isPre=False, isPlan='plan'):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/historyPlan', params)
        else:
            return "pls check args "
