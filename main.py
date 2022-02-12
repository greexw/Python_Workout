import smtplib
import datetime as dt
import pandas
import random

current_date = dt.datetime.now()
current_day = current_date.day
current_month = current_date.month

letters = []
for i in range(1, 4):
    with open(f"letter_templates/letter_{i}.txt") as file:
        letters.append(file.read())


def send_wishes(name, email):
    wishes = random.choice(letters).replace("[NAME]", name)

    password = "TEST321test"
    my_email = "test123test4568@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{wishes}")


data = pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if current_day == row["day"] and current_month == row["month"]:
        send_wishes(row["name"], row["email"])
