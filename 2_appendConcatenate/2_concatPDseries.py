import pandas as pd

jan = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-jan-2015.csv',
                    index_col='Date', parse_dates=True)
feb = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-feb-2015.csv',
                    index_col='Date', parse_dates=True)
mar = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-mar-2015.csv',
                    index_col='Date', parse_dates=True)

units=[]

for month in [jan, feb, mar]:
    units.append(month['Units'])

quarter1 = pd.concat(units, axis='rows')
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
