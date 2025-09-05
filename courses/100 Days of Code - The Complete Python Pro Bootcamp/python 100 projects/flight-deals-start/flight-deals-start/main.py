import requests
from datetime import datetime, timedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
SHEETY_ENDPOINT = "https://api.sheety.co/85ad4abf3ea8e01cc35f6d956023471f/flightDeals/prices"
AMADEUS_API_KEY = "zXMN6XD5tooWIO9OIwUAQ3UfWVVMpVql"
AMADEUS_API_Secret = "sBCYrsQHGVDefp8m"
AMADEUS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_LOCATION_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_OFFER_URL = "https://test.api.amadeus.com/v1/shopping/flight-offers"

def get_amadeus_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_Secret
    }
    response = requests.post(AMADEUS_TOKEN_URL, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def get_iata_code(city_name, token):
    params = {
        "keyword": city_name,
        "include": "AIRPORTS",
        "max": "2"
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(AMADEUS_LOCATION_URL, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()
    try:
        return results["data"][0]["iataCode"]
    except (KeyError, IndexError):
        print(f"IATA code not found for {city_name}")
        return None

def update_sheet(row_id, iata_code):
    update_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
    body = {
        "price": {
            "iataCode": iata_code
        }
    }
    response = requests.put(update_endpoint, json=body)
    response.raise_for_status()
    print(f"Updated row {row_id} with IATA code {iata_code}")

def generate_dates(months=6):
    today = datetime.today()
    dates = []
    for week in range(months * 4):
        date = today + timedelta(days=7*week)
        dates.append(date.strftime("%Y-%m-%d"))
    return dates

def find_cheapest_price(destination_code, token):
    dates = generate_dates()
    cheapest_price = float('inf')

    for date in dates:
        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": destination_code,
            "departureDate": date,
            "adults": 1,
            "currencyCode": "USD",
            "max": 1
        }
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(AMADEUS_FLIGHT_OFFER_URL, headers=headers, params=params)
        print(f"🔎 Checking {date} from ICN to {destination_code}: {response.status_code}")
        if response.status_code != 200:
            print(f"❌ Error response: {response.text}")  # 추가!!
            continue  # 바로 다음 날짜로 넘어감

        if response.status_code == 200:
            try:
                data = response.json()["data"][0]
                price = float(data["price"]["grandTotal"])
                if price < cheapest_price:
                    cheapest_price = price
            except (KeyError, IndexError):
                continue
        if cheapest_price == float('inf'):
            return None
        else:
            return  int(cheapest_price)
def main():
    sheet_response = requests.get(url=SHEETY_ENDPOINT)
    sheet_response.raise_for_status()
    sheet_data = sheet_response.json()["prices"]

    token = get_amadeus_token()

    for city in sheet_data:
        if city.get("iataCode","") == "":
            iata_code = get_iata_code(city["city"], token)
            if iata_code:
                update_sheet(city["id"], iata_code)

    for city in sheet_data:
        destination_code = city.get("iataCode")
        if destination_code:  # iataCode가 있다면
            cheapest_price = find_cheapest_price(destination_code, token)
            if cheapest_price is not None:
                current_price = city.get("lowestPrice")
                # current_price가 None이면 inf로 바꿔서 비교
                current_price = float(current_price) if current_price else float('inf')

                if cheapest_price < current_price:
                        update_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
                        body = {
                            "price": {
                                "lowestPrice": cheapest_price
                            }
                        }
                        response = requests.put(update_endpoint, json=body)
                        response.raise_for_status()
                        print(f"Updated {city['city']} with lower price {cheapest_price}")
                else:
                        print(f"No update needed for {city['city']}: current {current_price} vs found {cheapest_price}")
if __name__ == "__main__":
    main()