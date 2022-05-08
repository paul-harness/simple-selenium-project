from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--no-sandbox')

driver =  webdriver.Chrome('./chromedriver', options=chrome_opt)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
