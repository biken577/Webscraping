from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  s=Service('/usr/local/bin/chromedriver')
  driver=webdriver.Chrome(options=chrome_options,service=s)
  return driver

driver=get_driver()

#load the page
driver.get('https://quotes.toscrape.com/login')

username=driver.find_element(By.NAME,'username')
username.send_keys('kcbiken577')
# print(username)

password=driver.find_element(By.NAME,'password')
password.send_keys('123456')
# print(password)

login=driver.find_element(By.XPATH,'//input[@class="btn btn-primary"]')
login.click()
# print(login)


#play with scroll 
#Height of page =1740
height=driver.execute_script('return document.body.scrollHeight')
print(height)

#scroll down
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)

#scroll down
driver.execute_script("window.scrollBy(0,-500)","")

time.sleep(3)

#scroll till it finds a webelement
next_button=driver.find_element(By.XPATH,'//a[text()="Next "]')
print(next_button)
driver.execute_script("arguments[0].scrollIntoView();",next_button)

#scroll to the bottom of the page
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


#quit the driver
#driver.quit()
