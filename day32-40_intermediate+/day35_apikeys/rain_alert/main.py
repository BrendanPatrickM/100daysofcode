import requests
import os
from twilio.rest import Client
api_key = os.environ.get('OWM_API_KEY')
account_sid = 'ACa79b1277a779b09d55d4abfaf912b7ba'
auth_token = os.environ.get('AUTH_TOKEN')
lat = 52.844349
lon = -8.983000

parameters = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall',
                        params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
slice_12h = data['hourly'][:12]
print(slice_12h)

will_rain = False
for condition in slice_12h:
    if condition['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain ☔️",
                        from_='+14078907419',
                        to='+447453584873'
                    )

    print(message.status)


# conditions = []
# for n in range(0,12):
#     new_condition = data['hourly'][n]['weather'][0]['id']
#     conditions.append(new_condition)
# rain = [n for n in conditions if n < 701]
# if len(rain) > 0:
#     print("don't forget to bring an umbrella")
