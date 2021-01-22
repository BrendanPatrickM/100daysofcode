import datetime as dt
import pandas
import smtplib
import random
MY_MAIL = ''
MY_PASS = ''


def get_message_text():
    filepath = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    real_name = data_dict[key][0]
    with open(filepath) as letter_file:
        text = letter_file.read()
        text = text.replace('[NAME]', real_name)
        return text


def send_email():
    print('sending email...')
    email_to = data_dict[key][1]
    print(email_to)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_MAIL,
                         password=MY_PASS)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=email_to,
            msg=f'Subject: Happy Birthday\n\n{text}'
        )


now = dt.datetime.now()
today_day = now.day
today_month = now.month
data = pandas.read_csv('birthdays.csv')
data_dict = {(row.month, row.day): [row.recipient, row.email] for (index, row) in data.iterrows()}
key = (today_month, today_day)

if key in data_dict:
    text = get_message_text()
    send_email()
