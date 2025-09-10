import requests
from datetime import datetime

GENDER = "men"
WEIGHT_KG = "65"
HEIGHT_CM = "175"
AGE = "29"

NUTRIENTS_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/85ad4abf3ea8e01cc35f6d956023471f/exerciseTrack/workouts"

APP_ID = "031c709e"
APP_KEY = "aeeb2402a54a876a0b26e7c41f4be7ff"

headers = {
    "x-app-id": APP_ID,
    "X-app-key": APP_KEY
}

exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

responses = requests.post(url=NUTRIENTS_ENDPOINT, json=parameters, headers=headers)
print(responses.status_code)
result = responses.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)