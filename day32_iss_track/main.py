import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.844349
MY_LONG = -8.983000
MY_EMAIL = 'brendanpython@gmail.com'
MY_PASSWORD = 'Python1977!!'


def check_iss_close():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    #iss_lon = float(data['iss_position']['longitude'])
    #iss_lat = float(data['iss_position']['latitude'])
    iss_lon = MY_LONG
    iss_lat = MY_LAT

    if (iss_lon < MY_LONG-5 or iss_lon > MY_LONG+5) or (iss_lat < MY_LAT-5 or iss_lon > MY_LAT+5):
        return False
    else:
        return True


def is_dark():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,

    }
    response = requests.get(url='https://api.sunrise-sunset.org/json',
                            params=parameters)
    response.raise_for_status()
    sun_data = response.json()

    sunrise = sun_data['results']['sunrise']
    sunrise_h = int(sunrise.split('T')[1].split(':')[0])
    sunset = sun_data['results']['sunset']
    sunset_h = int(sunset.split('T')[1].split(':')[0])
    time_now = datetime.now()

    time = time_now.hour
    if time < sunrise_h or time > sunset_h:
        return True
    else:
        return False


while True:
    if check_iss_close() and not is_dark():
        print('LOOK FOR ISS')
        connection = smtplib.SMTP('smtp@gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you"

        )
    else:
        print('not yet')
    time.sleep(60)

# send me an email
