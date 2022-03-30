import requests


class DataManager:
    def __init__(self, sheety_enpoint):
        self.sheety_endpoint = sheety_enpoint

    def get_datasheet(self):
        sheet_data = requests.get(url=self.sheety_endpoint)
        return sheet_data.json()['prices']

    def update_datasheet(self, sheet_data):
        for row in sheet_data:
            id = row['id']
            data = {
                'price': {
                    'iataCode': row['iataCode'],
                }
            }
            requests.put(url=f'{self.sheety_endpoint}/{id}', json=data)