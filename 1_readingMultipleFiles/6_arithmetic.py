import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pittsburgh2013.csv'
                    , index_col = 'Date', parse_dates=True)

print(weather.columns)

# broadcasting scalar multiplication
print(weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn']*2.54)

# absolute temperature range
w1_range = weather.loc['2013-7-1':'2013-7-7',['Min TemperatureF', 'Max TemperatureF']]
print(w1_range)
# slice the mean temp from w1
w1_mean = weather.loc['2013-7-1':'2013-7-7', 'Mean TemperatureF']
print(w1_mean)
# relative temperature range
print(w1_range.divide(w1_mean, axis='rows'))
#percentage change: .pct_change()
print(w1_mean.pct_change()*100)

# examine how arithmetic works across different dataframe with different indexes
gold = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/gold_top5.csv', index_col=0)
silver = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/silver_top5.csv', index_col=0)
bronze = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/bronze_top5.csv',index_col=0)
# use .add() method to sum between DFs
print(bronze.add(silver, fill_value=0)) # NOTE: default fill_value = NaN
print(bronze.add(silver, fill_value=0).add(gold, fill_value=0))
