import pandas as pd
pd.options.mode.chained_assignment = None


#data read start
data = pd.read_csv('weather.csv', names = [
                                            'country',
                                            'state',
                                            'city',
                                            'postal_code',
                                            'observation_date',
                                            'day_of_year',
                                            'temp_min_f',
                                            'temp_max_f',
                                            'temp_avg_f',
                                            'total_precip_in',
                                            'total_snowfall_in',
                                            'total_snowdepth_in_state'                                             
                                             ]) 
print(data.head(5))
print('\n\n\n')
#data read end


#What is the range of dates in the dataset?
min_date = data.observation_date.min()
max_date = data.observation_date.max()
print('[1]  What is the range of dates in the dataset?')
print(f'Ans: Range of dates in the given dataset : {min_date} to {max_date}\n\n\n')


#How many countries are included in the dataset?
distinct_countries = data.country.nunique()
print('[2]  How many countries are included in the dataset?')
print(f'Ans: Total {distinct_countries} distinct countries are included in the dataset\n\n\n')



#What is the coldest day ever recorded in Toronto? How cold was it?
toronto_data = data[data['city'] == 'Toronto']

min_temp = toronto_data.temp_min_f.min()
coldest_row = toronto_data[toronto_data['temp_min_f'] == min_temp]
coldest_date = coldest_row.observation_date

print('[3]  What is the coldest day ever recorded in Toronto? How cold was it?')
print('Ans: Date(s) of coldest days are:')
c=0
for x in coldest_date:
    c+=1
    print(f'     {c}) : {x}')
print(f'\n     Coldest day temperature : {min_temp} fahrenheit \n\n\n')






#What is the snowfall total for Denver in 2014?
denver_data = data[data['city'] == 'Denver']
denver_data = denver_data[pd.DatetimeIndex(denver_data['observation_date']).year == 2014]
snowfall_total = sum(denver_data['total_snowfall_in'])
print('[4]  What is the snowfall total for Denver in 2014?')
print(f'Ans: Snowfall total for Denver in year 2014 is {snowfall_total}\n\n\n')






#What are the top 5 rainiest cities in 2018? How much rain did each receive? 
#Assume rain to be the amount of total precipitation minus any snowfall.
data_2018 = data[pd.DatetimeIndex(data['observation_date']).year == 2018]
data_2018['rain'] = data_2018['total_precip_in'] - data_2018['total_snowfall_in']
sorted_data_2018 = data_2018.sort_values(by = 'rain',ascending=False)

result = sorted_data_2018.head(5)
print('[5]  What are the top 5 rainiest cities in 2018? How much rain did each receive?')
print('Ans: Top 5 rainiest cities in 2018 are')
c=0
for x,y in zip(result.city, result.rain):
    c+=1
    print(f'     {c}) city : {x} with rain = {y}')

print('\n\n\n')




#How many days in each month of 2019 did Olympia, Washington see some sort of precipitation falling?
data_2019 = data[pd.DatetimeIndex(data['observation_date']).year == 2019]
washington_data_2019 = data_2019[data_2019['state'] == 'Washington']
olympia_data_2019 = washington_data_2019[washington_data_2019['city'] == 'Olympia']

data_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
from datetime import datetime
for x,y in zip(olympia_data_2019.observation_date, olympia_data_2019.total_precip_in):
    if y != 0.00:
        data_dict[datetime.strptime(x,"%Y-%m-%d").month] += 1

print('[6]  How many days in each month of 2019 did Olympia, Washington see some sort of precipitation falling?')
print('Ans: Total days in each month of year 2019 when Olympia, Washington see some sort of precipitation falling are')
for x in data_dict:
    print(f'     Total {data_dict[x]} days in month - {x}')

print('\n\n')

























