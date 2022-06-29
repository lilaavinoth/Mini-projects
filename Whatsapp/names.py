# Designed by Lilaa Vinoth - PC [Oct,15 2020]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import clipboard
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
import numpy as np
driver.get('https://web.whatsapp.com/')

all_names = ['Amma','Nanda Kishore','Manickam','Farook','Xaviour','Vikash','Akshita Akka','Raj Pandi','Yogesh','Vinoth','Parasuram','Suganthan Russia','Sahul','Das','Haridas SRM','Kavi','Arun DSM','Siddeshwar','Logesh','Yuvaraj','Sri Ram','Avinash','Mani CSE','Varshini SRM']
count = 1
nick_name = np.array(['Amma','Nanda Kishore','Manickam','Farooq','Xaviour','Vikash','Akshita Akka','Raj Pandi','Yogesh','Vinoth','Parasu','Suganthan','Sahul','Das','Haridas','Kavi Priya','Arun','Siddesh','Logesh','Yuvaraj','Sri Ram','Avinash','Mani','Varshini'])

num = 0
input('Enter anything after scanning QR code')

for name in all_names:

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,'//span[@title = "{}"]'.format(name)))
        )
        element.click()
    except:
        print('except has reached')

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    clipboard.copy('Hi ' + nick_name[num] + ', this is to inform you that Lilaa Vinoth no longer have access to this '
                                            'WhatsApp account for the next 1 hour.\n\nAny message you send within the '
                                            'time period will be managed by a machine. The access will be revoked '
                                            'automatically to him at 10:25 PM.\n\n *~This message was created and sent '
                                            'by LVAI*')



    msg_box.click()
    msg_box.send_keys(Keys.CONTROL, 'v')
    num += 1



    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    button.click()


    
