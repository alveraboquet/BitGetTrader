#!/usr/bin/python

from ..client import Client
from ..consts import (POST, GET, MIX_TRACE_V1_URL)


class TraceApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)


    def close_track_order(self, symbol, trackingNo):
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/closeTrackOrder', params)
        else:
            return "pls check args "


    def current_track(self, symbol, productType, pageSize=20, pageNo=1):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/currentTrack', params)
        else:
            return "pls check args "

    def history_track(self, startTime, endTime, pageSize=100, pageNo=1):
        params = {}
        if startTime and endTime:
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/historyTrack', params)
        else:
            return "pls check args "

    def summary(self):
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/summary')

    def profit_settle_margin_coin(self):
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/profitSettleTokenIdGroup')

    def profit_date_group(self, pageSize, pageNo):
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateGroupList', params)
        else:
            return "pls check args "

    def profit_date_detail(self, marginCoin, date, pageSize, pageNo):
        params = {}
        if marginCoin and date and pageSize and pageNo:
            params["marginCoin"] = marginCoin
            params["date"] = date
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateList', params)
        else:
            return "pls check args "

    def wait_profit_detail(self, pageSize, pageNo):
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/waitProfitDateList', params)
        else:
            return "pls check args "

    def follower_history_orders(self, page_size, page_no, start_time, end_time):
        params = {}
        if page_size and page_no:
            params["pageSize"] = page_size
            params["pageNo"] = page_no

        if start_time and end_time:
            params["startTime"] = start_time
            params["endTime"] = end_time

        return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerHistoryOrders', params)
