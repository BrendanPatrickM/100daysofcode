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
        query = {'term': city, 'location_types': 'city'}
        response = requests.get(url=endpoint, params=query,
                                headers=self.headers)
        reply = response.json()
        #pprint(reply)
        return reply['locations'][0]['code']

    def find_flights(self, city_code, limit_price, origin):
        endpoint = f'{TEQUILA_EP}/search'
        query = {
            'fly_from': origin,
            'fly_to': city_code,
            'date_from': self.today,
            'date_to': self.end_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            'one_for_city': 1,
            "max_stopovers": 0,
            'price_to': limit_price,
            "curr": "GBP"
        }
        response = requests.get(url=endpoint, params=query,
                                headers=self.headers)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found to {city_code}')
            return None

        city_to = data['cityTo']
        price = data['price']
        print(f"{city_to}: £{price}")
        return data['deep_link']
