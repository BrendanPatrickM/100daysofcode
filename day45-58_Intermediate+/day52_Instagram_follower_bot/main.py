from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


DRIVER_PATH = '/Users/brendan/Development/chromedriver'
INSTA_USER = os.environ.get('INSTAUSER')
INSTA_PASS = os.environ.get('PASSWORD')
SIMILAR_ACCOUNT = 'https://www.instagram.com/dji_official/'


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com')
        accept_button = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/button[1]'
            )
        accept_button.click()
        sleep(1)
        username = self.driver.find_element_by_name('username')
        username.send_keys(INSTA_USER)
        password = self.driver.find_element_by_name('password')
        password.send_keys(INSTA_PASS)
        password.send_keys(Keys.ENTER)
        sleep(3)
        notifications_no = self.driver.find_element_by_xpath(
          '/html/body/div[4]/div/div/div/div[3]/button[2]'
        )
        notifications_no.click()

    def find_followers(self):
        print('find step') 
        self.driver.get(SIMILAR_ACCOUNT)
        sleep(1)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
            )
        followers.click()
        sleep(2)
        # on the followers modal window
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]'
            )
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
                )
            sleep(2)

    def follow(self):
        print('follow step')


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
