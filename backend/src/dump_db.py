import os
from .BCH import get_total_BCH
from .BTC_USD import get_total_BTC_USD
from .BTC_USDT import get_total_BTC_USDT
from .LIVE_BTC import get_total_LIVE_BTC
from .LIVE_ETH import get_total_LIVE_ETH
from .LIVE_LTC import get_total_LIVE_LTC
from .LTC import get_total_LTC
from .XBT import get_total_XBT
from .XMR import get_total_XMR
from .XRP import get_total_XRP
from .test import get_total_Test_BTC

def get_total():
    result = {
        "BCH": get_total_BCH(),
        "BTC_USD": get_total_BTC_USD(),
        "BTC_USDT": get_total_BTC_USDT(),
        "LIVE_BTC": get_total_LIVE_BTC(),
        "LIVE_ETH": get_total_LIVE_ETH(),
        "LIVE_LTC": get_total_LIVE_LTC(),
        "LTC": get_total_LTC(),
        "XBT": get_total_XBT(),
        "XMR": get_total_XMR(),
        "XRP": get_total_XRP(),
        "TEST_BTC_EUR": get_total_Test_BTC(),
    }
    return result

# result = get_today()
# print (result)