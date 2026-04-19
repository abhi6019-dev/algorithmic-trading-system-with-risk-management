import pandas as pd

def add_indicators(df):
    df = df.copy()

    # Moving averages
    df["MA_short"] = df["Close"].rolling(5).mean()
    df["MA_long"] = df["Close"].rolling(20).mean()

    # Z-score
    mean = df["Close"].rolling(20).mean()
    std = df["Close"].rolling(20).std()

    df["Z_score"] = (df["Close"] - mean) / std

    return df