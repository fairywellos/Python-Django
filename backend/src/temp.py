path = "../logs/"

## get equity last line
today_equity_line = open ( path + "LIVE_MA-1-21_BTC_USD_kraken_equity.log" ,"r" ).readlines()[-1].split(",")
today_trades_line = open ( path + "LIVE_MA-1-21_BTC_USD_kraken_trades.log" ,"r" ).readlines()[-1].split("\t")

## set initial value
# strategy = "LIVE_MA-1-21_BTC_USD"
# date = ""
# quantity = ""
# entry = ""
# last_price = ""
# buy_or_sell = ""
# returns = ""
# equity = ""

## get each info


# def get_each_LIVE_BTC():
#     date = today_equity_line[0].split(" ")[0]
#     quantity = today_equity_line[1].replace(" ", "")
#     entry = today_equity_line[2].replace(" ", "")

#     if "BUY" in today_trades_line[0]:
#         buy_or_sell = "Buy"
#     else:
#         buy_or_sell = "Sell"

#     if len(today_trades_line) > 2:
#         last_price = today_trades_line[2]
#         returns = today_trades_line[3].replace("\n", "")
#     else:
#         last_price = ""
#         returns = ""

#     equity = today_equity_line[6].replace("\n", "").replace(" ", "")

#     result = {
#         "strategy": strategy,
#         "date": date,
#         "quantity": quantity,
#         "entry": entry,
#         "last_price": last_price,
#         "buy_or_sell": buy_or_sell,
#         "returns": returns,
#         "equity": equity
#     }

#     return result

# len_equity = 0
# len_trades = 0



def get_total_LIVE_BTC():
    total_equity = open ( path + "LIVE_MA-1-21_BTC_USD_kraken_equity.log" ,"r" ).readlines()
    total_trades = open ( path + "LIVE_MA-1-21_BTC_USD_kraken_trades.log" ,"r" ).readlines()

    ## compare start date of quity and trades log for each strategy in order to save data to db.
    start_date_equity = total_equity[1].split(",")[0].split(" ")[0].replace("-", "/")
    start_date_trade = total_trades[0].split("\t")[0].split(" ")[0].replace("-", "/")
    print(start_date_equity, start_date_trade)
    import datetime
    format_equity = '%Y/%d/%m' # The format
    format_trade = '%Y/%m/%d' # The format
    datetime_start_equity = datetime.datetime.strptime(start_date_equity, format_equity)
    datetime_start_trade = datetime.datetime.strptime(start_date_trade, format_trade)

    # print(datetime_start_equity.date(), datetime_start_trade.date())

    #####################################
    total_for_each = []
    result = {}
    #####################################
    if datetime_start_equity.date() < datetime_start_trade.date():
        i = 1
        while i < len(total_equity):

            # initialize values
            strategy = "LIVE_MA-1-21_BTC_USD"
            date = ""
            quantity = ""
            entry = ""
            last_price = ""
            buy_or_sell = ""
            returns = ""
            equity = ""

            # get the value of date, quantity, entry, equity from equity.log file

            tmp_equity = total_equity[i].split(",")
            date = tmp_equity[0].split(" ")[0]
            quantity = tmp_equity[1].replace(" ", "")
            entry = tmp_equity[2].replace(" ", "")
            equity = tmp_equity[6].replace("\n", "").replace(" ", "")

            ## date format change: '2019-18-06' => '2019-06-18'

            formated_date = datetime.datetime.strptime(date, "%Y-%d-%m")
            str_date = formated_date.strftime("%Y-%m-%d")

            # get the value of buy_or_sell, last_price, returns in trades.log file
            with open(path + "LIVE_MA-1-21_BTC_USD_kraken_trades.log") as f:
                for num, line in enumerate(f, 1):
                    if str_date in line:
                        tmp_trade = line.split("\t")
                        if "BUY" in tmp_trade[0]:
                            buy_or_sell = "Buy"
                        else:
                            buy_or_sell = "Sell"

                        if len(tmp_trade) > 2:
                            last_price = tmp_trade[2]
                            returns = tmp_trade[3].replace("\n", "")

            i += 1      ## increase index
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
            # print("here is answer", strategy, date, quantity, entry, last_price, buy_or_sell, returns, equity)
    else:
        i = 0
        while i < len(total_trades):
            print (total_trades[i])
            i += 1

print (get_total_LIVE_BTC())
# get_each_info()

# print(date, quantity, entry, last_price, buy_or_sell, returns, equity)
