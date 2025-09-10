import requests
import datetime

# API 키와 엔드포인트 설정
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_NAME = "META"
COMPANY_NAME = "Meta Platforms"
STOCK_API = "29MEZA2RUXRL6PCM"
NEWS_API = "1cf8b7abd4934dd1a89a82e7bf13ce68"

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1365635760715464724/wxeSIPRP63GVFEhaPDtYOqHCBE6yuXwlxyPHyQ3pdn8Lw_Yvb0JbC42Ekli97n-OEw8s"

# 주식 데이터 가져오기
parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API
}

response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()

time_series = data["Time Series (60min)"]

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
yesterday_prices = [(time, info) for time, info in time_series.items() if yesterday in time ]
yesterday_prices.sort()
closing_price1 = yesterday_prices[-1][1]["4. close"]

day_before_yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
day_before_yesterday_prices = [(time, info) for time, info in time_series.items() if day_before_yesterday in time ]
day_before_yesterday_prices.sort()
closing_price2 = day_before_yesterday_prices[-1][1]["4. close"]
# 퍼센트 변동 계산
positive_difference = abs(float(closing_price1)-float(closing_price2))
print(positive_difference)
percentage_difference = (positive_difference  / float(closing_price2)) * 100
print(percentage_difference)
# 퍼센트 변동 계산

# 1% 이상 변동이면 뉴스 가져오기
if percentage_difference >= 1:
    news_params = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
        "pageSize": 3,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # 뉴스 포맷팅
    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]

    # 디스코드 Webhook으로 보내기 준비
    for article in formatted_articles:
        message = f"{STOCK_NAME}: 🔺{round(percentage_difference, 2)}%\n{article}"
        # 여기에 디스코드 Webhook 보내는 코드 추가할 거야
        payload = {
            "content": message
        }
        discord_response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        discord_response.raise_for_status()