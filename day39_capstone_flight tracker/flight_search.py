from datetime import datetime, timedelta
import requests
import os
from pprint import pprint
TEQUILA_EP = 'https://tequila-api.kiwi.com'
API_KEY = os.environ.get('TEQUILA_KEY')


class FlightSearch:
    def __init__(self):
        self.headers = {"apikey": API_KEY}
        self.today = datetime.now().strftime('%d/%m/%Y')
        self.end_date = (datetime.now() + timedelta(183)).strftime('%d/%m/%Y')

    def fetch_code(self, city):
        endpoint = f'{TEQUILA_EP}/locations/query'
        # headers = {"apikey": API_KEY}
        query = {'term': city, 'location_types': 'city'}
        response = requests.get(url=endpoint, params=query, headers=self.headers)
        reply = response.json()
        return reply['locations'][0]['code']

    def find_flights(self, city_code, limit_price):
        endpoint = f'{TEQUILA_EP}/search'
        query = {
            'fly_from': 'LON',
            'fly_to': city_code,
            'date_from': self.today,
            'date_to': self.end_date,
            'one_for_city': 1,
            'one_for_day': 1,
            'price_to': limit_price
        }
        response = requests.get(url=endpoint, params=query, headers=self.headers)
        
        try :
            data = response.json()['data'][0]
        except IndexError:
            print('No flights found')
            return None
        
        return (data['price'])
        
