import pandas as pd

weather1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/weather1.csv', index_col='Month')

year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# reindex weather1 with 'year': weather2
weather2 = weather1.reindex(year)
print(weather2)
# reindex weather1 with 'year' and ffill(): weather3
weather3 = weather1.reindex(year).ffill()
print(weather3)
