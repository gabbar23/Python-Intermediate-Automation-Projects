import requests
from twilio.rest import Client
from dotenv import dotenv_values



config = dotenv_values(".env")
auth_token = config["OWM_API"]
account_sid=config["OWM_SID"]
api_end="https://api.openweathermap.org/data/2.5/onecall"
para={
    "lat":"",#location
    "lon":74.498703,
    "exclude":"current,minutely,daily,alerts",
    "appid":config["APP_ID"]
    }



response=requests.get(url=api_end,params=para)
response.raise_for_status()
weather_data=response.json()

is_rain=False
for hour in range(0,12):
    condition=((weather_data["hourly"][hour]["weather"][0]["id"]))
    print(condition)
    if condition<=600:
        is_rain=True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hi! it is going to rain today! Bring an umbrella ☂️ ",
        from_='',
        to='+'
    )
    print(message.sid)
