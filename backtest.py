def backtest(df, entry_signal, exit_signal):
    position = False
    trades = []

    for i in range(len(df)):
        if entry_signal.iloc[i] and not position:
            entry_price = df.iloc[i]["close"]
            entry_date = df.iloc[i]["date"]
            position = True

        elif exit_signal.iloc[i] and position:
            exit_price = df.iloc[i]["close"]
            exit_date = df.iloc[i]["date"]
            trades.append((entry_date, exit_date, exit_price - entry_price))
            position = False

    return trades
