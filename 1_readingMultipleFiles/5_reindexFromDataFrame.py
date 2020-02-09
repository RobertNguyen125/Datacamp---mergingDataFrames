import pandas as pd

name_1981 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Baby names/names1981.csv',
                        header=None, names=['name','gender','count'], index_col=[0,1])
name_1881 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Baby names/names1881.csv',
                        header=None, names=['name','gender','count'], index_col=[0,1])

print(name_1881.info())
print(name_1981.info())

# create new df 'common_name' by reindexing name_1981 with 'index' attribute of df name_1881
common_name = name_1981.reindex(name_1881.index)
print(common_name.shape)

# .dropna()
common_name = common_name.dropna()
print(common_name.shape)
