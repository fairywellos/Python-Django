path = "logs/"

## get equity last line
today_equity_line = open ( path + "MA-1-21_BTC_USD_kraken_equity.log" ,"r" ).readlines()[-1].split(",")
today_trades_line = open ( path + "MA-1-21_BTC_USD_kraken_trades.log" ,"r" ).readlines()[-1].split("\t")

## set initial value
strategy = "MA-1-21_BTC_USD"
date = ""
quantity = ""
entry = ""
last_price = ""
buy_or_sell = ""
returns = ""
equity = ""

## get each info
def get_each_BTC_USD():
    date = today_equity_line[0].split(" ")[0]
    quantity = today_equity_line[1].replace(" ", "")
    entry = today_equity_line[2].replace(" ", "")
    last_price = today_trades_line[2]
    if "BUY" in today_trades_line[0]:
        buy_or_sell = "Buy"
    else:
        buy_or_sell = "Sell"
    returns = today_trades_line[3].replace("\n", "")
    equity = today_equity_line[6].replace("\n", "").replace(" ", "")
    result = {
        "strategy": strategy,
        "date": date,
        "quantity": quantity,
        "entry": entry,
        "last_price": last_price,
        "buy_or_sell": buy_or_sell,
        "returns": returns,
        "equity": equity
    }

    return result
# print(date, quantity, entry, last_price, buy_or_sell, returns, equity)
# get_each_info()