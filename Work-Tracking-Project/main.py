import requests
from datetime import datetime
from dotenv import dotenv_values


config = dotenv_values(".env")

APP_ID_NUTRI=config["MY_APP_ID_NUTRI"]
API_NUTRI=config["MY_API_NUTRI"]

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint=config["MY_SHEETY_ENDPOINT"]

GENDER=""
AGE=""
WEIGHT=""
HEIGHT_CM =""

#Tracker

headers={
    "x-app-id":APP_ID_NUTRI,
    "x-app-key":API_NUTRI,
}

exercise_query=input("What did you do today?")
para={
     "query":exercise_query,
     "gender":GENDER,
     "weight_kg":WEIGHT,
     "height_cm":HEIGHT_CM,
     "age":AGE
}

response_exercise=requests.post(url=exercise_endpoint,json=para,headers=headers)
exercise_data=response_exercise.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


# #Sheety

SHEETY_BASIC_AUTH=config["MY_SHEETY_BASIC_AUTH"]

for exercise in exercise_data["exercises"]:
    sheets_input={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise['nf_calories']
        }
    }
    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BASIC_AUTH}"
    }
    sheets_response=requests.post(url=sheety_endpoint,json=sheets_input,headers=bearer_headers)

    print(sheets_response.text)