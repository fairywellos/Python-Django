path = "./logs/"
equity = open(path + "Test_BTC_EUR_kraken_equity.log", "r").read()
trades = open(path + "Test_BTC_EUR_kraken_trades.log", "r").read()
main = open(path + "Test_BTC_EUR_kraken.log", "r").read()

## get euity last line
equity_lastline = open ( path + "Test_BTC_EUR_kraken_equity.log" ,"r" ).readlines()[-1]

## get the stance from main log
with open(path + "Test_BTC_EUR_kraken.log") as f:
    for num, line in enumerate(f, 1):
        if "Stance is " in line:
            start_num = len(line) - 13
            end_num = len(line) -2
            array_str = line[int(start_num):int(end_num)].split(",")
            print(array_str)
            i = 1
            stance_0 = int(array_str[0].replace(" ", ""))
            stance_1 = int(array_str[1].replace(" ", ""))
            stance_2 = int(array_str[2].replace(" ", ""))
            stance_3 = int(array_str[3].replace(" ", ""))
            print (type(stance_0))

print(stance_0, stance_1, stance_2)

## get the orderid
orderid = ""
side = ""
comm_to_open = ""
comm_to_close = ""
cost_to_open = 0.0
comm_to_close = 0.0
qty = 0.0
entry_price = 0.0
exit_price = 0.0
mark_price = 0.0
cash = 0.0
currency = ""
can_trade = ""
symbol_trading = ""
exchange = ""
equity = 0.0
leverage = 0
with open(path + "MA-1-21_XRP_USD_kraken.log") as f:
    for num, line in enumerate(f, 1):
        if "'orderid'" in line:
            for x in line.split(","):
                if "orderid" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 1
                    end_num = len(tmp) - 1
                    orderid = tmp[start_num:end_num]
                if "side" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 1
                    end_num = len(tmp) - 1
                    side = tmp[start_num:end_num]
                if "comm_to_open" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    comm_to_open = tmp[start_num:end_num]
                if "comm_to_close" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    comm_to_close = tmp[start_num:end_num]
                if "cost_to_open" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    cost_to_open = tmp[start_num:end_num]
                if "cost_to_close" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    cost_to_close = tmp[start_num:end_num]
                if "qty" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    qty = tmp[start_num:end_num]
                if "entry_price" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    entry_price = tmp[start_num:end_num]
                if "exit_price" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    exit_price = tmp[start_num:end_num]
                if "mark_price" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    mark_price = tmp[start_num:end_num]
                if "cash" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    cash = tmp[start_num:end_num]
                if "currency" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 1
                    end_num = len(tmp) - 1
                    currency = tmp[start_num:end_num]
                if "can_trade" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    can_trade = tmp[start_num:end_num]
                if "symbol_trading" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 1
                    end_num = len(tmp) - 1
                    symbol_trading = tmp[start_num:end_num]
                if "exchange" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 1
                    end_num = len(tmp) - 1
                    exchange = tmp[start_num:end_num]
                if "equity" in x:
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp)
                    equity = tmp[start_num:end_num]
                if "leverage" in x:
                    print x
                    tmp = x.split(":")[1].replace(" ", "")
                    start_num = 0
                    end_num = len(tmp) - 2
                    leverage = tmp[start_num:end_num]

print (leverage)




# equity_json = {
#     "stance": [
#         0,
#         1,
#         -1,
#         0
#     ],
#     "orderid": null,
#     "side": null,
#     "comm_to_open": null,
#     "comm_to_close": null,
#     "cost_to_open": null,
#     "cost_to_close": null,
#     "qty": 0,
#     "entry_price": null,
#     "exit_price": null,
#     "mark_price": 7261.05,
#     "cash": 50.0,
#     "currency": "EUR",
#     "can_trade": true,
#     "symbol_trading": "BTC/EUR",
#     "exchange": "kraken",
#     "equity": 50.0
# }

