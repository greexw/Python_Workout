import requests
import datetime

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
AH_APIKEY = ""
AH_API_URL = "https://www.alphavantage.co/query?"
NA_APIKEY = ""
NA_API_URL = "https://newsapi.org/v2/everything"

ah_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AH_APIKEY,
}

# get the company stock info from alphavantage API
ah_response = requests.get(AH_API_URL, params=ah_parameters)
data = ah_response.json()['Time Series (Daily)']

yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

yesterday_close_price = float(data[str(yesterday)]['4. close'])
db_yesterday_close_price = float(data[str(day_before_yesterday)]['4. close'])

na_parameters = {
    "apiKey": NA_APIKEY,
    "q": COMPANY_NAME
}

# get the news about company from newsapi API
na_response = requests.get(NA_API_URL, params=na_parameters)  # get the news about our company
na_data = na_response.json()["articles"]

# if the close price was changed by 1% or more - print the 3 newest articles about company
if (yesterday_close_price-db_yesterday_close_price)/db_yesterday_close_price >= 0.01:
    print(f"{COMPANY_NAME} price has changed by minimum 1%! (from {db_yesterday_close_price}$ to {yesterday_close_price}$)."
          f" Here are some news about your company: \n")
    for i in range(3):
        print(na_data[i]['title'])
        print(na_data[i]['description']+"\n")
