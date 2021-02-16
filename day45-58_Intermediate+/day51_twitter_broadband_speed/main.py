from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
TARGET_UP = 10
TARGET_DOWN = 200
DRIVER_PATH = "/Users/brendan/Development/chromedriver"


class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        consent = self.driver.find_element_by_css_selector(
            '#_evidon-banner-acceptbutton')
        consent.click()

        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
            'div[3]/div[1]/a')
        go_button.click()

        sleep(45)
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
            'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
            'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(self.down)
        print(self.up)
        return [self.down, self.up]

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        sleep(3)

        # Login
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/'
            'div/div[1]/label/div/div[2]/div/input'
            )
        email.send_keys(USERNAME)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/'
            'div/div[2]/label/div/div[2]/div/input'
            )
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(3)

        # Write Tweet
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
            'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/'
            'div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
            )
        tweet_compose.send_keys(
            f'Hey Internet Provider, why is my speed {self.down}Mbps down,'
            f' {self.up}Mbps up. When I pay for {TARGET_DOWN}/{TARGET_UP}'
            )
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
            'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/'
            'div[2]/div[3]'
            )
        tweet_button.click()
        self.driver.quit()


# LOGIC
bot = TwitterBot()
actual_speeds = bot.get_internet_speed()
if float(actual_speeds[0]) < TARGET_DOWN:
    bot.tweet_at_provider()
else:
    print('All Good')
