import pandas as pd
import numpy as np
# NOTE:
# np.arange: include the start but exclude the end
# np.reshape(x,y): change the shape of the array (matrix). (x,y) must be dividable by arange(X)
a = np.arange(8).reshape(2,4) + 0.1
print('a', a)
b = np.arange(6).reshape(2,3) + 0.2
print('b', b)
c = np.arange(12).reshape(3,4) + 0.3
print('c', c)

# stack arrays horizontally: np.hstack([b,a])
print(np.hstack([b,a]))

# or np.concatenate: both array must have the same number of rows
print(np.concatenate([b,a], axis=1))

# stack arrays vertically:
print(np.vstack([a,c]))
print(np.concatenate([a,c], axis=0)) # NOTE: both needs have the same columns

# --------------------------------------------------------------------------------
pop = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/population_00.csv', index_col=0)
unemployment = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/unemployment_00.csv', index_col=0)

inner = pd.concat([pop, unemployment], axis=1, join='inner')
print(inner)
outer = pd.concat([pop, unemployment], axis=1, join='outer')
print(outer)
