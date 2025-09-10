from telnetlib import theNULL

import requests
import datetime
STOCK_NAME = "META"
COMPANY_NAME = "Meta Platforms"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "29MEZA2RUXRL6PCM"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "1cf8b7abd4934dd1a89a82e7bf13ce68"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "interval":"60min",
    "apikey":STOCK_API
}

response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()

time_series = data["Time Series (60min)"]

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
yesterday_prices = [(time, info) for time, info in time_series.items() if yesterday in time ]
yesterday_prices.sort()
print(yesterday_prices)
closing_price1 = yesterday_prices[-1][1]["4. close"]
print(closing_price1)
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
day_before_yesterday_prices = [(time, info) for time, info in time_series.items() if day_before_yesterday in time ]
day_before_yesterday_prices.sort()
print(day_before_yesterday)
closing_price2 = day_before_yesterday_prices[-1][1]["4. close"]
print(closing_price2)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(float(closing_price1)-float(closing_price2))
print(positive_difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (positive_difference  / float(closing_price2)) * 100
print(percentage_difference)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference >= 5:
    print("Get News")
    ## STEP 2: https://newsapi.org/
    parameters2 ={
        "apiKey": NEWS_API,
        "q": STOCK_NAME,
        "pageSize": 3
    }
    response2 = requests.get(url=NEWS_ENDPOINT,params=parameters2)
    data2 = response2.json()
    print(data2)
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
parameters2 ={
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
response2 = requests.get(url=NEWS_ENDPOINT,params=parameters2)
data2 = response2.json()["articles"]
three_articles = data[:3]
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

