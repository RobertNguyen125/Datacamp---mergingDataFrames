import pandas as pd

jan = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-jan-2015.csv',
                    index_col='Date', parse_dates=True)
feb = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-feb-2015.csv',
                    index_col='Date', parse_dates=True)
mar = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/sales/sales-mar-2015.csv',
                    index_col='Date', parse_dates=True)

month_list =  [('january', jan), ('february', feb), ('march', mar)]

month_dict = {}

for month_name, month_data in month_list:
    month_dict[month_name] = month_data.groupby('Company').sum()

sales = pd.concat(month_dict)
print(sales)

idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'],:])
