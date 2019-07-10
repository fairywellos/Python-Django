import os
from .BCH import get_each_BCH, get_monthly_BCH
from .BTC_USD import get_each_BTC_USD, get_monthly_BTC_USD
from .BTC_USDT import get_each_BTC_USDT, get_monthly_BTC_USDT
from .LIVE_BTC import get_each_LIVE_BTC, get_monthly_LIVE_BTC
from .LIVE_ETH import get_each_LIVE_ETH, get_monthly_LIVE_ETH
from .LIVE_LTC import get_each_LIVE_LTC, get_monthly_LIVE_LTC
from .LTC import get_each_LTC, get_monthly_LTC
from .XBT import get_each_XBT, get_monthly_XBT
from .XMR import get_each_XMR, get_monthly_XMR
from .XRP import get_each_XRP, get_monthly_XRP
from .test import get_each_Test_BTC, get_monthly_Test_BTC

def get_today():
    result = {
        "BCH": get_each_BCH(),
        "BTC_USD": get_each_BTC_USD(),
        "BTC_USDT": get_each_BTC_USDT(),
        "LIVE_BTC": get_each_LIVE_BTC(),
        "LIVE_ETH": get_each_LIVE_ETH(),
        "LIVE_LTC": get_each_LIVE_LTC(),
        "LTC": get_each_LTC(),
        "XBT": get_each_XBT(),
        "XMR": get_each_XMR(),
        "XRP": get_each_XRP(),
        "TEST_BTC_EUR": get_each_Test_BTC(),
    }
    return result

def get_monthly():
    result = {
        "BCH": get_monthly_BCH(),
        "BTC_USD": get_monthly_BTC_USD(),
        "BTC_USDT": get_monthly_BTC_USDT(),
        "LIVE_BTC": get_monthly_LIVE_BTC(),
        "LIVE_ETH": get_monthly_LIVE_ETH(),
        "LIVE_LTC": get_monthly_LIVE_LTC(),
        "LTC": get_monthly_LTC(),
        "XBT": get_monthly_XBT(),
        "XMR": get_monthly_XMR(),
        "XRP": get_monthly_XRP(),
        "TEST_BTC_EUR": get_monthly_Test_BTC(),
    }
    print (result)
    return result