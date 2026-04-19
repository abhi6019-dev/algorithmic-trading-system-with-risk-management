import numpy as np

def run_backtest(df, initial_capital=10000,
                 stop_loss=0.03,
                 take_profit=0.12,
                 risk_per_trade=0.015):

    df = df.copy()

    capital = initial_capital
    position = 0
    entry_price = 0
    position_size = 0
    best_price = 0

    portfolio_values = []
    trades = []

    for i in range(1, len(df)):
        price = df["Close"].iloc[i]
        prev_price = df["Close"].iloc[i - 1]
        signal = df["Signal"].iloc[i - 1]

        # 🟢 ENTER TRADE
        if position == 0 and signal != 0:
            position = signal
            entry_price = price
            best_price = price

            position_size = risk_per_trade / (stop_loss + 1e-6)
            position_size = min(position_size, 1)

        # 🔴 STOP LOSS
        if position == 1 and (price - entry_price) / entry_price <= -stop_loss:
            trades.append((entry_price, price, position))
            position = 0

        elif position == -1 and (entry_price - price) / entry_price <= -stop_loss:
            trades.append((entry_price, price, position))
            position = 0

        # 🟢 TAKE PROFIT
        if position == 1 and (price - entry_price) / entry_price >= take_profit:
            trades.append((entry_price, price, position))
            position = 0

        elif position == -1 and (entry_price - price) / entry_price >= take_profit:
            trades.append((entry_price, price, position))
            position = 0

        # 🔥 TRAILING STOP
        if position == 1:
            best_price = max(best_price, price)
            if (price - best_price) / best_price <= -0.02:
                trades.append((entry_price, price, position))
                position = 0

        elif position == -1:
            best_price = min(best_price, price)
            if (best_price - price) / best_price <= -0.02:
                trades.append((entry_price, price, position))
                position = 0

        # 📊 DAILY RETURN
        if position == 1:
            pnl = (price - prev_price) / prev_price * position_size
        elif position == -1:
            pnl = (prev_price - price) / prev_price * position_size
        else:
            pnl = 0

        capital *= (1 + pnl)
        portfolio_values.append(capital)

    df = df.iloc[1:]
    df["Portfolio_Value"] = portfolio_values

    return df, trades