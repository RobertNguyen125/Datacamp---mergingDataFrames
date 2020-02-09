import pandas as pd

jan = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-jan-2015.csv',
                    index_col='Date', parse_dates=True)
feb = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-feb-2015.csv',
                    index_col='Date', parse_dates=True)
mar = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-mar-2015.csv',
                    index_col='Date', parse_dates=True)
print(jan.head())

jan_unit = jan['Units']
feb_unit = feb['Units']
mar_unit = mar['Units']

quarter1 = jan_unit.append(feb_unit).append(mar_unit)

print(quarter1)
print(quarter1.loc['2015-01-27':'2015-02-02'])
print(quarter1.loc['2015-02-26':'2015-03-07'])
print(quarter1.sum())
