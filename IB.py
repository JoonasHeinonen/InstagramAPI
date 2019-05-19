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
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)

        # "//a[@href'accounts/login']"
        # "//input[@name='username']"Kirjaudu sisään<a href="/accounts/login/?source=auth_switcher">Kirjaudu sisään</a>
        # "//input[@name='password']"

girdeuxIG = InstagramBot("Heinonen", "Password12345")
girdeuxIG.login()