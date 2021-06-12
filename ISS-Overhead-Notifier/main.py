from datetime import datetime
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

parameter={
    "lat":30.89279747750818,
    "lng":75.84960937500001,
    "formatted":0
}


response=requests.get(url="https://api.sunrise-sunset.org/json",params=PARAMETER)
response.raise_for_status()
data=response.json()

sunrise=float(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=float(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)
print(sunrise)
current_time_hour=datetime.now().hour
print(current_time_hour)



# ISS
def location():
    response_iss=requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data=response_iss.json()["iss_position"]
    iss_latt=int(data["latitude"])
    iss_lng=int(data["longitude"])
    if (iss_lng <80.84) & (iss_lng >70.84) & (iss_latt <35.84) & (iss_latt >25.84):
        return True
    else:
        return False

#time_check
def time():
    parameter = {
        "lat": 30.89279747750818,
        "lng": 75.84960937500001,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETER)
    response.raise_for_status()
    data = response.json()

    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)
    print(sunrise)
    current_time_hour = datetime.now().hour
    print(current_time_hour)

    if (current_time_hour>sunset) or (current_time_hour<sunrise):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if time() and location():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )

