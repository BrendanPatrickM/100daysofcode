from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN = 'LON'

# Create Class objects and retreive spreadsheet data
data = DataManager()
sheet_data = data.get_data()
flightsearch = FlightSearch()

# check if codes are present and update if empty
for destination in sheet_data:
    code = destination['iataCode']
    city = destination['city']

    if code == '':
        new_iata = flightsearch.fetch_code(city)
        destination['iataCode'] = new_iata
data.update_iata(sheet_data)

# search for flights
for destination in sheet_data:
    city = destination['city']
    city_code = destination['iataCode']
    price = destination['lowestPrice']
    flight = flightsearch.find_flights(city_code, price, ORIGIN)
