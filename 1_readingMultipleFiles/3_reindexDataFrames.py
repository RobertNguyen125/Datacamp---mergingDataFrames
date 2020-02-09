# NOTE: below is not conventional
# indexes: many pandas Index data structure
# indices: many index labels within Index Data Structure

import pandas as pd

weather1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/monthly_max_temp.csv',index_col='Month')
print(weather1.head())
# sort weather1 index in alphabetical order: weather2
weather2 = weather1.sort_index()
print(weather2.head())
# sort weather1 index in reverse alphabetical order: weather3
weather3 =  weather1.sort_index(ascending=False)
print(weather3.head())
# sort weather1 numerically using 'Max TemperatureF'
weather4 = weather1.sort_values('Max TemperatureF')
