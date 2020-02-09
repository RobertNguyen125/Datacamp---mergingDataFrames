import pandas as pd

population = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/pa_zipcode_population.csv')
print(population.head())
cities = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/pa_zipcode_city.csv')
print(cities)
counties = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pa/pa_counties.csv')
print(counties)

print(pd.merge(population, cities)) # NOTE: inner join
print(pd.merge(counties, cities, left_on='CITY NAME', right_on='City'))



# gold = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Gold.csv',index_col='Country')
# silver = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Silver.csv',index_col='Country')
# bronze = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Summer_Olympic_medals/Bronze.csv',index_col='Country')
#
# # print(gold.head())
# gold_sorted = gold.sort_values('Total')
# # print(gold_sorted)
# silver_sorted = silver.sort_values('Total')
# # print(silver_sorted)
# bronze_sorted = bronze.sort_values('Total')
# # print(bronze_sorted)
#
# print(pd.merge(bronze_sorted, gold_sorted, on='NOC'))
