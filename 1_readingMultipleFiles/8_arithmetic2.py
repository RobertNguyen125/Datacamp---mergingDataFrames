import pandas as pd

gdp = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/GDP/gdp.csv', index_col='DATE', parse_dates=True)
print(gdp.head())

post2008 = gdp['2008':]
print(post2008.tail(8))
# resample 'post2008' to annualy: yearly | .last() to select the last day of the year for consistency
yearly = post2008.resample('A').last()
print(yearly)
# compute growth
yearly['growth']=yearly.pct_change()*100
print(yearly)
