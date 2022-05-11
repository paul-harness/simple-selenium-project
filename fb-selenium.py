from selenium import webdriver
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
 
 
LOGIN_URL = 'https://www.facebook.com/login.php'
 
class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
 
 
    def login(self):
        email_element = driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
 
 
if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='sample@example.com', password='PASSWORD', browser='Firefox')
    fb_login.login()
