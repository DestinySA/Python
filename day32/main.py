import random
import pandas
import smtplib
from datetime import datetime

##################### Extra Hard Starting Project ######################

data_file = pandas.read_csv("birthdays.csv")
birthday_dict = { (data_row["month"], data_row["day"]) : data_row for (index, data_row) in data_file.iterrows() }

today_tuple = (datetime.now().month, datetime.now().day)

if today_tuple in birthday_dict:
    birthday_name = birthday_dict[today_tuple]["name"]
    birthday_email = birthday_dict[today_tuple]["email"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", f"{birthday_name}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="miguelangelsonarc17@gmail.com", password="prsp itud hyur axsp")
            connection.sendmail(from_addr="miguelangelsonarc17@gmail.com", to_addrs=f"{birthday_email}", msg=f"Subject: {birthday_name}\n\n{letter}")
