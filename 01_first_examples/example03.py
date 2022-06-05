#https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836
# Import package
import yfinance as yf

# Get the data
data = yf.download(tickers="MSFT", period="5d", interval="1m")

# Print the data
print(data.tail())
