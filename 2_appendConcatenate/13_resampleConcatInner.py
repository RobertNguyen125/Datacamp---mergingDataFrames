import pandas as pd

china  = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/GDP/china.csv', index_col= 'Year')
us  = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/GDP/us.csv', index_col= 'Year')

# since china GDP is calculated annually and U.S quarterly, need .resample() to transform data
# new df: china_annual and us_annual
china_annual = china.resample('A').last().pct_change(10).dropna()
print(china_annual.head())
us_annual = us.resample('A').last().pct_change(10).dropna()
print(us_annual)

gdp = pd.concat([china_annual, us_annual], axis=1, join='inner')

print(gdp.resample('10A').last())
