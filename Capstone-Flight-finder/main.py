from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# creating objects
sheety = DataManager()
flight_search = FlightSearch()
sheety_data = sheety.retrieve_data()
notification_manager = NotificationManager()

# filling iata codes
print(sheety_data)
for i in range(len(sheety_data)):
    if sheety_data[i]["iataCode"] == "":
        sheety_data[i]["iataCode"] = flight_search.get_destinatoin_code(sheety_data[i]["city"])

sheety.destination_data = sheety_data
sheety.insert_data()

# main-search
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for city in sheety_data:
    flight = flight_search.search_flight(city["iataCode"], origin_city="LON", from_time=tomorrow,
                                         to_time=six_month_from_today)

    if flight is None:
        continue

    if flight.price < city["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from" \
                  f" {flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.land_date} " \
                  f"to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        notification_manager.send_message(message)
