import pandas as pd

austin = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather/austin.csv', index_col=0)
houston = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather/houston.csv', index_col=0)

tx_weather = pd.merge_ordered(austin, houston)
print(tx_weather)
tx_weather_stuff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'])
print(tx_weather_stuff)
tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'], fill_method='ffill')
print(tx_weather_ffill)
