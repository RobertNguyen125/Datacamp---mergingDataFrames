import pandas as pd

medals = []
medal_types = ['bronze', 'silver', 'gold']
for medal in medal_types:
        # use string interpolation: % medal from list 'medal_types' will replace %s
        file_names='/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/%s_top5.csv' % medal
        # create list of columns for new medal_df
        columns = ['Country', medal]
        medal_df = pd.read_csv(file_names, header=0, index_col='Country', names=columns)
        medals.append(medal_df)
medals_df = pd.concat(medals, axis='columns')
print(medals_df)
