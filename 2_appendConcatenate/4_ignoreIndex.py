import pandas as pd

names_1981 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Baby names/names1981.csv')
names_1881 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Baby names/names1881.csv')
# create list of labels
column_list = ['name', 'gender', 'count']

# add label to list to DFs
names_1981.columns= column_list
names_1881.columns = column_list
# add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981
# inspect the DF after adding 'year' columns
print(names_1881.head())
# create new DF with ignore_index=True:
combined_names = names_1881.append(names_1981, ignore_index=True)
# print(names_1981.shape)
# print(names_1881.shape)
print(combined_names.head())
# print all rows contain the name 'Morgan':
print(combined_names.loc[combined_names['name']=='Morgan'])
