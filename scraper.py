from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def selectOption(select,texttoselect):
    options = select.find_elements_by_tag_name("option")
    if options:
        for o in options:
            if o.text == texttoselect:
                o.click()

browser = webdriver.Firefox()
browser.get('http:///www.seek.co.nz')

keywords = browser.find_element_by_id('Keywords')
#require initial backspace to delete default text
keywords.send_keys(Keys.BACK_SPACE + "tech")
industries = browser.find_element_by_id('catindustry')
selectOption(industries,'Legal')
search = browser.find_element_by_id('DoSearch')
search.submit()
#this is an example to visually demonstrate controlling the browser
#however normally you would close the browser instance  with:
#browse
