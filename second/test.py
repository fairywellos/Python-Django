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
            array_str = line[start_num:end_num].split(",")
            print(array_str)
            i = 1
            stance_0 = int(array_str[0].replace(" ", ""))
            stance_1 = int(array_str[1].replace(" ", ""))
            stance_2 = int(array_str[2].replace(" ", ""))
            stance_3 = int(array_str[3].replace(" ", ""))
            print (type(stance_0))

print(stance_0, stance_1, stance_2)





test_dic = {}
print (equity_lastline)

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

