import requests
from datetime import datetime

APP_ID = "ba609d68"
API_KEY = "378407d00348b57d88df3ec0792a5d2f"
TOKEN = "Basic a2hhbGl0MjM6VG91Y2htYXRlNyE="

user_exercise = input("What exercise did you complete?: ")

info = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = {
    "query": user_exercise,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 180,
    "age": 24
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, json=query, headers=info)
result_from_exercise = response.json()
exercise = result_from_exercise["exercises"][0]["name"]
calories = result_from_exercise["exercises"][0]["nf_calories"]
duration = result_from_exercise["exercises"][0]["duration_min"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_url = "https://api.sheety.co/b220701b63ba974ab02882a560c5e484/workoutTracking/sheet1"

access_info = {
    "Authorization": TOKEN
}

info_to_add = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": f"{duration} minutes",
            "calories": calories
        }
    }
sheet_response = requests.post(url=sheety_url, json=info_to_add, headers=access_info)

print(sheet_response.text)
