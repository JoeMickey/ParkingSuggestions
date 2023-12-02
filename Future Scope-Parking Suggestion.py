import pandas as pd
import numpy as np
from collections import defaultdict
from geopy.geocoders import Nominatim
from sklearn.preprocessing import OneHotEncoder
from geopy.distance import geodesic
import xgboost as xgb
from sklearn.model_selection import train_test_split
import pickle


# import datasets
df = pd.read_csv('database.csv')
population = pd.read_csv("./DataSource/population_cities_2010_2022.csv", index_col = "City")
parking_lots = pd.read_csv("./DataSource/park_lots_loc_datasd.csv")
parking_meters = pd.read_csv("./DataSource/parking_meters_loc_datasd.csv")

# population data integrate
sd_cities = ["San Diego city","Chula Vista city","Oceanside city","Escondido city","Carlsbad city","El Cajon city","Vista city","San Marcos city","Encinitas city","National City city"]
# filter non-sd data
for index, row in population.iterrows():
    if index not in sd_cities: population = population.drop(index)
# align the name format
for i in range(2010,2023):
    population[str(i)] = population[str(i)].str.replace(',', '').astype(float)
assert len(population) == len(sd_cities), 'Missing City Population'
# get the whole SD's population
population_whole_sd = [[sum(j for j in population[str(i)])] for i in range(2010,2023)]
assert len(population_whole_sd) == 13, 'Population Incomplete'

# get the past two years' data
df['date_issue'] = pd.to_datetime(df['date_issue'], format = '%Y-%m-%d')
condition = df['date_issue'].dt.year >= 2022
df_2022_2023 = df[condition]

# find the location with over 50 tickets
locations_set_2022_2023 = set(df_2022_2023['location'])
locations_count_2022_2023 = defaultdict(int)
for index, row in df_2022_2023.iterrows():
    locations_count_2022_2023[row['location']] += 1
locations_count_over_50_2022_2023 = defaultdict(int)
for key, value in locations_count_2022_2023.items():
    if value >= 50:
        locations_count_over_50_2022_2023[key] = value

# get location details
def get_address_details_geopy(address):
    '''
    :param address: str of address
    :return: the lat, lng and postcode of the address
    '''
    assert isinstance(address, str), 'Invalid Input for address'

    address = str(address) + ", San Diego, CA"
    location = geolocator.geocode(address)
    if location:
        reverse_location = geolocator.reverse((location.latitude, location.longitude), language="en")
        if reverse_location:
            return (location.latitude,location.longitude,reverse_location.raw.get('address', {}).get('postcode'))
    else:
        print(address, "Location not found.")

geolocator = Nominatim(user_agent="my_geocoder",timeout=10)
address_components = defaultdict(list)
for d in set(locations_count_over_50_2022_2023.keys()):
    address_detail = get_address_details_geopy(d)
    address_components[d].append(address_detail)

locations_count_over_50_2022_2023_located = defaultdict(int)
for key, value in locations_count_over_50_2022_2023.items():
    if key in address_components and address_components[key][0] and len(address_components[key][0]) == 3:
        locations_count_over_50_2022_2023_located[key] = address_components[key][0]

# filter the location that can't be located
condition = df_2022_2023['location'].isin(locations_count_over_50_2022_2023_located)
df_2022_2023_located = df_2022_2023[condition]
df_2022_2023_located[['lat', 'lng','postcode']] = df_2022_2023_located['location'].apply(lambda x: pd.Series(locations_count_over_50_2022_2023_located.get(x, [None, None, None])))

# get one-hot encoding model
months, days, weekdays, postcodes = [], [], [], []
def get_ohe_date(date):
    '''
    :param date: string of date
    :return: amend the list of the required samples for one hot encoding model
    '''
    assert isinstance(date, str), 'Invalid Date'

    date = pd.to_datetime(date, format = '%Y-%m-%d')
    months.append([date.month])
    days.append([date.day])
    weekdays.append([date.weekday()])

df_2022_2023_located['date_issue'].apply(get_ohe_date)


#one hot encoding model fit
months_enc = OneHotEncoder(drop='first')
months_enc.fit(months)

days_enc = OneHotEncoder(drop='first')
days_enc.fit(days)

weekdays_enc = OneHotEncoder(drop='first')
weekdays_enc.fit(weekdays)

# if someday is holiday
us_holidays = {
    'New Years Day': '2023-01-01',
    'Martin Luther King Jr. Day': '2023-01-16',
    'Presidents Day': '2023-02-20',
    'Memorial Day': '2023-05-29',
    'Independence Day': '2023-07-04',
    'Labor Day': '2023-09-04',
    'Thanksgiving Day': '2023-11-23',
    'Christmas Day': '2023-12-25',
    'New Years Day2': '2022-01-01',
    'Martin Luther King Jr. Day2': '2022-01-16',
    'Presidents Day2': '2022-02-20',
    'Memorial Day2': '2022-05-29',
    'Independence Day2': '2022-07-04',
    'Labor Day2': '2022-09-04',
    'Thanksgiving Day2': '2022-11-23',
    'Christmas Day2': '2022-12-25',
}
holidays = list(us_holidays.values())

#if holiday
def if_holiday(date):
    '''
    :param date: string of a date
    :return: if the date is a holiday
    '''
    assert isinstance(date, str), 'Invalid Date'

    if str(date)[:10] in holidays:
        return 1
    else:
        return 0

