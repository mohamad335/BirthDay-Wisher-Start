
from datetime import datetime
import smtplib
import random
import pandas
MY_EMAIL= "blackjack@gmail.com"#note: these email and pass are example not correct email  
PASSWORD="abcdapple123"
today = datetime.now()
today_tuple=(today.month,today.day)#first we put the current month and day on tuple
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}#then we put the day of birth and month as type of tuple on dictionary with it value
if today_tuple in birthday_dict:#check if birthday same as the current day
    birthday_person= birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"#to get a random message of birthday message
    with open(file_path) as letter_file:#we open the file and then read it and replace the name with the name of person birthday's
        name= letter_file.read()
        name= name.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{name}"
                            )







 
       
        

