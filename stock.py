#!/usr/bin/env python
# coding=utf-8
#http://tushare.org/trading.html#id4

import tushare as ts
from wxpy import *

bot = Bot()

stock_list = [
        {"code":"002341","im":"金磊", "high_threshold":7.5, "low_threshold":5.0},
        {"code":"000070","im":"金磊", "high_threshold":7.5, "low_threshold":5.0},
            ]
for i in range(0,len(stock_list)):
    #print((stock_list[i]["code"]))
    data = ts.get_realtime_quotes(stock_list[i]["code"])
    if data.at[0, "price"] > stock_list[i]["high_threshold"]:
        str = "股票:%s  当前价格:%s 开盘价:%s 最高价:%s 最低价:%s "%(data.at[0,"name"], data.at[0, "price"], data.at[0, "open"], data.at[0, "high"], data.at[0, "low"])
        notify = bot.friends().search(stock_list[i]["im"])
        notify.send(str)
