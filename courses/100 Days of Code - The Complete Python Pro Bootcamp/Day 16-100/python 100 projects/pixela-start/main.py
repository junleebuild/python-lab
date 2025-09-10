import datetime
import requests
from requests import delete

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jun123412"
TOKEN = "hjalerdifd123h12"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }
today = datetime.datetime.now()
TODAY = today.strftime("%Y%m%d")
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
pixel_config = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today? "),
}

update_config = {
    "quantity": "12"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# responses = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(responses.text)
# responses = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(responses.text)
# responses = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(responses)

responses = requests.delete(url=delete_endpoint, headers=headers)
print(responses.text)