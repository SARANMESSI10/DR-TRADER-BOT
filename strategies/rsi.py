import yfinance as yf

def check_rsi_signal(symbol="AAPL"):
    data = yf.download(symbol, period="14d", interval="1d")
    close = data['Close']

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=14).mean().iloc[-1]
    avg_loss = loss.rolling(window=14).mean().iloc[-1]

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    if rsi > 70:
        return f"⚠️ {symbol} RSI = {rsi:.2f} → Overbought! Consider Selling."
    elif rsi < 30:
        return f"✅ {symbol} RSI = {rsi:.2f} → Oversold! Consider Buying."
    else:
        return f"ℹ️ {symbol} RSI = {rsi:.2f} → Neutral."
