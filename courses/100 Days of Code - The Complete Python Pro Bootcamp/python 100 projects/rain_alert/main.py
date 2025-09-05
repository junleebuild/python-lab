import requests
import json
import os
my_latitude = 36.643902
my_longitude = 127.501198
api_key = os.environ.get("API_KEY")
print(api_key)
for key, value in os.environ.items():
    print(f"{key}: {value}")
parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
print(response)
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
#
# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring an umbrella.")
# print(weather_data["hourly"][0]["weather"][0]["id"])
