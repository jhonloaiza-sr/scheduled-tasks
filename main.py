##################### Hard Starting Project ######################
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
#print(month_birthdays)


now = dt.datetime.now()
month = now.month
day = now.day



letter = random.choice(["letter_1.txt", "letter_2.txt"])
#print(letter)

for birthday in month_birthdays:
    if month == birthday["month"] and day == birthday["day"]:
        #print("Good birthday")
        filtro = (read_birthdays["month"] == month) & (read_birthdays["day"] == day)
        name = read_birthdays.loc[filtro, "name"].item()
        with open(f"./letter_templates/{letter}") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)
            print(letter)

        with smtplib.SMTP("smtp.gmail.com", ) as connection:
            connection.starttls()  # Cifra el correo
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=DESTINATION,
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )






# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