df_2022_2023_located['holiday'] = df_2022_2023_located['date_issue'].apply(if_holiday)


#if near an interest
interests = {
    'balboa park' : (32.733742, -117.145545),
    'san diego zoo' : (32.735986, -117.150995),
    'old town' : (32.754029, -117.196988),
    'seaport village' : (32.708990, -117.171087),
    'seaworld sandiego' : (32.764251, -117.226386),
    'museum of contemporary art' : (32.844553, -117.278324),
    'la jolla cove' : (32.850550, -117.273070),
    'blacks beach' : (32.880351, -117.251877),
    'mission beach' : (32.769585, -117.253014)
}
interests_ll = list(interests.values())

#if near interests
def get_nearby_points_of_interest(row):
    '''
    :param row: row of df
    :return: if the location is near an interest
    '''
    assert len(row) != 0, 'Invalid Row'

    distances = np.sqrt(np.sum((interests_ll - np.array([row['lat'],row['lng']]))**2, axis=1))
    closest_point = interests_ll[np.argmin(distances)]
    if geodesic((row['lat'],row['lng']), closest_point).meters <= 1500:
            return 1
    return 0

df_2022_2023_located['interest'] = df_2022_2023_located.apply(get_nearby_points_of_interest, axis = 1)

# organzie all the meters' location
meters_location = []
def get_meters_location(row):
    meters_location.append((row['lat'],row['lng']))

parking_meters.apply(get_meters_location, axis = 1)
meters_location = np.array(list(set(meters_location)))

#if near parking places
def get_nearby_parking(row):
    '''
    :param row: row of df
    :return: if the location is near a parking meter
    '''
    assert len(row) != 0, 'Invalid Row'

    distances = np.sqrt(np.sum((meters_location - np.array([row['lat'],row['lng']]))**2, axis=1))
    closest_point = meters_location[np.argmin(distances)]
    if geodesic(closest_point, (row['lat'],row['lng'])).meters < 500:
        return 1
    else:
        return 0

df_2022_2023_located['parking'] = df_2022_2023_located.apply(get_nearby_parking, axis = 1)


# negative sample for test
df_2022_2023_located['sample_type'] = 1
def negative_sampling(row):
    '''
    :param row: row of df
    :return: if the location is near a parking meter
    '''
    assert len(row) != 0, 'Invalid Row'

    negative_columns = ['date_issue', 'location']
    other_rows = df_2022_2023_located[df_2022_2023_located.index != row.name]
    negative_sample = other_rows.sample(n=1)[negative_columns].values.flatten()

    new_row1 = row.copy()
    new_row1['date_issue'] = negative_sample[0]
    new_row1['holiday'] = 1 if new_row1['date_issue'] in holidays else 0
    new_row1['sample_type'] = 0

    df_2022_2023_located.loc[int(df_2022_2023_located.iloc[-1].name) + 1] = new_row1

    new_row2 = row.copy()
    new_row2['location'] = negative_sample[1]
    new_row2['lat'] = locations_count_over_50_2022_2023_located[new_row2['location']][0]
    new_row2['lng'] = locations_count_over_50_2022_2023_located[new_row2['location']][1]
    new_row2['postcode'] = locations_count_over_50_2022_2023_located[new_row2['location']][2]
    new_row2['interest'] = get_nearby_points_of_interest(new_row2)
    new_row2['parking'] = get_nearby_parking(new_row2)
    new_row2['sample_type'] = 0

    df_2022_2023_located.loc[int(df_2022_2023_located.iloc[-1].name) + 1] = new_row2


df_2022_2023_located.apply(negative_sampling, axis=1)

#postcode ohe
df_2022_2023_located_drop_none = df_2022_2023_located.dropna(subset=['postcode'])
postcodes = np.array(df_2022_2023_located_drop_none['postcode'].tolist()).reshape(-1,1)
postcodes_enc = OneHotEncoder(drop='first')
postcodes_enc.fit(postcodes)

# build features
x, y = [], []
def feature(row):
    '''
    :param row: row of df
    :return: amend the variables
    '''
    assert len(row) != 0, 'Invalid Row'

    if len(str(row['postcode'])) != 5:
        pass
    date = pd.to_datetime(row['date_issue'], format = '%Y-%m-%d')
    x_sum = months_enc.transform([[date.month]]).toarray().tolist()[0] + days_enc.transform([[date.day]]).toarray().tolist()[0] + weekdays_enc.transform([[date.weekday()]]).toarray().tolist()[0]+ [row['holiday']] + postcodes_enc.transform([[row['postcode']]]).toarray().tolist()[0] + [row['lat']] + [row['lng']] + [row['interest']] + [row['parking']]
    x.append(x_sum)
    y.append(row['sample_type'])

df_2022_2023_located_drop_none.apply(feature, axis = 1)


def accuracy(y, y_pred):
    '''
    :param y: original result
    :param y_pred: predicting result
    :return: the accuracy of the predict
    '''
    count = 0
    for i in range(len(y)):
        if y[i] == y_pred[i]:
            count += 1
    return count / len(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
mod = xgb.XGBClassifier(objective="binary:logistic", eval_metric="logloss", use_label_encoder=False, max_depth=20)
mod.fit(x_train, y_train)

with open('model.pkl', 'wb') as file:
    pickle.dump(mod, file)