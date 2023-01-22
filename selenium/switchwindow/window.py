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

url1='https://www.nike.com/w/mens-sale-3yaepznik1'
url2='https://www.adidas.com/us'
#load the page
driver.get(url1)

time.sleep(3)
#open a new window with execute_script()
driver.execute_script("window.open('');")

time.sleep(3)
#switch to new window
driver.switch_to.window(driver.window_handles[1])
driver.get(url2)

time.sleep(3)
#close window in focus
driver.close()

time.sleep(3)
#switch back to old window
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)
driver.close()
