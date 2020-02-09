import pandas as pd

hardware = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Hardware.csv', parse_dates=['Date']).sort_values('Date')
service = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Service.csv', parse_dates=['Date']).sort_values('Date')
software = pd.read_csv('/Users/apple/desktop/meergingDataFrames/dataset/Sales/feb-sales-Software.csv', parse_dates=['Date']).sort_values('Date')

# because there are no common value in 'Date' column, we need to specify the how='outer'
pd.merge(hardware, software, how='outer').sort_values('Date')

# merge_ordered()
print(pd.merge_ordered(hardware, software).head()) # NOTE: this is an outer join
print(pd.merge_ordered(hardware, software, on=['Date', 'Company'], suffixes=['_hardware','_software']).head())
