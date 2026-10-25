#!/usr/bin/env python3
"""Single-security end-of-day indicators from adjusted-close and share volume."""

import argparse
import json
import numpy as np
import pandas as pd


def analyze(frame):
    df = frame.copy()
    for field in ("date", "adjusted_close", "volume"):
        if field not in df:
            raise ValueError(f"Missing {field}")
    if "symbol" in df and df["symbol"].nunique() != 1:
        raise ValueError("One security per input")
    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df = df.sort_values("date")
    if df["date"].duplicated().any() or len(df) < 250:
        raise ValueError("At least 250 distinct trading dates required")
    close = pd.to_numeric(df["adjusted_close"], errors="raise").astype(float)
    volume = pd.to_numeric(df["volume"], errors="raise").astype(float)
    if (
        not np.isfinite(close).all()
        or not np.isfinite(volume).all()
        or (close <= 0).any()
        or (volume < 0).any()
    ):
        raise ValueError("Invalid price or volume")
    delta = close.diff()
    # True Wilder RSI: initial 14-session arithmetic mean, then alpha=1/14 recurrence.
    gains = delta.clip(lower=0).to_numpy()
    losses = (-delta.clip(upper=0)).to_numpy()
    avg_gain = float(gains[1:15].mean())
    avg_loss = float(losses[1:15].mean())
    for i in range(15, len(close)):
        avg_gain = (avg_gain * 13 + gains[i]) / 14
        avg_loss = (avg_loss * 13 + losses[i]) / 14
    rsi = (
        50.0
        if avg_gain == avg_loss == 0
        else 100.0
        if avg_loss == 0
        else 100 - 100 / (1 + avg_gain / avg_loss)
    )
    macd = (
        close.ewm(span=12, adjust=False).mean()
        - close.ewm(span=26, adjust=False).mean()
    )
    signal = macd.ewm(span=9, adjust=False).mean()
    ma50 = close.rolling(50).mean()
    ma200 = close.rolling(200).mean()
    cross = ((ma50 > ma200) & (ma50.shift() <= ma200.shift())).tail(15).any()
    nonzero = volume.where(volume > 0)
    base = nonzero.shift().rolling(20, min_periods=15).mean()
    return {
        "as_of": df["date"].iloc[-1].isoformat(),
        "sessions": len(df),
        "rsi14": float(rsi),
        "macd": float(macd.iloc[-1]),
        "macd_signal": float(signal.iloc[-1]),
        "sma50": float(ma50.iloc[-1]),
        "sma200": float(ma200.iloc[-1]),
        "golden_cross_last15": bool(cross),
        "volume_surge_last10": bool((nonzero / base >= 2).tail(10).any()),
        "adjustment": "input must use one consistent adjusted-close vintage",
        "zero_volume_sessions": int((volume == 0).sum()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    print(
        json.dumps(
            analyze(pd.read_csv(args.csv)),
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
    )


if __name__ == "__main__":
    main()
