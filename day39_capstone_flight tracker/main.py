from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheet_data = data.get_data()
flightsearch = FlightSearch()

for destination in sheet_data:
    code = destination['iataCode']
    city = destination['city']

    if code == '':
        new_iata = flightsearch.fetch_code(city)
        destination['iataCode'] = new_iata

data.update_iata(sheet_data)
