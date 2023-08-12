import requests
import os

SHEETY_ENDPOINT = ("https://api.sheety.co/02cf0db9fdbf9c243cb6bd20502be4be/"
                   "flightDeals/prices")
SHEETY_HEADERS = {
            "Authentication": f"Bearer {os.environ['SHEETY_BEARER_TOKEN']}"
        }


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        self.data = response.json()['prices']
        return self.data

    def update_city_codes(self):
        for location in self.data:
            new_data = {
                "price": {
                    "iataCode": location['iataCode']
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{location['id']}",
                                    json=new_data,
                                    headers=SHEETY_HEADERS
                                    )
            response.raise_for_status()
            print(response.text)
