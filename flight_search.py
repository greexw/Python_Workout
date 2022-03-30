import requests

from flight_data import FlightData

class FlightSearch:
    def __init__(self, tequila_endpoint, tequila_apikey):
        self.tequila_endpoint = tequila_endpoint
        self.tequila_apikey = tequila_apikey

    def get_iata(self, city_name):
        headers = {
            'apikey': self.tequila_apikey
        }
        params = {
            'term': city_name,
        }
        response = requests.get(url=f'{self.tequila_endpoint}/locations/query', headers=headers, params=params)
        data = response.json()['locations']
        return data[0]['code']

    def check_flights(self, origin_code, destination_code, from_time, to_time):
        headers = {
            'apikey': self.tequila_apikey
        }
        params = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN"
        }

        response = requests.get(url=f"{self.tequila_endpoint}/v2/search", headers=headers, params=params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
