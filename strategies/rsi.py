# strategies/rsi.py

import yfinance as yf
import pandas as pd

def compute_rsi(data, period=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def should_buy(symbol):
    data = yf.download(symbol, period="7d", interval="1h")
    rsi = compute_rsi(data['Close'])

    if rsi.iloc[-1] < 30:
        return True
    return False

def should_sell(symbol):
    data = yf.download(symbol, period="7d", interval="1h")
    rsi = compute_rsi(data['Close'])

    if rsi.iloc[-1] > 70:
        return True
    return False
