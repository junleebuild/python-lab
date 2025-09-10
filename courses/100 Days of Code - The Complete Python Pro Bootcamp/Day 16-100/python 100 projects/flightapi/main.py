import requests

API_KEY ="68100d4841bb52da5be29087"

response = requests.get("https://api.flightapi.io/onewaytrip/68100d4841bb52da5be29087/ICN/YOW/2025-05-01/1/0/0/Economy/KRW" )
print(response.json())