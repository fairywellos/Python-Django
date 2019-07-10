path = "../../logs/"

today_equity_line = open ( path + "Test_BTC_EUR_kraken_equity.log" ,"r" ).readlines()[-1].split(",")
today_trades_line = open ( path + "Test_BTC_EUR_kraken_trades.log" ,"r" ).readlines()[-1].split("\t")

## set initial value
strategy = "Test_BTC_EUR"
date = ""
quantity = ""
entry = ""
last_price = ""
buy_or_sell = ""
returns = ""
equity = ""

## get each info
def get_each_Test_BTC():
    total_trades = open ( path + "Test_BTC_EUR_kraken_trades.log" ,"r" ).readlines()
    last_start_date = total_trades[0].split("\t")[0].split(" ")[0]
    print (last_start_date)
    for line in total_trades:
        if len(line.split("\t")) < 3:
            last_start_date = line.split("\t")[0].split(" ")[0]
            "**********"
            print(last_start_date)
    import datetime
    date = last_start_date
    current_date = today_trades_line[0].split(" ")[0]
    formated_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    str_date = formated_date.strftime("%m-%d-%Y")
    date = str_date
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

def get_monthly_Test_BTC():
    total_trades = open ( path + "Test_BTC_EUR_kraken_trades.log" ,"r" ).readlines()
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

###### Will use in the future

## get the stance from main log
# with open(path + "Test_BTC_EUR_kraken.log") as f:
#     for num, line in enumerate(f, 1):
#         if "Stance is " in line:
#             start_num = len(line) - 13
#             end_num = len(line) -2
#             array_str = line[int(start_num):int(end_num)].split(",")
#             print(array_str)
#             i = 1
#             stance_0 = int(array_str[0].replace(" ", ""))
#             stance_1 = int(array_str[1].replace(" ", ""))
#             stance_2 = int(array_str[2].replace(" ", ""))
#             stance_3 = int(array_str[3].replace(" ", ""))
#             print (type(stance_0))

# print(stance_0, stance_1, stance_2)


###### Will use in the future

## get the orderid
# orderid = ""
# side = ""
# comm_to_open = ""
# comm_to_close = ""
# cost_to_open = 0.0
# comm_to_close = 0.0
# qty = 0.0
# entry_price = 0.0
# exit_price = 0.0
# mark_price = 0.0
# cash = 0.0
# currency = ""
# can_trade = ""
# symbol_trading = ""
# exchange = ""
# equity = 0.0
# leverage = 0
# with open(path + "MA-1-21_XRP_USD_kraken.log") as f:
#     for num, line in enumerate(f, 1):
#         if "'orderid'" in line:
#             for x in line.split(","):
#                 if "orderid" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 1
#                     end_num = len(tmp) - 1
#                     orderid = tmp[start_num:end_num]
#                 if "side" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 1
#                     end_num = len(tmp) - 1
#                     side = tmp[start_num:end_num]
#                 if "comm_to_open" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     comm_to_open = tmp[start_num:end_num]
#                 if "comm_to_close" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     comm_to_close = tmp[start_num:end_num]
#                 if "cost_to_open" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     cost_to_open = tmp[start_num:end_num]
#                 if "cost_to_close" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     cost_to_close = tmp[start_num:end_num]
#                 if "qty" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     qty = tmp[start_num:end_num]
#                 if "entry_price" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     entry_price = tmp[start_num:end_num]
#                 if "exit_price" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     exit_price = tmp[start_num:end_num]
#                 if "mark_price" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     mark_price = tmp[start_num:end_num]
#                 if "cash" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     cash = tmp[start_num:end_num]
#                 if "currency" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 1
#                     end_num = len(tmp) - 1
#                     currency = tmp[start_num:end_num]
#                 if "can_trade" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     can_trade = tmp[start_num:end_num]
#                 if "symbol_trading" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 1
#                     end_num = len(tmp) - 1
#                     symbol_trading = tmp[start_num:end_num]
#                 if "exchange" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 1
#                     end_num = len(tmp) - 1
#                     exchange = tmp[start_num:end_num]
#                 if "equity" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp)
#                     equity = tmp[start_num:end_num]
#                 if "leverage" in x:
#                     tmp = x.split(":")[1].replace(" ", "")
#                     start_num = 0
#                     end_num = len(tmp) - 2
#                     leverage = tmp[start_num:end_num]


