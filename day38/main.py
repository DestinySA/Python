from datetime import datetime
import requests

APP_ID = "CHANGE APP ID"
API_KEY = "CHANGE KEY"
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 167
AGE = 32

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_data, headers=nutritionix_headers)


sheety_endpoint = "https://api.sheety.co/614a75b25d12ed2eef459c93d66fe97a/workout/notes"


sheety_headers = {
    "Authorization" : "Bearer Eclipse117."
}

exercises = response.json()["exercises"]
for exercise in exercises:
    note = {
        "note": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=note, headers=sheety_headers)
    print(response.text)
