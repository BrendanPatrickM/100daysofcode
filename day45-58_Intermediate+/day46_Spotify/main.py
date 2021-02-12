from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"
# date = input('please enter a date YYYY-MM-DD: ')
date = "2021-02-06"

response = requests.get(f'{BASE_URL}{date}')
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

all_songs = soup.find_all(
    name='span',
    class_='chart-element__information__song text--truncate color--primary'
)
all_titles = [song.getText()for song in all_songs]
print(all_titles)
