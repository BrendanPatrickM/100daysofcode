import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = ""          # Stock token eg: TSLA
COMPANY_NAME = ""   # eg: Tesla inc
AV_KEY = ''
NEWS_KEY = ''
TWILIO_KEY = ''
TWILIO_SID = ''
TWILIO_NUMBER = ''
MY_NUM = ''


def days_ago(days):
    date = datetime.now() - timedelta(days)
    date_string = date.strftime('%Y-%m-%d')
    return date_string


def percentage_change(current, previous):
    if previous != 0:
        return float(current - previous) / abs(previous) * 100
    else:
        return "undefined"


def format_text(num):
    headline = articles[num]['title']
    brief = articles[num]['description']
    if change > 0:
        emoji = '🔺'
    else:
        emoji = '🔻'
    body_string = (f'{STOCK}:{emoji}{round(change)}%\n'
                   f'Headline: {headline}\nBrief: {brief}')
    return body_string


stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': AV_KEY,
}

response = requests.get('https://www.alphavantage.co/query?',
                        params=stock_parameters)
data = response.json()
d1_price = float(data['Time Series (Daily)'][days_ago(1)]['5. adjusted close'])
d2_price = float(data['Time Series (Daily)'][days_ago(2)]['5. adjusted close'])
change = percentage_change(d1_price, d2_price)


if abs(change) > 5:
    news_parameters = {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWS_KEY,
    }

    news_response = requests.get('https://newsapi.org/v2/everything',
                                 params=news_parameters)
    articles = news_response.json()['articles'][0:3]

    for num in range(0, 3):
        body = format_text(num)
        client = Client(TWILIO_SID, TWILIO_KEY)
        message = client.messages \
                        .create(
                            body=body,
                            from_=TWILIO_NUMBER,
                            to=MY_NUM
                        )
        print(message.status)
