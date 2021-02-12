
import requests
from bs4 import BeautifulSoup


url = 'https://www.empireonline.com/movies/features/best-movies-2/'


response = requests.get(url)
webpage_data = response.text
soup = BeautifulSoup(webpage_data, 'html.parser')

all_movies = soup.find_all(name='h3', class_='title')
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')

