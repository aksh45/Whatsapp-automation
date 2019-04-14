from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("/home/aki/chromedriver")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
name= input('Enter the name of user or group : ')
msg= input()
count = int(input('Enter the count : '))

arg='//span[@title = "{}"]'
t1=wait.until(EC.presence_of_element_located((By.XPATH,arg.format(name))))
t1.click()
msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()

