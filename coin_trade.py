import okx.Account_api as Account
import okx.Funding_api as Funding
import okx.Market_api as Market
import okx.Public_api as Public
import okx.Trade_api as Trade
import okx.status_api as Status
import okx.subAccount_api as SubAccount
import okx.TradingData_api as TradingData
import okx.Broker_api as Broker
import okx.Convert_api as Convert
import okx.FDBroker_api as FDBroker
import okx.Rfq_api as Rfq
import okx.TradingBot_api as TradingBot

import json
import sys
import time
import numpy as np


def bool_to_str(flag: bool):
    if flag == True:
        return "1"
    else:
        return "0"
class static():  # 私有变量，无法在外部访问，Foo.__var会出错
    def __init__(self, init_v0=0, init_v1=0, init_v2=0, init_v3=0,init_v4=0,
                       init_v5=0, init_v6=0, init_v7=0,init_v8=0,init_v9=0):
        
        self.__var0 = init_v0
        self.__var1 = init_v1
        self.__var2 = init_v2
        self.__var3 = init_v3
        self.__var4 = init_v4
        self.__var5 = init_v5
        self.__var6 = init_v6
        self.__var7 = init_v7
        self.__var8 = init_v8
        self.__var9 = init_v9

    @classmethod
    def get_var0(cls):
        return cls.__var0

    @classmethod
    def set_var0(cls, num):
        cls.__var0 = num

    @classmethod
    def get_var1(cls):
        return cls.__var1

    @classmethod
    def set_var1(cls, num):
        cls.__var1 = num

    @classmethod
    def get_var2(cls):
        return cls.__var2

    @classmethod
    def set_var2(cls, num):
        cls.__var2 = num

    @classmethod
    def get_var3(cls):
        return cls.__var3

    @classmethod
    def set_var3(cls, num):
        cls.__var3 = num

    @classmethod
    def get_var4(cls):
        return cls.__var4

    @classmethod
    def set_var4(cls, num):
        cls.__var4 = num

    @classmethod
    def get_var5(cls):
        return cls.__var5

    @classmethod
    def set_var5(cls, num):
        cls.__var5 = num

    @classmethod
    def get_var6(cls):
        return cls.__var6

    @classmethod
    def set_var6(cls, num):
        cls.__var6 = num

    @classmethod
    def get_var7(cls):
        return cls.__var7

    @classmethod
    def set_var7(cls, num):
        cls.__var7 = num

    @classmethod
    def get_var8(cls):
        return cls.__var8

    @classmethod
    def set_var8(cls, num):
        cls.__var8 = num

    @classmethod
    def get_var9(cls):
        return cls.__var9

    @classmethod
    def set_var9(cls, num):
        cls.__var9 = num

