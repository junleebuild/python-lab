##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import smtplib
# 1. Update the birthdays.csv
my_email = "testemail12087@gmail.com"
password = "tjtk nfml ugkr kvrf"
with open("birthdays.csv", mode="r") as file:
    birth_lists = file.readlines()
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

for line in birth_lists[1:]:
    line = line.strip()
    name, email, year, month, day = line.split(",")
    if int(month) == now.month and int(day) == now.day:
        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as letter:
            letter_contents = letter.read()
            personalized_letter = letter_contents.replace("[NAME]",name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birth day {name}\n\n{personalized_letter}"
            )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




