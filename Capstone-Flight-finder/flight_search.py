import requests
from flight_data import FlightData
from dotenv import dotenv_values

config = dotenv_values(".env")

TEQUILA_API_SEARCH=config["TEQUILA_API_SEARCH_ENV"]
TEQUILA_ENDPOINT = config["TEQUILA_ENDPOINT_ENV"]


class FlightSearch:
    def get_destinatoin_code(self,city_name):
        header = {
            "apikey": TEQUILA_API_SEARCH
        }
        query = {
            "term": f"{city_name}",
            "location_types": "city"
        }
        response_result = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=query)
        result=response_result.json()["locations"]
        iata_code=result[0]["code"]
        return (iata_code)

    def search_flight(self,destination_city_code,origin_city,from_time, to_time):
        header={
            "apikey":TEQUILA_API_SEARCH
        }
        query={
            "fly_from":origin_city,
            "fly_to":destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        search_response=requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=header,params=query)
        try:
            data = search_response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=header,
                params=query,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                land_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                land_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data


