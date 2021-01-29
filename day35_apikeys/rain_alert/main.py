import requests
api_key = '0a97b34b3262c74cf35dd63d420c4564'
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

will_rain = False
for condition in slice_12h:
    if condition['weather'][0]['id'] < 700:
        will_rain = True
if will_rain:
    print("don't forget to bring an umbrella")

# conditions = []
# for n in range(0,12):
#     new_condition = data['hourly'][n]['weather'][0]['id']
#     conditions.append(new_condition)
# rain = [n for n in conditions if n < 701]
# if len(rain) > 0:
#     print("don't forget to bring an umbrella")
