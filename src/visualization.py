import matplotlib.pyplot as plt

def plot_equity_curve(df):
    plt.figure(figsize=(12, 6))

    plt.plot(df.index, df["Portfolio_Value"], label="Strategy", linewidth=2)

    plt.title("Equity Curve", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)

    plt.savefig('outputs/charts/equity_curve.png')

def plot_with_benchmark(df):
    plt.figure(figsize=(12, 6))

    # Strategy
    plt.plot(df.index, df["Portfolio_Value"], label="Strategy", linewidth=2)

    # Buy & Hold benchmark
    buy_hold = df["Close"] / df["Close"].iloc[0] * df["Portfolio_Value"].iloc[0]
    plt.plot(df.index, buy_hold, label="Buy & Hold", linestyle="--")

    plt.title("Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)

    plt.savefig('outputs/charts/benchmark.png')

def plot_drawdown(df):
    equity = df["Portfolio_Value"]
    peak = equity.cummax()
    drawdown = (equity - peak) / peak

    plt.figure(figsize=(12, 4))
    plt.plot(df.index, drawdown, color="red")
    plt.title("Drawdown")
    plt.grid(True)
    
    plt.savefig('outputs/charts/drawdown.png')