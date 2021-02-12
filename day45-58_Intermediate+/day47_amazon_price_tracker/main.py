from bs4 import BeautifulSoup
import smtplib
import requests
import os

URL = 'https://www.amazon.co.uk/gp/product/B08KQGZ19V?pf_rd_r=J06GMVK2CJVK4V8JKB68&pf_rd_p=6e878984-68d5-4fd2-b7b3-7bc79d9c8b60&pd_rd_r=e4c54cbe-58e3-4408-bd8a-f8749bf0537a&pd_rd_w=0ESkl&pd_rd_wg=o0rza&ref_=pd_gw_unk'
TARGET_PRICE = 86.39
my_email = os.environ.get('EMAILENV')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Accept-Language': 'en-gb'
}

response = requests.get(url=URL, headers=headers)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

prod_name = soup.find(name='span', class_='a-size-large product-title-word-break').text.strip('\n')
print(prod_name)

price = float(soup.find(
    name='span',
    class_='a-size-medium a-color-price priceBlockBuyingPriceString'
).text.split('£')[1])

if price <= TARGET_PRICE:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password='Python1977!!')
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject: {prod_name}\n\nPrice alert, the current price is {price}'
        )