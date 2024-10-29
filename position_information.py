from coin_trade import *

def information(data: dict):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)

        # 获取买一价 卖一价
        ask, bid = cn.ask_bid()
        # 获取持仓信息
        result = cn.get_position_information()

        long_peices = cn.get_long_position_peices(result)
        long_markPx = cn.get_positon_information(result, 'long', key='markPx')
        long_prices = cn.get_long_position_prices(result)
        long_profits = cn.get_positon_information(result, 'long', key='upl')
        long_liqPx = cn.get_positon_information(result, 'long', key='liqPx')
        long_imr = cn.get_positon_information(result, 'long', key='imr')

        short_peices = cn.get_short_position_peices(result)
        short_markPx = cn.get_positon_information(result, 'short', key='markPx')
        short_prices = cn.get_short_position_prices(result)
        short_profits = cn.get_positon_information(result, 'short', key='upl')
        short_liqPx = cn.get_positon_information(result, 'short', key='liqPx')
        short_imr = cn.get_positon_information(result, 'short', key='imr')

        sum_peice = long_peices + short_peices
        sum_profit = long_profits + short_profits
        long_peices = str(long_peices)
        long_markPx = str(round(long_markPx, 3))
        long_prices = str(round(long_prices, 3))
        long_profits = str(round(long_profits, 3))
        long_liqPx = str(round(long_liqPx, 3))
        long_imr = str(round(long_imr, 3))

        short_peices = str(short_peices)
        short_markPx = str(round(short_markPx, 3))
        short_prices = str(round(short_prices, 3))
        short_profits = str(round(short_profits, 3))
        short_liqPx = str(round(short_liqPx, 3))
        short_imr = str(round(short_imr, 3))

        sum_peice = str(round(sum_peice, 3))
        sum_profit = str(round(sum_profit, 3))
        long_list = [symbol, long_peices, long_markPx, long_prices,  long_liqPx,long_profits, long_imr, ask]
        short_list = [symbol, short_peices, short_markPx, short_prices, short_liqPx, short_profits, short_imr, bid]
        sum_list = [sum_peice, sum_profit]
        return long_list, short_list, sum_list
    except:
        pass
def open_buy_peice(data: dict,peice):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)
        cn.open_buy(peice)
    except:
        pass

def open_sell_peice(data: dict,peice):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)
        cn.open_sell(peice)
    except:
        pass


def close_long_peice(data: dict, peice: int):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)
        cn.close_long(peice)
    except:
        pass


def close_short_peice(data: dict, peice: int):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)
        cn.close_short(peice)
    except:
        pass

def close_long_peices(data: dict):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)

        result = cn.get_position_information()
        long_peices = cn.get_long_position_peices(result)
        cn.close_long(long_peices)
    except:
        pass

def close_short_peices(data: dict):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)

        result = cn.get_position_information()
        short_peices = cn.get_short_position_peices(result)
        cn.close_short(short_peices)
    except:
        pass




def close_all_peices(data: dict):
    try:
        api = data.get("api")
        api_key = data.get("api_key")
        password = data.get("password")
        flag = data.get("flag")
        flag = bool_to_str(flag)
        symbol = data.get("symbol")
        cn = coin_trade(api, api_key, password, flag, symbol)

        result = cn.get_position_information()
        long_peices = cn.get_long_position_peices(result)
        short_peices = cn.get_short_position_peices(result)
        cn.close_long(long_peices)
        cn.close_short(short_peices)
    except:
        pass





if __name__ == '__main__':

    api = "6e73c2c1-226b-446f-8c14-dd39c8fc25b7"
    api_key = "CA2E8A0AC53961D8B04D5A2EE71E9883"
    password = "Ccmy-0622"
    flag = True
    symbol = "ETH-USDT-SWAP"


    data = {"api": api,
            "api_key": api_key,
            "password": password,
            "flag": flag,
            "symbol": symbol}
    long_list ,short_list ,sum_list= information(data)
    print(long_list)
    print(short_list)
    print(sum_list)
