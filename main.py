from data_manager import DataManager
from flight_search import FlightSearch

from datetime import datetime, timedelta

# endpoint and Apikeys for Tequila&Sheety API's
SHEETY_ENDPOINT = ""
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
TEQUILA_APIKEY = ''

# IATA code for origin airport/city
ORIGIN_IATA = 'WRO'

flight_search = FlightSearch(TEQUILA_ENDPOINT, TEQUILA_APIKEY)
data_manager = DataManager(SHEETY_ENDPOINT)

# get the datasheet with destinations and low prices
sheet_data = data_manager.get_datasheet()

# get IATA code for city if not exists
for sheet in sheet_data:
    if sheet['iataCode'] == '':
        sheet['iataCode'] = flight_search.get_iata(sheet['city'])

# update datasheets with IATA codes
data_manager.update_datasheet(sheet_data)

# get tomorrow and year from today dates
tomorrow = datetime.now() + timedelta(days=1)
year_from_today = datetime.now() + timedelta(days=(12 * 30))

# check the flights to all destinations - from today to day year of today. If price of the flight is lower than price
# in sheet - print about founded low price fly
for sheet in sheet_data:
    flight = flight_search.check_flights(ORIGIN_IATA, sheet["iataCode"], tomorrow, year_from_today)
    if flight:
        if flight.price < sheet['lowestPrice']:
            print(f'Low price! From {flight.origin_city} to {flight.destination_city}.\nPrice: {flight.price}\n'
                  f'fly date: {flight.out_date}\nreturn date: {flight.return_date}')
