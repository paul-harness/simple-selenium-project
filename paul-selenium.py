from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()
