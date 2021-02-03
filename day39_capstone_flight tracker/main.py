from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# Create Class objects and retreive spreadsheet data
# data = DataManager()
# sheet_data = data.get_data()
flightsearch = FlightSearch()
# pprint(sheet_data)

# check if codes are present and update if empty
# for destination in sheet_data:
#     code = destination['iataCode']
#     city = destination['city']

#     if code == '':
#         new_iata = flightsearch.fetch_code(city)
#         destination['iataCode'] = new_iata
# data.update_iata(sheet_data)

# search for flights


sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
 {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 1}]


for destination in sheet_data:
    city = destination['city']
    city_code = destination['iataCode']
    price = destination['lowestPrice']
    result = flightsearch.find_flights(city_code, price)
    print(f'{city}: €{result}')
