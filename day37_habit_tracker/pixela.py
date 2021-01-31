from datetime import datetime
import requests


class Pixela:
    def __init__(self, username, token):
        self.USERNAME = username
        self.TOKEN = token
        self.date = (datetime.now()).strftime('%Y%m%d')
        self.headers = {
            'X-USER-TOKEN': self.TOKEN,
            }

    def add_pixel(self, quantity):
        print(f'quantity = {quantity}')
        self.endpoint = 'https://pixe.la/v1/users/brendan/graphs/graph1'
        self.params = {
            'date': self.date,
            'quantity': quantity,
            }
        response = requests.post(url=self.endpoint, json=self.params,
                                 headers=self.headers)
        print(response.text)