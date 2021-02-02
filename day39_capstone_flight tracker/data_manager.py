import requests


class DataManager:
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/9b32cef2ac94d8b0c8a576aafe17f209/flightDeals/prices'
        self.sheet_response = requests.get(url=self.endpoint)
        self.sheet = self.sheet_response.json()

    def get_data(self):
        return(self.sheet['prices'])
