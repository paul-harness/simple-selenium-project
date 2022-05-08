# tutorial to get page source of google.com
from selenium import webdriver
import os

URL = os.environ.get('PLUGIN_URL')
SEARCHTERM = os.environ.get('PLUGIN_SEARCHTERM')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

# print page source for URL
driver.get(URL)
print(driver.page_source)

# return TRUE if SEARCHTERM is in page source
# Getting current URL source code 
get_source = driver.page_source
  
# Text you want to search
search_text = SEARCHTERM
  
# print True if text is present else False
print(search_text in get_source)

