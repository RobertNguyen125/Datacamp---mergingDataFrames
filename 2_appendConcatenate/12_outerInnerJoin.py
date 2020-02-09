import pandas as pd

gold = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/gold_top5.csv',index_col='Country')
silver = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/silver_top5.csv',index_col='Country')
bronze = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/bronze_top5.csv',index_col='Country')

medal_list = [bronze, silver, gold]

medals = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, join='inner')
print(medals)
