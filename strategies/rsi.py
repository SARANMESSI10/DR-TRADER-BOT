import yfinance as yf

def should_buy(symbol):
    data = yf.download(symbol, period='7d', interval='1h')
    close_prices = data['Close']
    rsi = compute_rsi(close_prices)

    return rsi[-1] < 30

def should_sell(symbol):
    data = yf.download(symbol, period='7d', interval='1h')
    close_prices = data['Close']
    rsi = compute_rsi(close_prices)

    return rsi[-1] > 70

def compute_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
