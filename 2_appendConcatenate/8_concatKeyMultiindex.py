import pandas as pd
medals = []
medal_types = ['bronze', 'silver', 'gold']

for medal in medal_types:
    file_name = '/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/%s_top5.csv' % medal
    medal_df = pd.read_csv(file_name, index_col='Country')
    medals.append(medal_df)

medals = pd.concat(medals, keys=medal_types)
print(medals)

medals_sorted = medals.sort_index(level=0)
print('Germany Bronze', medals_sorted.loc[('bronze', 'Germany')])
print(medals_sorted.loc['silver'])
idx = pd.IndexSlice
print(medals_sorted.loc[idx[:,'United Kingdom'],:])
