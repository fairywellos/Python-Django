import os
from .BCH import get_each_BCH
from .BTC_USD import get_each_BTC_USD
from .BTC_USDT import get_each_BTC_USDT
from .LIVE_BTC import get_each_LIVE_BTC
from .LIVE_ETH import get_each_LIVE_ETH
from .LIVE_LTC import get_each_LIVE_LTC
from .LTC import get_each_LTC
from .XBT import get_each_XBT
from .XMR import get_each_XMR
from .XRP import get_each_XRP

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
    }
    return result

result = get_today()
print (result)