# Designed by Lilaa Vinoth - PC [Oct,15 2020]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get('https://www.ilovepdf.com/jpg_to_pdf')

selector = driver.find_element_by_xpath('//*[@id="pickfiles"]')
selector.send_keys("C:\\IMG_0037.JPG")

