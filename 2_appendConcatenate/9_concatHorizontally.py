import pandas as pd

# hardware = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Hardware.csv', index_col="Date")
# software = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Software.csv', index_col="Date")
# service = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Service.csv', index_col="Date")

dataframes = []
for dataframe in dataframes:
    file_name = ['/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Hardware.csv',
    '/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Software.csv',
    '/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Service.csv')
    dataframes.append(file_name, index_col='Date')

february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])
