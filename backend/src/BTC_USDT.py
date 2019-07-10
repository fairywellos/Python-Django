path = "../../logs/"

## get equity last line
today_equity_line = open ( path + "MA-1-21_BTC_USDT_binance_equity.log" ,"r" ).readlines()[-1].split(",")
today_trades_line = open ( path + "MA-1-21_BTC_USDT_binance_trades.log" ,"r" ).readlines()[-1].split("\t")

## set initial value
strategy = "MA-1-21_BTC_USDT"
date = ""
quantity = ""
entry = ""
last_price = ""
buy_or_sell = ""
returns = ""
equity = ""

## get each info
def get_each_BTC_USDT():
    total_trades = open ( path + "MA-1-21_BTC_USDT_binance_trades.log" ,"r" ).readlines()
    last_start_date = total_trades[0].split("\t")[0].split(" ")[0]
    print (last_start_date)
    for line in total_trades:
        if len(line.split("\t")) < 3:
            last_start_date = line.split("\t")[0].split(" ")[0]
            "**********"
            print(last_start_date)
    import datetime
    date = last_start_date
    formated_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    str_date = formated_date.strftime("%m-%d-%Y")
    date = str_date
    current_date = today_trades_line[0].split(" ")[0]
    quantity = today_equity_line[1].replace(" ", "")
    entry = today_equity_line[2].replace(" ", "")

    if "BUY" in today_trades_line[0]:
        buy_or_sell = "Buy"
    else:
        buy_or_sell = "Sell"

    if len(today_trades_line) > 2:
        last_price = today_trades_line[2]
        returns = today_trades_line[3].replace("\n", "")
    else:
        last_price = ""
        returns = ""

    equity = today_equity_line[6].replace("\n", "").replace(" ", "")
    result = {
        "strategy": strategy,
        "date": date,
        "current_date": current_date,
        "quantity": quantity,
        "entry": entry,
        "last_price": last_price,
        "buy_or_sell": buy_or_sell,
        "returns": returns,
        "equity": equity
    }

    return result
# get_each_info()
# print(date, quantity, entry, last_price, buy_or_sell, returns, equity)

def get_monthly_BTC_USDT():
    total_trades = open ( path + "MA-1-21_BTC_USDT_binance_trades.log" ,"r" ).readlines()
    returns_date = total_trades[0].split("\t")[0].split(" ")[0]
    if len(total_trades[0].split("\t")) > 2:
        returns_value = total_trades[0].split("\t")[3].replace("\n", "")
    else:
        returns_value = ""
    for line in total_trades:
        line_date = line.split("\t")[0].split(" ")[0]
        # if len(line.split("\t")) > 2:
        #     returns_value = line.split("\t")[3].replace("\n", "")
        # else:
        #     returns_value = ""
        #     returns_date = line.split("\t")[0].split(" ")[0]
        if line_date[8] == '3':
            returns_date = line.split("\t")[0].split(" ")[0]
            if len(line.split("\t")) > 2:
                returns_value = line.split("\t")[3].replace("\n", "")
            else:
                returns_value = ""
    print(returns_date, returns_value)
    return {
        "strategy": strategy,
        "month": returns_date,
        "returns": returns_value,
    }