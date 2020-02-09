import pandas as pd

revenue1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/revenue1.csv', index_col=0)
managers1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/managers1.csv', index_col=0)


managers1.columns=['city','branch_id','state','manager']

combined = pd.merge(revenue1, managers1, on=['branch_id', 'city', 'state'])
print(combined)
