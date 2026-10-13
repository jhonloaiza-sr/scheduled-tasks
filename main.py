
import os
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
DESTINATION = os.environ.get("DESTINATION")

read_birthdays = pandas.read_csv("birthdays.csv")
month_birthdays = read_birthdays[["month", "day"]].to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

letter = random.choice(["letter_1.txt", "letter_2.txt"])

for birthday in month_birthdays:
    if month == birthday["month"] and day == birthday["day"]:
        #print("Good birthday")
        filtro = (read_birthdays["month"] == month) & (read_birthdays["day"] == day)
        name = read_birthdays.loc[filtro, "name"].item()
        with open(f"./letter_templates/{letter}") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)
            print(letter)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Cifra el correo
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=DESTINATION,
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )



