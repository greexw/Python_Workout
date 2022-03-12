import requests
from datetime import datetime

NUTRITIONIX_APPID = ""
NUTRITIONIX_KEY = ""
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/e0b61997ecfdcd3b24fffe8a1a3c37ef/myWorkouts/workouts"
SHEETY_KEY = ""

headers = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_KEY,
}

query = input("Tell me about your exercises: ")

params = {
    "query": query
}
# Get response about exercises details (duration, calories) from NUTRITRIONIX API
response_google = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers).json()

# add exercises to google_sheets by Sheety API
headers_gsheet = {
    "authorization": SHEETY_KEY
}

for exercise in response_google['exercises']:
    params = {
        'workout': {
            "date": datetime.today().strftime('%d/%m/%Y'),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"]),
        }
    }
    requests.post(url=SHEETY_ENDPOINT, json=params, headers=headers_gsheet)
