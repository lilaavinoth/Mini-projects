# Designed my Lilaa Vinoth - PC [Sep,17 2020]

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')

all_names = ["Amma", "Kavi"]
filepath = ["E:\CANON\IMG_0032.JPG"]

input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    image_box = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)

    sleep(2)

    send_button = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
    send_button.click()
