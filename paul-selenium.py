# tutorial to get page source of google.com
from selenium import webdriver
URL = os.environ.get('PLUGIN_URL') 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('URL')
print(driver.page_source)
