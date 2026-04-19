import numpy as np

def generate_signals(df):
    df = df.copy()

    # Momentum
    momentum = np.where(df["MA_short"] > df["MA_long"], 1, -1)

    # Mean reversion
    z = df["Z_score"]
    mean_rev = np.where(z < -1.2, 1,
               np.where(z > 1.2, -1, 0))

    # Combine
    raw_signal = momentum + mean_rev

    df["Signal"] = np.where(raw_signal > 0, 1,
                   np.where(raw_signal < 0, -1, 0))

    df["Signal"] = np.where(abs(z) < 0.5, 0, df["Signal"])

    return df