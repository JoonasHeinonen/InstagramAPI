from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        
        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//input[@name='password']"

girdeuxIG = InstagramBot("Heinonen", "Password12345")
girdeuxIG.login()