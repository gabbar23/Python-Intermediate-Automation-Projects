import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

difference: float
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "https://www.alphavantage.co/query?"
para_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": config["PARA_APIKEY"]
}
news_api = "https://newsapi.org/v2/everything"
news_para = {
    "apikey": config["NEWS_APIKEY"],
    "q": COMPANY_NAME,
}
account_sid = config["ACC_SID"]
auth_token = config["ACC_TOKEN"]



# Stock information
def stock_price():
    global difference
    stock = requests.get(url=STOCK_API, params=para_stock)

    stock.raise_for_status()
    today = (date.today())
    yesterday = (today - timedelta(days=1))
    test = str(today - timedelta(days=2))
    data_2 = stock.json()
    data=data_2["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    today_close = data_list[0]["4. close"]
    yesterday_close = data_list[1]["4. close"]
    difference = abs(float(today_close) - float(yesterday_close))
    price_change = round(abs(((float(today_close) - float(yesterday_close)) / float(yesterday_close)) * 100), 2)
    return (price_change)


stock_info=stock_price()

# Main-Program
if stock_info >= .1:
    client = Client(account_sid, auth_token)
    news = requests.get(url=news_api, params=news_para)
    title = news.json()["articles"][:3][1]["title"]
    des = news.json()["articles"][:3][1]["description"]
    if difference >=0:
        message = client.messages \
            .create(
            body=f"TESLA: 🔺{abs(stock_info)}\nHeadline : {title} \nBrief : {des}",
            from_='+17342594666',
            to='+918837679689'
        )
        print(f"TESLA: 🔺{abs(stock_info)}\n Headline : {title} \nBrief : {des}")
    elif difference <=0:
        message = client.messages \
            .create(
            body=f"TESLA: 🔻{abs(stock_info)}\nHeadline : {title} \nBrief : {des}",
            from_='+17342594666',
            to='+918837679689'
        )
        print(f"TESLA: 🔻{abs(stock_info)}\n {title} \n {des}")

    print(message.status)
