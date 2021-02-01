import os
import requests
from datetime import datetime

date = (datetime.now()).strftime('%d/%m/%Y')
GENDER = 'male'
WEIGHT = 75
HEIGHT = 173
AGE = 35
APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')


nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# plain_text = input('Tell me which excercise you did?: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'x-remote-user-id': '0'
}

params = {
    'query': plain_text,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age':AGE,
}

# response = requests.post(url=nutrix_endpoint, headers=headers, json=params)
# response =response.json()
