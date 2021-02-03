import requests
import os
from pprint import pprint
TEQUILA_EP = 'https://tequila-api.kiwi.com'
API_KEY = os.environ.get('TEQUILA_KEY')


class FlightSearch:
    def __init__(self):
        self.headers = {"apikey": API_KEY}

    def fetch_code(self, city):
        endpoint = f'{TEQUILA_EP}/locations/query'
        # headers = {"apikey": API_KEY}
        query = {'term': city, 'location_types': 'city'}
        response = requests.get(url=endpoint, params=query, headers=self.headers)
        reply = response.json()
        return reply['locations'][0]['code']

    def find_flights(self):
        print("finding flights")
        endpoint = f'{TEQUILA_EP}/search'
        query = {
            'fly_from': 'LON',
            'fly_to': 'IE',
            'date_from': '01/04/2021',
            'date_to': '05/06/2021',
        }
        response = requests.get(url=endpoint, params=query, headers=headers)
        pprint(response.text)

