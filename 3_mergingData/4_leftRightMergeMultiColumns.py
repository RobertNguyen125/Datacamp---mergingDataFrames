import pandas as pd

managers1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/managers1.csv', index_col=0)
revenue1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/revenue1.csv', index_col=0)
sales = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/sales.csv', index_col=0)

revenue_and_sales = pd.merge(revenue1, sales, on=['city','state'], how='right')
print(revenue_and_sales)
sales_and_managers = pd.merge(sales, managers1, left_on=['city','state'], right_on=['branch','state'], how='left')
print(sales_and_managers)

merge_default = pd.merge(sales_and_managers, revenue_and_sales)
print(merge_default)

merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')
print(merge_outer)

merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, how='outer', on=['city','state'])
print(merge_outer_on)
