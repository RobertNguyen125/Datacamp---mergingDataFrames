import pandas as pd
from glob import glob

# path = r'/Users/apple/desktop/meergingDataFrames/dataset/Summer Olympic Medal'
# filenames = glob.glob(path + )
filenames = ['/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Gold.csv',
'/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Silver.csv',
'/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Bronze.csv']

df = []
for filename in filenames:
    df.append(pd.read_csv(filename))

print(df[0].head())
