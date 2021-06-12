import random
import pandas
import smtplib
import datetime as dt

letter_list = []
myemail = "gabbar78dummy@gmail.com"
mypass = "78numV!54$+MmE"

# Retrieving-Letters

for i in range(1, 4):
    with open(f"./letter_templates/letter_{i}.txt") as file:
        letter = file.read()
        letter_list.append(letter)

# handling csv

records_names = pandas.read_csv("birthdays.csv")
users = records_names.to_dict(orient="records")
# handling dates


current_date = dt.datetime.now()
for user in users:
    if (user["month"] == current_date.month) & (user["day"] == current_date.day):
        print("Email Sent to ", user["name"])
        random_letter = random.choice(letter_list)
        new_letter = random_letter.replace("[NAME]", user["name"])
        with smtplib.SMTP("smtp.gmail.com.") as connection:
            connection.starttls()
            connection.login(user=myemail, password=mypass)
            connection.sendmail(from_addr=myemail,
                                to_addrs=user["email"],
                                msg=f"Subject:Happy Birthday! \n\n {new_letter}"
                                )

