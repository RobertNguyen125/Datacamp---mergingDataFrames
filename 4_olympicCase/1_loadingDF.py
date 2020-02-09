import pandas as pd
editions = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/edition.tsv', sep='\t')


editions = editions[['Edition', 'Grand Total', 'City', 'Country']]
print(editions)
ioc = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/ioc.csv')
ioc = ioc[['Country', 'NOC']]
print(ioc)
