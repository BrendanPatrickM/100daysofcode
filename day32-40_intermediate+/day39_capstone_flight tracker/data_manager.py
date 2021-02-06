import requests
endpoint = 'https://api.sheety.co/9b32cef2ac94d8b0c8a576aafe17f209/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.sheet_response = requests.get(url=endpoint)
        self.sheet = self.sheet_response.json()
        

    def get_data(self):
        print('get data')
        print(self.sheet)
        # return(self.sheet['prices'])

    def update_iata(self, sheet_data):
        for destination in sheet_data:
            id = str(destination['id'])
            iata = destination['iataCode']
            updated_params = {
                'price': {
                    'iataCode': iata
                }
            }
            new_url = f'{endpoint}/{id}'
            requests.put(url=new_url, json=updated_params)
