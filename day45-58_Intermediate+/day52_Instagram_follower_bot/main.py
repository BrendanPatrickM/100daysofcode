from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
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
            sleep(1)

    def follow(self):
        n = 0
        new = 0

        # this returns a list of selenium objects, each a follow button`
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                print(f'{n} followed')
                new += 1

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div/div[3]/button[2]'
                    )
                cancel_button.click()
                print(f'{n} already a follower')

            n += 1
            sleep(1)
        print(f'{new} new follows from this run')


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
