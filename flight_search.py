import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.headers = {
            "apikey": os.environ['TEQUILA_API_KEY'],
            "accept": "application/json"
        }

    def get_city_code(self, city_name):
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": "true"
        }

        data = requests.get(url=self.endpoint,
                            params=params,
                            headers=self.headers
                            )
        for location in data.json()['locations']:
            if location['name'] == city_name:
                return location['code']