class coin_trade():
    def __init__(self, api_key, secret_key, passphrase, flag, symbol):
        static()
        self.broker_code = 'e48bb19f7155BCDE'
        self.clOrdId  = '0622'
        self.tag = '0622'
        
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__passphrase = passphrase
        self.__flag = flag  # 1 模拟盘  0 实盘
        self.symbol = symbol
        
        self.__var0 ,self.__var1,self.__var2 ,self.__var3,self.__var4  = 0,0,0,0,0
        self.__var5,self.__var6, self.__var7, self.__var8, self.__var9 = 0,0,0,0,0


        self.accountAPI = Account.AccountAPI(self.__api_key, self.__secret_key, self.__passphrase, False,  self.__flag)
        self.fundingAPI = Funding.FundingAPI(self.__api_key, self.__secret_key, self.__passphrase, False,  self.__flag)
        self.convertAPI = Convert.ConvertAPI(self.__api_key, self.__secret_key, self.__passphrase, False, self.__flag)
        self.marketAPI = Market.MarketAPI(self.__api_key, self.__secret_key,  self.__passphrase, True, self.__flag)
        self.publicAPI = Public.PublicAPI(self.__api_key, self.__secret_key,  self.__passphrase, False, self.__flag)
        self.tradingDataAPI = TradingData.TradingDataAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        self.tradeAPI = Trade.TradeAPI(self.__api_key,self.__secret_key,self.__passphrase, False,self.__flag)
        # 子账户API subAccount
        self.subAccountAPI = SubAccount.SubAccountAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        self.BrokerAPI = Broker.BrokerAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        self.FDBrokerAPI = FDBroker.FDBrokerAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        # 大宗交易(Rfq)API
        self.RfqAPI = Rfq.RfqAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        # 网格交易
        self.TradingBot = TradingBot.TradingBotAPI(self.__api_key,self.__secret_key,self.__passphrase,False,self.__flag)
        self.Status = Status.StatusAPI(self.__api_key,self.__secret_key,self.__passphrase, False,self.__flag)


    def get_api_key_flag(self):
        return (self.__api_key,self.__secret_key,self.__passphrase,self.__flag)
    def set_api_key_flag(self, api_key, secret_key, passphrase, flag):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__passphrase = passphrase
        self.__flag = flag  # 1 模拟盘  0 实盘

    def get_symbol(self):
        return self.symbol
    def set_symbol(self,symbol:str):
        self.__symbol = symbol

    def get_vr0(self):
        return self.__vr0
    def set_vr0(self, num):
        self.__vr0 = num
    def get_vr1(self):
        return self.__vr1
    def set_vr1(self, num):
        self.__vr1 = num

    def get_vr2(self):
        return self.__vr2
    def set_vr2(self, num):
        self.__vr2 = num
    def get_vr3(self):
        return self.__vr3
    def set_vr3(self, num):
        self.__vr3 = num
        
    def get_vr4(self):
        return self.__vr4
    def set_vr4(self, num):
        self.__vr4 = num
    def get_vr5(self):
        return self.__vr5
    def set_vr5(self, num):
        self.__vr5 = num
        
    def get_vr6(self):
        return self.__vr6
    def set_vr6(self, num):
        self.__vr6 = num
    def get_vr7(self):
        return self.__vr7
    def set_vr7(self, num):
        self.__vr7 = num
        
    def get_vr8(self):
        return self.__vr8
    def set_vr8(self, num):
        self.__vr8 = num
    def get_vr9(self):
        return self.__vr9
    def set_vr9(self, num):
        self.__vr9 = num


    # 获取杠杆
    def get_levers(self, cross_or_isolated='cross'):
        result = self.accountAPI.get_leverage(self.symbol, cross_or_isolated)
        return float(result['data'][0].get('lever'))
    # 设置杠杆
    def set_levers(self, levers=10, mgnMode='cross'):
        lever = self.get_levers(mgnMode)
        if lever and lever < levers:
            self.accountAPI.set_leverage(instId=self.symbol, lever=str(lever), mgnMode=mgnMode)
    # 获取账户配置
    def get_account_config(self):
        result = self.accountAPI.get_account_config()
        if self.check_result(result):
            return result['data']
    # 设置双向持仓
    def set_two_way_position(self):
        result = self.get_account_config()
        if result[0].get('posMode') != 'long_short_mode':
            result = self.accountAPI.get_position_mode('long_short_mode')
            print(result)
    # 获取订单薄
    def get_order_book(self, limit):
        if int(limit) > 400:
            limit = '400'
        limit = str(limit)
        result = self.marketAPI.get_orderbook(self.symbol, limit)
        if self.check_result(result):
            return result['data']

    def ask_bid(self, result):
        ask, bid = 0.0, 0.0
        if result:
            ask = result[0]['asks'][0][0]
            bid = result[0]['bids'][0][0]
        return float(ask), float(bid)

    def ask_bid(self):
        ask, bid = 0.0, 0.0
        result = self.get_order_book(1)
        if result:
            ask = result[0]['asks'][0][0]
            bid = result[0]['bids'][0][0]
        return float(ask), float(bid)

    def asks_or_bids(self, result, asks_or_bids='asks'):
        list1, list2, list3, list4 = [], [], [], []
        if result:
            listask = result[0][asks_or_bids]
            for i in listask:
                list1.append(float(i[0]))
                list2.append(float(i[1]))
                list3.append(float(i[3]))
                list4.append(float(i[1]) * float(i[3]))
        return list1, list2, list3, list4

    # 获取单个产品行情信息
    def get_ticker(self):
        result = self.marketAPI.get_ticker(self.symbol)
        if self.check_result(result):
            return result['data']

    # 获取账户信息
    def get_account_information(self):
        result = self.accountAPI.get_account(self.symbol)
        if self.check_result(result):
            return result['data']

    # 获取结余
    def get_balance(self, result, key='cashBal', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key))
        return 0.0

    # 获取可用保证金
    def get_margin(self, result, key='availEq', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key))
        return 0.0

    # 保证金率
    def get_margin_rate(self, result, key='mgnRatio', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key)) * 100
        return 0.0

    # 获取未实现盈亏
    def get_unrealized_profits(self, result, key='upl', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key))
        return 0.0

    # 获取实际杠杆
    def get_real_lever(self, result, key='notionalLever', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key))
        return 0.0

    # 总权益
    def get_money(self, result, key='eq', ccy='USDT'):
        for i in result[0]['details']:
            if i.get('ccy') == ccy:
                return float(i.get(key))
        return 0.0
    
    # 市价做多
    def open_buy(self, sz, cross_or_isolated='cross'):
        order_number = 0
        if sz > 0:
            sz = str(sz)
            result = self.tradeAPI.place_order(instId=self.symbol, clOrdId = self.clOrdId, tdMode = cross_or_isolated,
                                          side='buy',posSide='long', ordType='market', sz=sz, tag=self.broker_code)
            print(result)
            order_number = result['data'][0]['ordId']
            if order_number != "":
                print("市价做多: ", order_number)
            elif sz and order_number == "":
                print("市价做多错误: ", order_number)
        return order_number

    # 市价做空
    def open_sell(self, sz, cross_or_isolated='cross'):
        order_number = 0
        if sz > 0:
            # if sz < 1:
            # sz = 1
            sz = str(sz)
            result = self.tradeAPI.place_order(instId=self.symbol, clOrdId=self.clOrdId, tdMode=cross_or_isolated,
                                          side='sell',posSide='short', ordType='market', sz=sz, tag=self.broker_code)
            print(result)
            order_number = result['data'][0]['ordId']
            if order_number != "":
                print("市价做空: ", order_number)
            elif sz and order_number == "":
                print("市价做空错误: ", order_number)
        return order_number
    
    # 市价平多
    def close_long(self, sz, cross_or_isolated='cross'):
        order_number = 0
        if sz > 0:
            sz = str(sz)
            result = self.tradeAPI.place_order(instId=self.symbol, clOrdId=self.clOrdId, tdMode=cross_or_isolated,
                                          side='sell',posSide='long', ordType='market', sz=sz, tag=self.broker_code)
            order_number = result['data'][0]['ordId']
            if order_number != "":
                print("市价平多: ", order_number)
            elif sz and order_number == "":
                print("市价平多错误: ", order_number)
        return order_number


    # 市价平空
    def close_short(self, sz, cross_or_isolated='cross'):
        order_number = 0
        if sz > 0:
            sz = str(sz)
            result = self.tradeAPI.place_order(instId=self.symbol, clOrdId=self.clOrdId, tdMode=cross_or_isolated,
                                          side='buy',posSide='short', ordType='market', sz=sz, tag=self.broker_code)
            order_number = result['data'][0]['ordId']
            if order_number != "":
                print("市价平空: ", order_number)
            elif sz and order_number == "":
                print("市价平空错误: ", order_number)
        return order_number
    
    # 获取持仓信息
    def get_position_information(self, instType='SWAP'):
        result = self.accountAPI.get_positions(instType=instType, instId=self.symbol)
        if self.check_result(result):
            return result['data']

    # 获取持仓信息
    def get_positon_information(self, result, long_or_short, key='upl', cross_or_isolated='cross'):
        value = 0.0
        for i in result:
            if i['mgnMode'] == cross_or_isolated and i['posSide'] == long_or_short:
                value = i[key]
            if i['mgnMode'] == cross_or_isolated and i['posSide'] == long_or_short:
                value = i[key]
            if i['mgnMode'] == cross_or_isolated and i['posSide'] == long_or_short:
                value = i[key]
            if i['mgnMode'] == cross_or_isolated and i['posSide'] == long_or_short:
                value = i[key]
            if value == "":
                value = 0.0
        return float(value)
    # 多持仓均价
    def get_long_position_prices(self, result, cross_or_isolated='cross'):
        try:
            value = self.get_positon_information(result, 'long', key='avgPx', cross_or_isolated=cross_or_isolated)
        except:
            value = 0.0
        return float(value)

    # 空持仓均价
    def get_short_position_prices(self, result, cross_or_isolated='cross'):
        try:
            value = self.get_positon_information(result, 'short', key='avgPx', cross_or_isolated=cross_or_isolated)
        except:
            value = 0.0
        return float(value)
    
    # 多持仓张数
    def get_long_position_peices(self, result, cross_or_isolated='cross'):
        try:
            value = self.get_positon_information(result, 'long', key='pos', cross_or_isolated=cross_or_isolated)
        except:
            value = -1
        return int(value)

    # 空持仓张数
    def get_short_position_peices(self, result, cross_or_isolated='cross'):
        try:
            value = self.get_positon_information(result, 'short', key='pos', cross_or_isolated=cross_or_isolated)
        except:
            value = -1
        return int(value)
    
    #价格百分比
    def price_percent(self, in_price, ref_price, percent, omax_tmin=1):
        if in_price and ref_price:
            if omax_tmin == 1 and percent and ref_price > in_price * (1 + percent):
                return True
            if omax_tmin == 2 and percent and ref_price < in_price * (1 - percent):
                return True
        return False

    def count_choose(self, peice, cnt, repeat_count=0, manner_choose=0, double=0,set_repeat_count=0):  # 张数 计数 重复计数 方式选择 翻倍 设置重复计数
        count = cnt
        if double == 0 and peice and repeat_count >= set_repeat_count:
            repeat_count = 0
            if manner_choose == 0:
                count = count
            if manner_choose and manner_choose != 3267 and manner_choose != 3268:
                count = count + manner_choose
        if double and peice and repeat_count >= set_repeat_count:
            count = count * double
        repeat_count += 1
        if peice == 0:
            count = cnt
            repeat_count = 0
        return int(count), int(repeat_count)

    #获取未成交订单信息
    def get_order_information(self, result, key='ordId'):
        buyid, sellid = [], []
        if len(result):
            for i in result:
                if i['instId'] == self.symbol and i['side'] == 'buy':
                    buyid.append(i[key])
                if i['instId'] == self.symbol and i['side'] == 'sell':
                    sellid.append(i[key])
        return buyid, sellid

    #移动止损止盈
    def move_sl_tp(self, buy_or_sell, long_or_short, sz, callbackRatio='0.05', activePx='',cross_or_isolated='cross'):  # 市价执行
        result = self.tradeAPI.place_algo_order(instId=self.symbol, tdMode=cross_or_isolated, side=buy_or_sell,
                                           posSide=long_or_short,ordType='move_order_stop', sz=sz,
                                           tag=self.broker_code, clOrdId=self.clOrdId, callbackRatio=callbackRatio,
                                           activePx=activePx)
        if result['data']:
            print(buy_or_sell + long_or_short + '回调幅度移动止损止盈下单成功', result['data'][0]['algoId'])
            return result['data'][0]['algoId']
        else:
            print(buy_or_sell + long_or_short + '回调幅度移动止损止盈下单错误')
    # 计划委托
    def plan_delegation(self, buy_or_sell, long_or_short, sz, TriggerPx, orderPx=-1, triggerPxType='last',
                 cross_or_isolated='cross'):  # orderPx=-1 市价执行#永续不支持
        result = self.tradeAPI.place_algo_order(instId=self.symbol, tdMode=cross_or_isolated, side=buy_or_sell,
                                           posSide=long_or_short,ordType='trigger', sz=sz,
                                           tag=self.broker_code, clOrdId=self.clOrdId, TriggerPx=TriggerPx,
                                           orderPx=orderPx,triggerPxType=triggerPxType)
        if result['data']:
            print(buy_or_sell + long_or_short + '计划委托下单成功', result['data'][0]['algoId'])
            return result['data'][0]['algoId']
        else:
            print(buy_or_sell + long_or_short + '计划委托下单错误')

    # 获取持仓均价
    def get_position_price_mean(self, long_price_mean, long_peice, short_price_mean, short_peice):
        price_mean, check = 0, 0
        if long_peice != short_peice:
            price_mean = (long_price_mean * long_peice + short_price_mean * short_peice) / (long_peice + short_peice)
            if long_peice > short_peice:
                check = 1
            else:
                check = 2
        return  check,price_mean


    # 获取最大允许下单量
    def get_max_peice(self, tdMode='cross', leverage='3', ccy="USDT"):
        result = self.accountAPI.get_maximum_trade_size(self.symbol, tdMode=tdMode, leverage=leverage, ccy=ccy)
        if result['data']:
            return result['data'][0].get('maxBuy'), result['data'][0].get('maxSell')
        else:
            0, 0
    # 获取最大可用额度
    def get_max_margin(self, tdMode='cross', ccy='USDT'):
        result = self.accountAPI.get_max_avail_size(self.symbol, tdMode, ccy)
        if result['data']:
            return result['data'][0].get('availBuy'), result['data'][0].get('availSell')
        else:
            return 0.0, 0.0
    # 获取手续费率
    def get_account_commission(self, instType='SWAP', type='takerU'):
        result = self.accountAPI.get_fee_rates(instType, '', category='1')
        if result['data']:
            return result['data'][0].get(type)
        else:
            return 0.0
    # 获取面值
    def get_par(self, mz='ctVal'):
        temp = self.symbol.split('-')
        symbolqz, instType = temp[0] + '-' + temp[1], temp[2]
        result = self.publicAPI.get_instruments(instType, symbolqz)
        if result['data']:
            return result['data'][0].get(mz)
        else:
            return 0.0

    # 合约手续费计算
    def get_commission(self, face_value, in_price, peice, rates):
        free = float(face_value) * float(in_price) * int(peice) * float(rates)
        return float(2 * free)

    # 合约手续费
    def get_commission(self, price_mean, peice, instType='SWAP'):
        fl = self.get_account_commission(instType=instType, type='takerU')
        re = self.get_par(mz='ctVal')
        fr = self.get_commission(re, price_mean, peice, fl)
        return float(fr)

    # 单位时间
    def tim_chk_1(self, ref_time, time_gap):
        if ref_time:
            if ref_time > static.get_var1() + time_gap:
                return True
                static.set_var1(ref_time)
        return False

    def tim_chk_2(self, ref_time, time_gap):
        if ref_time:
            if ref_time > static.get_var2() + time_gap:
                return True
                static.set_var2(ref_time)
        return False

    def tim_chk_3(self, ref_time, time_gap):
        if ref_time:
            if ref_time > static.get_var3() + time_gap:
                return True
                static.set_var3(ref_time)
        return False

    def tim_chk_4(self, ref_time, time_gap):
        if ref_time:
            if ref_time > static.get_var4() + time_gap:
                return True
                static.set_var4(ref_time)
        return False

    # 单位时间上涨百分比
    def tim_up_percent_var56(self, ref_time, ref_price, time_gap,set_percent):  # 需要init_v赋值 t.set_var56(ref_time)
        check = False
        if set_percent and ref_time and ref_price:
            if ref_time < static.get_var5() + time_gap and static.get_var6() != 0:
                if set_percent and (ref_price - static.get_var6()) / static.get_var6() > set_percent:
                    check = True
                    static.set_var5(ref_time)
                    static.set_var6(ref_price)
            else:
                static.set_var5(ref_time)
                static.set_var6(ref_price)
        return check
    # 单位时间下跌百分比
    def tim_down_percent_var78(self, ref_time, ref_price, time_gap, set_percent):  # 需要init_v赋值 t.set_var78(ref_time)
        check = False
        if set_percent and ref_time and ref_price:
            if ref_time < static.get_var7() + time_gap and static.get_var8() != 0:
                if set_percent and (static.get_var8() - ref_price) / static.get_var8() > set_percent:
                    check = True
                    static.set_var7(ref_time)
                    static.set_var8(ref_price)
            else:
                static.set_var7(ref_time)
                static.set_var8(ref_price)
        return check

    # 区间 上下区间
    def interval_chk(self, in_value, up_limit, down_limit):
        check = False
        t1 = in_value > 0 and in_value < up_limit and in_value > down_limit
        t2 = in_value > 0 and in_value < up_limit and down_limit == 0
        t3 = in_value > 0 and up_limit == 0 and in_value > down_limit
        t4 = in_value > 0 and up_limit == 0 and down_limit == 0
        tz = t1 + t2 + t3 + t4
        if tz:
            check = True
        return check

    def LV(self, compute_array, begin_index, end_index, whether_reverse=False):
        if whether_reverse:
            compute_array.reverse()
        minn = sys.maxsize
        for i in compute_array[begin_index:end_index]:
            if i < minn:
                minn = i
        return minn

    def HV(self, compute_array, begin_index, end_index, whether_reverse=False):
        if whether_reverse:
            compute_array.reverse()
        maxx = -999999999
        for i in compute_array[begin_index:end_index]:
            if i > maxx:
                maxx = i
        return maxx
    # 获取k线数据
    def get_k_information(self, bar='1m', lit=10):
        if lit > 300:
            lit = 300
        lit = str(lit)
        result = self.marketAPI.get_candlesticks(self.symbol, bar=bar, limit=lit)
        if self.check_result(result):
            return result['data']

    def get_k_information(self, result):
        list0, list1, list2, list3, list4, list5, list6 = [], [], [], [], [], [], []
        for i in result:
            list0.append(float(i[0]))
            list1.append(float(i[1]))
            list2.append(float(i[2]))
            list3.append(float(i[3]))
            list4.append(float(i[4]))
            list5.append(float(i[5]))
            list6.append(float(i[6]))
        return list0, list1, list2, list3, list4, list5, list6
    # 穿越某值
    def crossing_value(self, in_value1, in_value0, value1, value0, omax_tmin):
        check = False
        if in_value1 and in_value0 and value1 and value0:
            if omax_tmin == 1 and in_value1 < value1 and in_value0 > value0:
                check = True
            if omax_tmin == 2 and in_value1 > value1 and in_value0 < value0:
                check = True
        return check

    def bufSort(self, arr, oliter_tfalls):
        n = len(arr)
        if n and oliter_tfalls == 1:
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if n and oliter_tfalls == 2:
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if n:
            return arr[0]
        else:
            return []

    def rolling_window(self, a, window):
        shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
        strides = a.strides + (a.strides[-1],)
        return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    #求差
    def get_list_dif(self, list1, in_value):
        cz = []
        for i in range(0, len(list1)):
            cz = list1[i] - in_value
        return cz
    def get_list_dif(self, list1, list2):
        cz = []
        cd = min(len(list1), len(list2))
        for i in range(0, cd):
            cz = list1[i] - list[i]
        return cz
    # 求差绝对值
    def get_list_dif_abs(self, list1, in_value):
        cz = []
        for i in range(0, len(list1)):
            cz = abs(list1[i] - in_value)
        return cz
    def get_list_dif_abs(self, list1, list2):
        cz = []
        cd = min(len(list1), len(list2))
        for i in range(0, cd):
            cz = abs(list1[i] - list[i])
        return cz
    # 求均值
    def get_list_mean(self, list, compute_period):
        mean = []
        if len(list) < compute_period:
            return []
        for i in range(0, len(list) - compute_period):
            if i + compute_period > len(list):
                break
            mean.append(np.mean(list[i:i + compute_period]))
        return mean
    # 求布林值
    def get_boll_value(self, list, compute_period, deviation):
        zg, up, down = [], [], []
        if len(list) < compute_period:
            return [], [], []
        for i in range(0, len(list) - compute_period):
            if i + compute_period > len(list):
                break
            zg.append(np.mean(list[i:i + compute_period]))
            up.append(np.mean(list[i:i + compute_period]) + deviation * np.std(list[i:i + compute_period]))
            down.append(np.mean(list[i:i + compute_period]) - deviation * np.std(list[i:i + compute_period]))
        return zg, up, down
    # 最高价回调
    def high_callback_percent_var9(self, t, long_peice, bid, callback_percent):  # var9
        check = False
        if callback_percent:
            if long_peice == 0:
                static.set_var9(bid)
            if long_peice and bid > static.get_var9():
                static.set_var9(bid)
            if bid < static.get_var9() * (1 - callback_percent):
                check = True
        return check
    # 最低价反弹
    def low_callback_percent_var0(self, t, short_peice, ask, callback_percent):  # var0
        check = False
        if callback_percent:
            if short_peice == 0:
                static.set_var0(ask)
            if short_peice and ask < static.get_var0():
                static.set_var0(ask)
            if ask > static.get_var0() * (1 + callback_percent):
                check = True
        return check
    # 追踪平多 var9
    def percent_close_long_var9(self, t, long_peice, long_price_mean, bid, trace_initiate_percent, trace_callback_percent):
        close_buy = self.price_percent(long_price_mean, bid, trace_initiate_percent, 1) * self.high_callback_percent_var9(t, long_peice, bid,
                                                                                              trace_callback_percent)
        if close_buy:
            self.close_long(long_peice)
    # 追踪平空 var0
    def percent_close_short_var0(self, t, short_peice, short_price_mean, ask, trace_initiate_percent, trace_callback_percent):
        close_sell = self.price_percent(short_price_mean, ask, trace_initiate_percent, 2) * self.low_callback_percent_var0(t, short_peice, ask,
                                                                                                trace_callback_percent)
        if close_sell:
            self.close_short(short_peice)
    # 下多挂单
    def plan_long_order(self, px, sz, ordType='limit', cross_or_isolated='cross'):
        result = self.tradeAPI.place_order(instId=self.symbol, tdMode=cross_or_isolated, side='buy',
                                      posSide='long', ordType=ordType, sz=sz, px=px, tgtCcy='', banAmend='')
        if result['data']:
            print('下多挂单成功 ', px, sz, result['data'].get('ordId'))
            return result['data'].get('ordId')
        else:
            print('下多挂单失败 ', px, sz)
        if self.check_result(result):
            return result['data']
    # 下空挂单
    def plan_short_order(self, px, sz, ordType='limit', cross_or_isolated='cross'):
        result = self.tradeAPI.place_order(instId=self.symbol, tdMode=cross_or_isolated, side='sell',
                                      posSide='short', ordType=ordType, sz=sz, px=px, tgtCcy='', banAmend='')
        if result['data']:
            print('下空挂单成功 ', px, sz, result['data'].get('ordId'))
            return result['data'].get('ordId')
        else:
            print('下空挂单失败 ', px, sz)
        if self.check_result(result):
            return result['data']
    # 批量下单
    def plan_multiple_order(self, list):
        result = self.tradeAPI.place_multiple_orders(list)
        if self.check_result(result):
            return result['data']
    # 撤单
    def cancel_order(self, id):
        id = str(id)
        result = self.tradeAPI.cancel_order(self.symbol, id)
        if result['data']:
            print('撤单成功 ', self.symbol, id)
            return result['data'].get('ordId')
        else:
            print('撤单失败 ', self.symbol, id)
        if self.check_result(result):
            return result['data']
    # 批量撤单
    def cancel_multiple_orders(self, list):
        result = self.tradeAPI.cancel_multiple_orders(list)
        if self.check_result(result):
            return result['data']
    # 修改订单价格张数
    def modify_order_price_peice(self, ordId, newPx, newSz, cxlOnFail='false'):
        result = self.tradeAPI.amend_order(self.symbol, cxlOnFail=cxlOnFail, ordId=ordId, clOrdId=self.clOrdId,
                                      newSz=newSz, newPx=newPx)
        if self.check_result(result):
            return result['data']

    # 修改订单价格
    def modify_order_price(self, ordId, newPx, cxlOnFail='false'):
        result = self.tradeAPI.amend_order(self.symbol, cxlOnFail=cxlOnFail, ordId=ordId, clOrdId=self.clOrdId,
                                      newPx=newPx)
        if self.check_result(result):
            return result['data']

    # 修改订单张数
    def modify_order_peice(self, ordId, newSz, cxlOnFail='false'):
        result = self.tradeAPI.amend_order(self.symbol, cxlOnFail=cxlOnFail, ordId=ordId, clOrdId=self.clOrdId,
                                      newSz=newSz)
        if self.check_result(result):
            return result['data']

    # 批量修改订单
    def modify_multiple_orders(self, list):
        result = self.tradeAPI.amend_multiple_orders(list)
        if self.check_result(result):
            return result['data']
    # close_long
    def close_long_positions(self, autoCxl='false', cross_or_isolated='cross'):
        result = self.tradeAPI.close_positions(instId=self.symbol, posSide='long', mgnMode=cross_or_isolated,
                                          autoCxl=autoCxl,
                                          clOrdId=self.clOrdId, tag=self.broker_code)
        if self.check_result(result):
            return result['data']

    # close_short
    def close_short_positions(self, autoCxl='false', cross_or_isolated='cross'):
        result = self.tradeAPI.close_positions(instId=self.symbol, posSide='short', mgnMode=cross_or_isolated,
                                          autoCxl=autoCxl,
                                          clOrdId=self.clOrdId, tag=self.broker_code)
        if self.check_result(result):
            return result['data']

    # 获取订单信息
    def get_order_information(self, ordld):
        result = self.tradeAPI.get_orders(self.symbol, ordld, clOrdId=self.clOrdId)
        if self.check_result(result):
            return result['data']

    def get_order_information_list(self, limit='100', ordType='limit', state='live'):
        result = self.tradeAPI.get_order_list(instId=self.symbol, instType='SWAP', ordType=ordType, state=state, limit=limit)
        if self.check_result(result):
            return result['data']

    def 返回值与索引(self, list_volume, list_price, set_value, omax_tmin=1):
        value1, value2, value3 = 0.0, 0.0, ''
        lens = min(len(list_volume), len(list_price))
        for i in range(0, lens):
            if omax_tmin == 1 and list_volume[i] > set_value:
                value1 = list_volume[i]
                value2 = list_price[i]
                value3 = i
                break
            if omax_tmin == 2 and list_volume[i] < set_value:
                value1 = list_volume[i]
                value2 = list_price[i]
                value3 = i
                break
        return value1, value2, value3

    def 获取历史持仓信息(self, before='', after='', limit='', cross_or_isolated='cross'):
        result = self.accountAPI.get_positions_history(instType='SWAP', instId=self.symbol, mgnMode=cross_or_isolated,
                                                  type='2',
                                                  after=after, before=before, limit=limit)
        if self.check_result(result):
            return result['data']

    def 解析列表字典信息float(self, result, key='pnl'):
        pnl = []
        for i in result:
            pnl.append(float(i.get(key)))
        return pnl

    def 解析列表字典信息string(self, result, key='pnl'):
        pnl = []
        for i in result:
            pnl.append(i.get(key))
        return pnl

    def 毫秒开盘时间(self, period='1D', count=0, lit=3):
        lit = lit + count
        tm = self.get_k_information(bar=period, lit=lit)
        open_time0 = str(int(tm[0][count]))
        open_time1 = str(int(tm[0][count + 1]))
        end_time = str(int(round(time.time() * 1000)))
        return open_time0, open_time1, end_time

    def iMAOnArray(self, Array, total, iMAPeriod, ma_shift, ma_method, shift, m=1):
        buf = []
        if total > 0 and total <= iMAPeriod:
            return 0
        if total == 0:
            total = len(Array)

        if len(buf) < 0 or iMAPeriod == 0:
            return 0
        buf += [0 for x in range(total)]
        if ma_method == 'MODE_SMA':
            sum = 0.0
            pos = total - 1
            for i in range(1, iMAPeriod):
                sum += Array[pos]
                pos = pos - 1
            while pos >= 0:
                sum += Array[pos]
                buf[pos] = sum / iMAPeriod
                sum -= Array[pos + iMAPeriod - 1]
                pos = pos - 1
            return buf[shift + ma_shift]
        elif ma_method == 'MODE_EMA':
            pr = 2.0 / (iMAPeriod + 1)
            pos = total - 2
            while pos >= 0:
                if pos == total - 2:
                    buf[pos + 1] = Array[pos + 1]
                buf[pos] = Array[pos] * pr + buf[pos + 1] * (1 - pr)
                pos = pos - 1
            return buf[shift + ma_shift]

        elif ma_method == 'MODE_SMMA':
            if m >= iMAPeriod:
                m = iMAPeriod - 1
            sum = 0.0
            pos = total - iMAPeriod
            while pos >= 0:
                if pos == total - iMAPeriod:
                    k = pos
                    for i in range(0, iMAPeriod):
                        sum += Array[k]
                        buf[k] = 0
                        k = k + 1
                else:
                    sum = buf[pos + 1] * (iMAPeriod - m) + m * Array[pos]
                buf[pos] = sum / iMAPeriod
                pos = pos - 1
            return buf[shift + ma_shift]
        elif ma_method == 'MODE_LWMA':
            sum, lsum = 0.0, 0.0
            i, weight = 0, 0
            pos = total - 1
            for i in range(1, iMAPeriod + 1):
                price = Array[pos]
                sum += price * i
                lsum += price
                weight += i
                pos = pos - 1
            pos = pos + 1
            i = pos + iMAPeriod
            while pos >= 0:
                buf[pos] = sum / weight
                if pos == 0:
                    break
                pos = pos - 1
                i = i - 1
                price = Array[pos]
                sum = sum - lsum + price * iMAPeriod
                lsum -= Array[i]
                lsum += price
            return buf[shift + ma_shift]
        else:
            return 0
        return 0

    def 获取系统时间(self):
        result = self.publicAPI.get_system_time()
        if self.check_result(result):
            return result['data']

    def 张币转换(self, sz='1', px=''):
        result = self.publicAPI.convert_contract_coin(type='2', instId=self.symbol, sz=sz, px=px)
        peice_coin = result['data'][0].get('sz')
        if peice_coin != '':
            peice_coin = float(peice_coin)
        else:
            peice_coin = 0.0
        return peice_coin

    def 币张转换(self, sz='1', px=''):
        result = self.publicAPI.convert_contract_coin(type='1', instId=self.symbol, sz=sz, px=px)
        coin_peice = result['data'][0].get('sz')
        if coin_peice != '':
            coin_peice = int(coin_peice)
        else:
            coin_peice = 0
        return coin_peice

    def 获取限价(self):
        result = self.publicAPI.get_price_limit(self.symbol)
        if result['data']:
            return result['data'][0].get('buyLmt'), result['data'][0].get('sellLmt')
        else:
            return 0.0, 0.0

    def 获取持仓总量(self):
        result = self.publicAPI.get_open_interest(instType='SWAP', instId=self.symbol)
        if result['data']:
            return ['data'][0].get('oi'), ['data'][0].get('oiCcy')
        else:
            return 0.0, 0.0

    def 获取永续合约当前资金费率(self):
        result = self.publicAPI.get_funding_rate(self.symbol)
        if result['data']:
            return result['data'][0].get('fundingRate'), result['data'][0].get('fundingTime'), result['data'][0].get(
                'nextFundingRate'), result['data'][0].get('nextFundingTime')
        else:
            return 0.0, 0, 0.0, 0

    def 获取永续合约历史资金费率(self, before='', after='', limit='100'):
        result = self.publicAPI.funding_rate_history(instId=self.symbol, before=before, after=after, limit=limit)
        if self.check_result(result):
            return result['data']

    def 获取交易产品基础信息(self, instType='SWAP'):
        result = self.publicAPI.get_instruments(instType=instType, instId=self.symbol)
        if self.check_result(result):
            return result['data']

    def 获取币种列表(self, result, key='instId'):
        lst = []
        for i in result:
            lst.append(i.get(key))
        return lst

    def 过滤币种列表(self, symbol_lists, str='-USDT'):
        lists = []
        for i in symbol_lists:
            if i.find(str) != -1:
                lists.append(i[:i.find(str)])
        return lists

    def 获取永续合约币种列表(self, result, key='instId'):
        self.symbol_list = self.获取币种列表(result, key=key)
        self.symbols = []
        for i in self.symbol_list:
            if i.find('-USDT-SWAP') != -1:
                self.symbols.append(i[:i.find('-USDT-SWAP')])
        return self.symbols

    def 拆分币种字符(self):
        temp = self.symbol.split('-')
        self.symbolqz, instType = temp[0] + '-' + temp[1], temp[2]
        return self.symbolqz, instType

    def 张币金额(self, peice_coin, price):
        return peice_coin * price

    def 张币保证金(self, peice_coin, price, lever):
        if lever >= 1:
            return peice_coin * price / lever
        else:
            return 0.0

    def 获取交易产品历史K线数据(self, bar='1D', before='', after='', lit=100):  # ts o h l c vol volCcy
        if lit > 100:
            lit = 100
        lit = str(lit)
        result = self.marketAPI.get_history_candlesticks(instId=self.symbol, after=after, before=before, bar=bar, limit=lit)
        if self.check_result(result):
            return result['data']

    def 获取交易产品K线数据(self, bar='1D', before='', after='', lit=300):  # ts o h l c vol volCcy
        if lit > 300:
            lit = 300
        lit = str(lit)
        result = self.marketAPI.get_candlesticks(instId=self.symbol, bar=bar, after=after, before=before, limit=lit)
        if self.check_result(result):
            return result['data']


    def 求list和(self, list1, list2):
        add = []
        lenght = min(len(list1), len(list2))
        for i in range(0, lenght):
            add.append(float(list1[i]) + float(list2[i]))
        return add

    def 求list差(self, list1, list2):
        dif = []
        lenght = min(len(list1), len(list2))
        for i in range(0, lenght):
            dif.append(float(list1[i]) - float(list2[i]))
        return dif

    def 求list积(self, list1, list2):
        acc = []
        lenght = min(len(list1), len(list2))
        for i in range(0, lenght):
            acc.append(float(list1[i]) * float(list2[i]))
        return acc

    def 求list除(self, list1, list2):
        dvc = []
        lenght = min(len(list1), len(list2))
        for i in range(0, lenght):
            if float(list2[i]) != 0:
                dvc.append(float(list1[i]) / float(list2[i]))
        return dvc

    def 求lists均值(self, list1, list2, list3, list4):
        mean, add = [], []
        lenght1 = min(len(list1), len(list2))
        lenght2 = min(len(list3), len(list4))
        lenght = min(lenght1, lenght2)
        for i in range(0, lenght):
            mean.append((float(list1[i]) + float(list2[i]) + float(list3[i]) + float(list4[i])) / 4)
            add.append(float(list1[i]) + float(list2[i]) + float(list3[i]) + float(list4[i]))
        return mean, add

    def 求双lists均值(self, list1, list2):
        mean, add = [], []
        lenght = min(len(list1), len(list2))
        for i in range(0, lenght):
            mean.append((float(list1[i]) + float(list2[i])) / 2)
            add.append(float(list1[i]) + float(list2[i]))
        return mean, add

    def data_to_csv(self, pd, data, index, columns, path='./data_to_csv.csv'):
        test = pd.DataFrame(data=data, index=index, columns=columns)
        test.to_csv(path, encoding='utf-8')
        return test

    def file_to_csv(self, csv, columns, lists, path='./no_fre.csv'):
        csvFile = open(path, "w+")
        try:
            writer = csv.writer(csvFile)
            writer.writerow(columns)
            writer.writerows(lists)
        finally:
            csvFile.close()
            time.sleep(0.001)

    def reader_csv(self, csv, path='./data_to_csv.csv'):
        list = []
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                list.append(line)
                print(line)
        return list

    def 毫秒时间戳(self, timeTemp):
        lMillisecond = str(timeTemp)[10:13]
        second = str(timeTemp)[0:10]
        timeArray = time.localtime(int(second))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        otherStyleTime = otherStyleTime + '.' + lMillisecond
        return otherStyleTime

    def 毫秒时间戳列表(self, timelist, count=-1):
        time_temp = []
        for i in timelist:
            time_temp.append(self.毫秒时间戳(i)[:count])
        return time_temp

    def 价格差限制(self, ask, bid, price_limit):
        if price_limit == 0:
            return True
        if ask and bid and price_limit != 0:
            return ask - bid < price_limit
        return False

    def 中间价(self, highmean, lowmean):
        mean_price = 0.0
        mean_price = (highmean + lowmean) / 2
        return mean_price

    def 百分比(self, double1, double2, percent, omax_tmin=1):
        check = False
        if double1 > 0 and double2 > 0 and percent > 0:
            if omax_tmin == 1 and double1 > double2 and double1 / double2 > percent:
                check = True
            if omax_tmin == 2 and double1 > double2 and double1 / double2 < percent:
                check = True
            if percent == 0:
                check = True
        return check

    def 资金划转to_trade(self, amt='', ccy='USDT'):
        result = self.fundingAPI.funds_transfer(ccy=ccy, amt=amt, type='0', froms="6", to="18", clientId=self.tag)
        if self.check_result(result):
            return result['data']

    def 资金划转to_funds(self, amt='', ccy='USDT'):
        result = self.fundingAPI.funds_transfer(ccy=ccy, amt=amt, type='0', froms="18", to="6", clientId=self.tag)
        if self.check_result(result):
            return result['data']

    def 获取资金划转状态(self, transId=''):
        result = self.fundingAPI.transfer_state(transId=transId, clientId=self.tag, type='0')
        if self.check_result(result):
            return result['data']

    def 斐波那契(self, lists, peice):
        if len(lists) == 0:
            return peice
        if len(lists) == 1 and lists[-1] > 0:
            return (lists[-1] + lists[-1])
        if len(lists) > 1 and lists[-1] > 0 and lists[-2] > 0:
            return (lists[-1] + lists[-2])
        return peice

    def 生成斐波那契(self, set_star_count=1, count=100):
        fibonacci = []
        i = 0
        while i < count:
            fibonacci.append(self.斐波那契(fibonacci, set_star_count))
            i += 1
        print(fibonacci)
        return fibonacci

    def 平方数列(self, lists, peice, pows=2):
        if len(lists) == 0:
            return pow(peice, pows)
        if len(lists) > 0:
            return pow((len(lists) + 1) * peice, pows)
        return peice

    def 生成平方(self, set_star_count=1, count=100):
        lists = []
        i = 0
        while i < count:
            lists.append(self.平方数列(lists, set_star_count))
            i += 1
        print(lists)
        return lists

    def 重复list(self, lists, count):
        lb = []
        if count < 1:
            count = 1
        for i in lists:
            for j in range(0, count):
                lb.append(i)
        print(lb)
        return lb

    def limit(self, in_value, limit):
        if limit == -1 or limit == 0:
            return False
        if limit > 0 and in_value < limit:
            return True
        return False

    def 生成百分比数列(self, start=0.0030, end=0.0500):
        add_percent = []
        i = start
        while end > 0 and i < end:
            add_percent.append(i)
            i += 0.0001
        return add_percent

    def 获取历史持仓订单记录(self, instType='SWAP'):
        lists = []
        result = self.tradeAPI.get_orders_history(instType=instType, instId=self.symbol)
        if result.get('code') == '0':
            for i in result['data']:
                if i.get('clOrdId') == self.clOrdId and i.get('pnl') != '0':
                    lists.append(i)
        return lists

    def check_result(self, result):
        if result.get('code') == '0':
            return True
        return False

    def return_data(self, result):
        if self.check_result(result):
            return result['data']
        else:
            return 'value错误'

    def 获取历史持仓订单记录(self, limit='10', instType='SWAP'):
        lists = []
        result = self.tradeAPI.get_orders_history(instType=instType, instId=self.symbol, limit=limit)
        if result.get('code') == '0':
            for i in result['data']:
                if i.get('clOrdId') == self.clOrdIdself and i.get('pnl') != '0' and (
                        (i.get('side') == 'sell' and i.get('posSide') == 'long') or (
                        i.get('side') == 'buy' and i.get('posSide') == 'short')):
                    lists.append(i)
        return lists

    def 获取symbols_price(self, symbol_lists, times=0.03):
        check = False
        while check == False:
            try:
                symbols_price = []
                for i in symbol_lists:
                    ask, bid = self.ask_bid(i)
                    lists = [i, "$" + str(bid)]
                    self.symbols_price.append(lists)
                    time.sleep(times)
                check = True
            except:
                check = False
                time.sleep(0.01)
        return self.symbols_price

    def 小数位数str(self, strr):
        value = strr[strr.find('.') + 1:]
        decimal_digits = len(strr[strr.find('.') + 1:])
        return decimal_digits, value

    def 小数位数float(self, val: float):
        val_str = str(val)
        digits_location = val_str.find('.')
        if digits_location:
            return len(val_str[digits_location + 1:])

    def boll_crossing(self, kperiod='4H', boll_period=20):
        list0, list1, list2, list3, list4, list5, list6 = self.get_k_information(kperiod,2 * boll_period + 1)
        middle, upper, lower = self.get_boll_value(np, list4, boll_period, 2)
        if self.crossing_value(list4[2], list4[1], upper[2], upper[1], 1):
            return 1
        if self.crossing_value(list4[2], list4[1], lower[2], lower[1], 2):
            return 2
        else:
            return 0

    # ---取数组sum_mean

    def 截取数组mean_sum(self, arr, lens, remove_digit=8, choose_sum=1):

        temp = 0.0
        if lens - 2 * remove_digit > 0:
            for i in range(lens - remove_digit):
                temp += float(arr[i + remove_digit])
            if choose_sum > 0:
                return temp
            else:
                return temp / (len - 2 * remove_digit)
        return temp

    def 截取数组(self, arr, lens, remove_digit):
        arr2 = []
        if lens - 2 * remove_digit > 0:
            for i in range(lens - remove_digit):
                arr2.append(arr[i + remove_digit])
        return arr2

    def 拆单市价做多(self, symbol1_long_piece, piece_s=10):
        pieces = symbol1_long_piece
        while pieces > 1 and pieces >= piece_s:
            self.open_buy(piece_s)
            pieces = pieces - piece_s
        if pieces >= 1:
            self.open_buy(pieces)

    def 拆单市价平多(self, symbol1_long_piece, piece_s=10):
        pieces = symbol1_long_piece
        while pieces > 1 and pieces >= piece_s:
            self.close_long(piece_s)
            pieces = pieces - piece_s
        if pieces >= 1:
            self.close_long(pieces)

    def 拆单市价做空(self, symbol2_short_piece, piece_s=10):
        pieces = symbol2_short_piece
        while pieces > 1 and pieces >= piece_s:
            self.open_sell(piece_s)
            pieces = pieces - piece_s
        if pieces >= 1:
            self.open_sell(pieces)

    def 拆单市价平空(self, symbol2_short_piece, piece_s=10):
        pieces = symbol2_short_piece
        while pieces > 1 and pieces >= piece_s:
            self.close_short(piece_s)
            pieces = pieces - piece_s
        if pieces >= 1:
            self.close_short(pieces)


if __name__ == '__main__':
    api_key = "6e73c2c1-226b-446f-8c14-dd39c8fc25b7"
    secret_key = "CA2E8A0AC53961D8B04D5A2EE71E9883"
    passphrase = "Ccmy-0622"
    flag = '1'  # 模拟盘
    # api_key = "29218e1e-1db8-4927-815b-cce6469d091e"
    # secret_key = "95DE6A929EE1E91872F0A9BD19C47CAE"
    # passphrase = "19960628,XIAyan"
    ###############

    td = coin_trade(api_key, secret_key, passphrase, flag, "ETH-USDT-SWAP")
    print(td.ask_bid())
