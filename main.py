from src.data_loader import load_data
from src.indicators import add_indicators
from src.strategy import generate_signals
from src.backtest import run_backtest
from src.metrics import *
from src.trade_analysis import analyze_trades
from src.visualization import plot_equity_curve, plot_with_benchmark, plot_drawdown

def main():
    # 📊 Load data
    data = load_data("AAPL", "2015-01-01", "2025-01-01")

    
    # 🧠 Add indicators
    data = add_indicators(data)

    # ⚙️ Generate trading signals
    data = generate_signals(data)

    # 🧪 Run backtest
    data, trades = run_backtest(data, 10000)

    # 📈 Calculate returns
    data = calculate_returns(data)

    # 📊 Performance metrics
    print("\n📊 PERFORMANCE METRICS")
    print("Total Return:", total_return(data))
    print("CAGR:", cagr(data))
    print("Sharpe:", sharpe_ratio(data))
    print("Max Drawdown:", max_drawdown(data))
    print("Volatility:", volatility(data))

    # 📈 Trade analysis
    stats = analyze_trades(trades)

    print("\n📈 TRADE ANALYSIS")
    for k, v in stats.items():
        print(f"{k}: {v}")

    plot_equity_curve(data)
    plot_with_benchmark(data)
    plot_drawdown(data)


if __name__ == "__main__":
    main()