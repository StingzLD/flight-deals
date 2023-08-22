from datetime import datetime, timedelta
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

ORIGIN_CITY_IATA = "DFW"

sheet = DataManager()
sheet_data = sheet.get_data()
flight_search = FlightSearch()


# Use the Flight Search and Sheety API to populate a Google Sheet with
# International Air Transport Association (IATA) codes for each city

location_updated = False

for location in sheet_data:
    if not location['iataCode']:
        location['iataCode'] = flight_search.get_city_code(location['city'])
        location_updated = True
        print(sheet_data)

if location_updated:
    sheet.data = sheet_data
    sheet.update_city_codes()


#  Use the Flight Search API to check for the cheapest flights from tomorrow
#  to six months later for all the cities in the Google Sheet

date_tomorrow = datetime.now() + timedelta(days=1)
date_in_six_months = datetime.now() + timedelta(days=(6 * 30))

for location in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=location['iataCode'],
        depart_date=date_tomorrow.strftime("%d/%m/%Y"),
        return_date=date_in_six_months.strftime("%d/%m/%Y")
    )


# TODO If the price is lower than the lowest price listed in the Google Sheet,
#  then send an SMS via the Twilio API.
# The SMS should include the departure airport IATA code, destination
# airport IATA code, departure city, destination city, flight price and flight
# dates.
# E.g., Low price alert! Only $### to fly from DFW-DFW to Berlin-SXF, leaving
# 2023-08-15 and returning 2023-08-23
