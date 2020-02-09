import pandas as pd

rain2013 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather/q1_rainfall_2013.csv',
                        index_col='Month', parse_dates=True)
rain2014 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather/q1_rainfall_2013.csv',
                        index_col='Month', parse_dates=True)

# use multilevel index for the rows
rain1314 = pd.concat([rain2013,rain2014], keys=[2013,2014], axis=0)
print(rain1314)
print(rain1314.loc[2014])

# use multilevel index for the columns
rain1314_2 = pd.concat([rain2013, rain2014], keys=[2013,2014], axis=1)
print(rain1314_2)

# concat with dict
rain_dict = {2013: rain2013, 2014: rain2014}
rain1314_3 = pd.concat(rain_dict, axis=1)
print(rain1314_3)
