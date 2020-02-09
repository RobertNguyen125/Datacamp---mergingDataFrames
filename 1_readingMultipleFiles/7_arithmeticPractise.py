import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/pittsburgh2013.csv',
                    index_col="Date", parse_dates=True)

print(weather.head())

temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]
# print(type(temps_f))
temps_c = (temps_f-32)*5/9 # NOTE: this is possible because both DFs have the same index
temps_c.columns=temps_c.columns.str.replace('F', 'C')
print(temps_c)
