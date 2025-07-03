import yfinance as yf
import pandas as pd

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def check_rsi_signal(symbol='BTC-USD'):
    df = yf.download(symbol, period="1mo", interval="1h")
    df.dropna(inplace=True)
    df['RSI'] = calculate_rsi(df)

    latest_rsi = df['RSI'].iloc[-1]
    
    if latest_rsi < 30:
        return f"📉 RSI is {latest_rsi:.2f}: *Oversold* signal on {symbol}. Consider Buying."
    elif latest_rsi > 70:
        return f"📈 RSI is {latest_rsi:.2f}: *Overbought* signal on {symbol}. Consider Selling."
    else:
        return f"⚖️ RSI is {latest_rsi:.2f}: Neutral zone on {symbol}."
