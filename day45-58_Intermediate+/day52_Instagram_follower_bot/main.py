from selenium import webdriver
import os


DRIVER_PATH = '/Users/brendan/Development/chromedriver'
INSTA_USER = os.environ.get('INSTAUSER')
INSTA_PASS = os.environ.get('PASSWORD')
SIMILAR_ACCOUNT = 'https://www.instagram.com/dji_official/'

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        print('initialising')

    def login(self):
        print('login step')
        self.driver.get('https://www.instagram.com')
        

    def find_followers(self):
        print('find step')

    def follow(self):
        print('follow step')

insta_bot = InstaFollower()
insta_bot.login()