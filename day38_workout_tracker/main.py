import os
import requests
from datetime import datetime

GENDER = 'male'
WEIGHT = 75
HEIGHT = 173
AGE = 35
APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheetly_endpoint = 'https://api.sheety.co/9b32cef2ac94d8b0c8a576aafe17f209/workoutTracker/workouts'
plain_text = input('Tell me which excercise you did?: ')

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
    'age': AGE,
}

response = requests.post(url=nutrix_endpoint, headers=headers, json=params)
response = response.json()

for exercise in response['exercises']:
    sheet_params = {
        "workout": {
            "date": (datetime.now()).strftime('%d/%m/%Y'),
            'time': datetime.now().strftime("%X"),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    sheet_response = requests.post(url=sheetly_endpoint, json=sheet_params)
    sheet_response = sheet_response.json()
    print (sheet_response)
