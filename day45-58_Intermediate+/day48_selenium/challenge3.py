from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "/Users/brendan/Development/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get('http://secure-retreat-92358.herokuapp.com')
name = driver.find_element_by_name("fName")
lname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')

name.send_keys('Brendan')
lname.send_keys('Murray')
email.send_keys('fake@email.com')
name.send_keys(Keys.ENTER)

# driver.quit()
