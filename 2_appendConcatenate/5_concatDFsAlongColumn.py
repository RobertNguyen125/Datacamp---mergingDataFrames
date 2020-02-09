import pandas as pd

weather_max = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather_max.csv')
weather_mean = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather_mean.csv')

weather_list = [weather_max, weather_mean]
weather = pd.concat(weather_list, axis='rows')
print(weather)
