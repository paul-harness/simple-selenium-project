# tutorial to get page source of google.com
from selenium import webdriver
import pytest
from time import sleep
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

# print page source for URL
driver.get(https://'lambdatest.github.io/sample-todo-app/')
driver.maximize_window()
driver.find_element_by_name("li1").click()
driver.find_element_by_name("li2").click()

title = "Sample page - lambdatest.com"
assert title == chrome_driver.title

sample_text = "Happy Testing at LambdaTest"
email_text_field = chrome_driver.find_element_by_id("sampletodotext")
email_text_field.send_keys(sample_text)
sleep(5)

driver.find_element_by_id("addbutton").click()
sleep(5)

output_str = driver.find_element_by_name("li6").text
sys.stderr.write(output_str)
    
  
sleep(2)
driver.close()
