from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASS')

path = '/Users/brendan/Development/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://tinder.com')

# LOGIN
login = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login.click()
sleep(3)
login_fb = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_fb.click()
# Bring popup into focus and enter details then focus back on base window
base_window = driver.window_handles[0]
login_popup = driver.window_handles[1]
driver.switch_to.window(login_popup)

sleep(1)
email_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('pass')
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

print(driver.window_handles)
driver.switch_to.window(base_window)
print(driver.title)


# clear notifications
sleep(7)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
sleep(2)

# click like

for n in range(10):

    # Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
