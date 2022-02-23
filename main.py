import requests
from twilio.rest import Client

API_KEY = ""
OWM_Endpoint = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""

weather_params = {
    "lat": 51.50,
    "lon": -0.5,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
       .create(
       body="It's goint to rain today! Bring umbrella with you.",
       from_='',
       to=''
    )
    print(message.status)






























