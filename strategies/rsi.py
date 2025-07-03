import yfinance as yf

def check_rsi_signal(ticker_symbol):
    data = yf.download(ticker_symbol, period='7d', interval='1h')

    if data.empty or 'Close' not in data:
        return f"Unable to fetch data for {ticker_symbol}. Please check the symbol."

    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()

    rs = avg_gain / (avg_loss + 1e-10)
    rsi = 100 - (100 / (1 + rs))

    latest_rsi = rsi.iloc[-1]

    if latest_rsi < 30:
        return f"{ticker_symbol} is Oversold (RSI={latest_rsi:.2f}) — BUY signal 📈"
    elif latest_rsi > 70:
        return f"{ticker_symbol} is Overbought (RSI={latest_rsi:.2f}) — SELL signal 📉"
    else:
        return f"{ticker_symbol} RSI={latest_rsi:.2f} — Neutral ⚖️"
