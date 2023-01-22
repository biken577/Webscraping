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
driver.get('https://www.nike.com/w/mens-sale-3yaepznik1')

#timed to load the page completely
time.sleep(2)
#driver.implicitely_wait(1)

#list of products
products=driver.find_elements(By.CLASS_NAME,'product-card__body')
#print(len(products))

#creating a dataframe
df=pd.DataFrame({'name':[],'category':[],'original':[],'sale':[],'link':[]})



while True:
  for product in products:
    name=product.find_element(By.CLASS_NAME,'product-card__title').text
    category=product.find_element(By.CLASS_NAME,'product-card__subtitle').text
    original=product.find_element(By.XPATH,'//div[contains(@class,"product-price is--striked-out")]').text
    sale=product.find_element(By.XPATH,'//div[contains(@class,"product-price is--current-price")]').text
    link=product.find_element(By.CLASS_NAME,'product-card__link-overlay').get_attribute('href')

    df=df.append({'name':name,'category':category,'original':original,'sale':sale,'link':link},ignore_index=True)


  #height of the page
  last_height=driver.execute_script('return document.body.scrollHeight')
  #scroll the page
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)

  new_height=driver.execute_script('return document.body.scrollHeight')

  print(last_height)
  print(new_height)
  if last_height==new_height:
    break

  #list of products for a new page
  products=driver.find_elements(By.CLASS_NAME,'product-card__body')

  
print(df)
df.to_csv('/Users/bikenkc/Desktop/web_scraping/selenium/Nike/sales1.csv')





