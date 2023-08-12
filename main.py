from data_manager import DataManager
from flight_search import FlightSearch

"""
APIs Required
Google Sheet Data Management - https://sheety.co/
Kiwi Partners Flight Search API - https://partners.kiwi.com/
Tequila Flight Search API Documentation -
https://tequila.kiwi.com/portal/docs/tequila_api
Twilio SMS API - https://www.twilio.com/docs/sms

IATA Airport Codes -
https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports
https://www.nationsonline.org/oneworld/airport_code.htm
"""

# Use the Flight Search and Sheety API to populate a Google Sheet with
# International Air Transport Association (IATA) codes for each city

sheet = DataManager()
sheet_data = sheet.get_data()
# sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
flight_search = FlightSearch()

location_updated = False

for location in sheet_data:
    if not location['iataCode']:
        location['iataCode'] = flight_search.get_city_code(location['city'])
        location_updated = True
        print(sheet_data)

if location_updated:
    sheet.data = sheet_data
    sheet.update_city_codes()


# TODO Use the Flight Search API to check for the cheapest flights from
#  tomorrow to six months later for all the cities in the Google Sheet


# TODO If the price is lower than the lowest price listed in the Google Sheet,
#  then send an SMS via the Twilio API.
# The SMS should include the departure airport IATA code, destination
# airport IATA code, departure city, destination city, flight price and flight
# dates.
# E.g., Low price alert! Only $### to fly from DFW-DFW to Berlin-SXF, leaving
# 2023-08-15 and returning 2023-08-23
