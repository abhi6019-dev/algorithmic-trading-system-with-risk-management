def analyze_trades(trades):
    profits = []

    for entry, exit_price, direction in trades:
        if direction == 1:  # long
            profit = (exit_price - entry) / entry
        else:  # short
            profit = (entry - exit_price) / entry

        profits.append(profit)

    wins = [p for p in profits if p > 0]
    losses = [p for p in profits if p < 0]

    return {
        "Total Trades": len(profits),
        "Win Rate": len(wins) / len(profits) if profits else 0,
        "Avg Win": sum(wins)/len(wins) if wins else 0,
        "Avg Loss": sum(losses)/len(losses) if losses else 0
    }