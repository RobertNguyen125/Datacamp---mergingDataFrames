import pandas as pd

sp500 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sp500.csv', index_col='Date', parse_dates=True)
exchange = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/exchange.csv', index_col='Date', parse_dates=True)
print(exchange.head())
dollars = sp500[['Open', 'Close']]
print(dollars.head())

pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')
print(pounds.head())
