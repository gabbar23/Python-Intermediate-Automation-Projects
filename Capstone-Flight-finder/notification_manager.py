from twilio.rest import Client
from dotenv import dotenv_values
config = dotenv_values(".env")

auth_token = config["AUTH"]
account_sid=config["SID"]

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self,message):
      message = self.client.messages.create(
          body=message,
          from_='',
          to='')
      print(message.sid)


