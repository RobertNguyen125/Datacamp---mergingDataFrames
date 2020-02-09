import pandas as pd

revenue = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/revenue.csv', index_col=0)
managers = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/managers.csv', index_col=0)

print(revenue)
print(managers)

merge_by_city = pd.merge(revenue, managers, on='city')
print(merge_by_city)

merge_by_id = pd.merge(revenue, managers, on='branch_id')
print(merge_by_id)

revenue1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/revenue1.csv', index_col=0)
managers1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/managers1.csv', index_col=0)
print(revenue1)
print(managers1)

combined = pd.merge(revenue1, managers1, left_on='city', right_on='branch')
print(combined)
