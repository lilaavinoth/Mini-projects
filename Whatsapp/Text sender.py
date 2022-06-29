# Designed by Lilaa Vinoth - PC [Oct,15 2020]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')

all_names = ['Amma','Kavi']

input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    msg_box.click()
    msg_box.send_keys(Keys.CONTROL, 'v')

    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    button.click()
