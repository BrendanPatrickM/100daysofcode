from datetime import datetime, timedelta
import requests
import os
from pprint import pprint
TEQUILA_EP = 'https://tequila-api.kiwi.com'
API_KEY = os.environ.get('TEQUILA_KEY')

headers = {"apikey": API_KEY}
today = datetime.now().strftime('%d/%m/%Y')
end_date = (datetime.now() + timedelta(183)).strftime('%d/%m/%Y')

endpoint = f'{TEQUILA_EP}/search'
query = {
    'fly_from': 'LON',
    'fly_to': 'NYC',
    'date_from': today,
    'date_to': end_date,
    'one_for_city': 1,
    'one_for_day': 1,
    'price_to': 240
}
response = requests.get(url=endpoint, params=query, headers=headers)
try:
    data = response.json()['data'][0]
except IndexError:
    print('No flights found')
    return None

    
return (data[0]['price'])
