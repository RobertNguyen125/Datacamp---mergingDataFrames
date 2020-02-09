import pandas as pd

gold = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Gold.csv')
silver = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Silver.csv')
bronze = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Bronze.csv')

# make a copy of gold: medal
medal = gold.copy()
print(medal)
new_label = ['Noc', 'Country', 'Gold']
# rename column label with new_label
medal.columns = new_label
print(medal)
# create 'Silver' and 'Bronze' columns for medal
medal['Silver'] = silver['Total']
medal['Bronze'] = bronze['Total']

print(medal.head())
