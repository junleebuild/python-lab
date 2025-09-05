import requests
from datetime import datetime
import smtplib
import time
my_email = "testemail12087@gmail.com"
password = "tjtk nfml ugkr kvrf"
MY_LAT = 36.643902 # Your latitude
MY_LONG = 127.501198 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunset_kst = (sunset + 9) % 24
sunrise_kst = (sunrise + 9) % 24

def iss_over_myhead_atnight():
    time_now = datetime.now()
    is_close = (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and \
               (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5)
    is_night = (time_now.hour >= sunset_kst or time_now.hour <= sunrise_kst)

    if is_close and is_night:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS is over your head\n\nLook at up."
            )
        print("보냈어")
    else:
        print("아직 밤에 뜨지 않았어.")
while True:
    iss_over_myhead_atnight()
    time.sleep(60)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



