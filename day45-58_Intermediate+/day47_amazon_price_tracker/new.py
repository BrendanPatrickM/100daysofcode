import smtplib
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user='brendanpython@gmail.com', password='Python1977!!')
    connection.sendmail(
        from_addr='brendan_python@gmail.com',
        to_addrs='brendan_python@gmail.com',
        msg='Subject: product name\n\nCurrent price is'
    )