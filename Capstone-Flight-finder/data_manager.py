import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
SHEETY_ENDPOINT=config["SHEETY_ENDPOINT_ENV"]

class DataManager:
    def __init__(self):
        self.destination_data={}

    def retrieve_data(self):
        response_get=requests.get(url=SHEETY_ENDPOINT)
        data=response_get.json()
        self.destination_data=data["prices"]
        return self.destination_data

    def insert_data(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response_put=requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data)

