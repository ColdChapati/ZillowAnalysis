# import pandas
import pandas as pd

# read csv
data = pd.read_csv('Zip_zhvi_uc_sfr_tier_0.33_0.67_sm_sa_mon.csv')

# reduce to houses below three fifty k
data = data.loc[data['2020-12-31'] <= 350000]

# remove states
data = data[~data.State.str.contains('FL')]
data = data[~data.State.str.contains('MI')]
data = data[~data.State.str.contains('LA')]

# create appreciation data
data['Appreciation-1-year'] = data['2020-12-31'] / data['2019-12-31']
data['Appreciation-3-years'] = (data['2020-12-31'] / data['2017-12-31']) ** (1/3)
data['Appreciation-5-years'] = (data['2020-12-31'] / data['2015-12-31']) ** (1/5)
data['Appreciation-7-years'] = (data['2020-12-31'] / data['2013-12-31']) ** (1/7)

# sort appreciation data
data_one_year = data.sort_values(by='Appreciation-1-year', ascending=False)
data_three_year = data.sort_values(by='Appreciation-3-years', ascending=False)
data_five_year = data.sort_values(by='Appreciation-5-years', ascending=False)
data_seven_year = data.sort_values(by='Appreciation-7-years', ascending=False)

# save appreciation data as a new dataframe
data_one_year = pd.DataFrame(data_one_year[['RegionName', 'State', 'City', 'CountyName', 'Appreciation-1-year']][:50])
data_three_year = pd.DataFrame(data_three_year[['RegionName', 'State', 'City', 'CountyName', 'Appreciation-3-years']][:50])
data_five_year = pd.DataFrame(data_five_year[['RegionName', 'State', 'City', 'CountyName', 'Appreciation-5-years']][:50])
data_seven_year = pd.DataFrame(data_seven_year[['RegionName', 'State', 'City', 'CountyName', 'Appreciation-7-years']][:50])

# export data to csv
data_one_year.to_csv('one-year')
data_three_year.to_csv('three-years')
data_five_year.to_csv('five-years')
data_seven_year.to_csv('seven-years')
