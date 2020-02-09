import pandas as pd

pop1 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/population_01.csv', index_col=0)
pop2 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/population_02.csv', index_col=0)

print(pop1, type(pop1), pop1.shape)
print(pop2, type(pop2), pop2.shape)

pop0 = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/population_00.csv', index_col=0)
unemployment = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/unemployment_00.csv', index_col=0)

# print(pop0.append(unemployment))
print(pd.concat([pop0, unemployment], axis=0)) # NOTE: stack DFs vertically
print(pd.concat([pop0, unemployment], axis=1)) # NOTE: stack DFs horizontally
