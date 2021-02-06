import datetime as dt
import random
import smtplib

my_email = ''
my_password = 'Python1977!!'


with open('day31_smtp/quotes.txt', 'r') as quote_file:
    quotes = quote_file.readlines()
   

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    quote_num = random.randint(0, len(quotes))

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Motivational Monday\n\n{quotes[quote_num]}"
        )
