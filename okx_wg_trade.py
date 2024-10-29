from coin_trade import *
import time


def wg_trade(data: dict):

    api = data.get("api")
    api_key = data.get("api_key")
    password = data.get("password")
    flag = data.get("flag")
    flag = bool_to_str(flag)
    open_long = data.get("open_long")
    open_short = data.get("open_short")
    symbol = data.get("symbol")
    peice = data.get("peice")
    peice_lit = data.get("peice_lit")
    percent_add = data.get("percent_add")
    percent_out = data.get("percent_out")
    tp_profits =data.get("tp_profits")
    sl_profits = data.get("sl_profits")

    cn = coin_trade(api, api_key, password, flag, symbol)
    ask_mark, bid_mark = 0,0

    initialize = 0  # 初始化
    while initialize == 0:
        try:
            cn.set_two_way_position()
            cn.set_levers(10)
            ask_mark,bid_mark = cn.ask_bid()
            initialize = 1
            print('初始化========成功')
        except:
            initialize = 0
            time.sleep(0.5)
            print('初始化=========错误,再次尝试')
    while 1:
        try:
            # 获取买一价 卖一价
            ask, bid = cn.ask_bid()
            # 获取持仓信息
            result = cn.get_position_information()
            long_peices = cn.get_long_position_peices(result)
            short_peices = cn.get_short_position_peices(result)
            long_prices = cn.get_long_position_prices(result)
            short_prices = cn.get_short_position_prices(result)

            long_profits = cn.get_positon_information(result, 'long', key='upl')
            short_profits = cn.get_positon_information(result, 'short', key='upl')
            # 没有持仓现价开一单
            long_first = open_long and long_peices == 0
            # 有持仓满足跌幅加一单
            long_next = open_long and long_peices < peice_lit and ask < ask_mark*(1 - percent_add)
            short_first = open_short and short_peices == 0
            short_next = open_short and short_peices < peice_lit and bid > bid_mark*(1 + percent_add)
            # 持仓均价百分比平仓  盈利金额平仓 亏损金额平仓

            close_long1 = percent_out > 0 and ask > long_prices * (1 + percent_out)
            close_long2 = tp_profits > 0 and long_profits > tp_profits
            close_long3 = sl_profits < 0 and long_profits < sl_profits
            close_long = close_long1 or close_long2 or close_long3

            close_short1 = percent_out > 0 and bid < short_prices * (1 - percent_out)
            close_short2 = tp_profits > 0 and short_profits > tp_profits
            close_short3 =  sl_profits < 0 and short_profits < sl_profits
            close_short = close_short1 or close_short2 or close_short3

            # 平多空
            if close_long:
                cn.close_long(long_peices)

            if close_short:
                cn.close_short(short_peices)

            if long_first:
                cn.open_buy(peice)
                ask_mark = ask
            if short_first:
                cn.open_sell(peice)
                bid_mark = bid

            if long_next:
                cn.open_buy(peice)
                ask_mark = ask
            if short_next:
                cn.open_sell(peice)
                bid_mark = bid

            print(cn.get_symbol(), ask,bid)
            print(long_peices,short_peices,long_prices,short_prices)

        except:
            time.sleep(0.3)
        time.sleep(0.3)

if __name__ == '__main__':

    api = "6e73c2c1-226b-446f-8c14-dd39c8fc25b7"
    api_key = "CA2E8A0AC53961D8B04D5A2EE71E9883"
    password = "Ccmy-0622"
    flag = True
    open_long = True
    open_short = True
    symbol = "ETH-USDT-SWAP"
    peice = 1
    peice_lit = 100
    percent_add = 0.0003
    percent_out = 0.003
    tp_profits = 100
    sl_profits = -100

    data = {"api": api,
            "api_key": api_key,
            "password": password,
            "flag": flag,
            "open_long": open_long,
            "open_short": open_short,
            "symbol": symbol,
            "peice": peice,
            "peice_lit": peice_lit,
            "percent_add": percent_add,

            "percent_out": percent_out,
            "tp_profits": tp_profits,
            "sl_profits": sl_profits}

    wg_trade(data)
