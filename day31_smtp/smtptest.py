# import smtplib

# my_email = 'brendanpython@gmail.com'
# my_password = 'Python1977!!'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='brendanmurrayfl@gmail.com',
#         msg='Subject: Hello\n\nHello Brendan'
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)
print(year)

date_of_birth = dt.datetime(year=1984, month=8, day=3)
print(date_of_birth)