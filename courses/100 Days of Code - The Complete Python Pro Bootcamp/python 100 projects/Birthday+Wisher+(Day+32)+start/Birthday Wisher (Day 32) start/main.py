import datetime as dt
import smtplib
import random
my_email = "testemail12087@gmail.com"
password = "tjtk nfml ugkr kvrf"

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()
quote = random.choice([q.strip() for q in quotes])

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Today's quote\n\n{quote}")
# import smtplib
#
# my_email = "testemail12087@gmail.com"
# password = "tjtk nfml ugkr kvrf"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email,
#                         msg="Subject:Hello\n\nThis is the body of my email.")
#     connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# day_of_birth = dt.datetime(year= 1995, month=12, day=15, hour=4)
# print(day_of_birth)