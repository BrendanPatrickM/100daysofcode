from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
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

email_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('pass')
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.switch_to(base_window)

# clear notifications
location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location.click()
noification_no = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
noification_no.click()
