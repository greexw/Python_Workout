import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.126454
MY_LONG = -28.41


def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    if (MY_LONG + 5 > iss_longitude > MY_LONG - 5) and (MY_LAT + 5 > iss_latitude > MY_LAT - 5):
        return True
    else:
        return False


def check_is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if datetime.now().hour < sunrise or datetime.now().hour > sunset:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_is_night() and check_position():
        password = "TEST321test"
        my_email = "test123test4568@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=f"Subject:ISS is close to you!\n\n "
                                    f"Hi! Look out the windows! ISS is close to you!")
    else:
        print("ISS is far far away")
