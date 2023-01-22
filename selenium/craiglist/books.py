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
driver.get('https://dallas.craigslist.org/search/bka')

#finding the all the books in a page
books=driver.find_elements(By.CLASS_NAME,'result-row')
# print(books[0:5])
# print(len(books))
df=pd.DataFrame({'name':[],'price':[],'date':[],'location':[],'details':[]})

# while True:
for book in books:
  name=book.find_element(By.XPATH,'//*[@class="result-title hdrlnk"]').text
  price=book.find_element(By.CLASS_NAME,'result-price').text
  date=book.find_element(By.CLASS_NAME,'result-date').text

  #testing
  

  link=book.find_element(By.XPATH,'//a[@class="result-title hdrlnk"]').get_attribute('href')
  print(link)

  time.sleep(3)
  #go to the other page
  driver.execute_script("window.open('');")
  time.sleep(3)
  driver.switch_to.window(driver.window_handles[1])
  driver.get(link)

  #driver.findElement(By.tagName("div")).getAttribute("innerText")
  details=driver.find_element(By.ID,'postingbody').text
  try:
    location=driver.find_element(By.CLASS_NAME,'mapaddress').text
  except:
    location='Not Available'
  
  #df=df.append({'location':location,'details':details},ignore_index=True)

  time.sleep(3)
  driver.close()

  driver.switch_to.window(driver.window_handles[0])

  time.sleep(3)
  
  

  df=df.append({'name':name,'price':price,'date':date,'location':location,'details':details},ignore_index=True)
  
  

  # try:
    # next_page=driver.find_element(By.XPATH,'//a[@class="button next"]')
    # next_page.click()
    # books=driver.find_elements(By.CLASS_NAME,'result-row')
  # except:
    # print("cannot click")
    # break



  
  
df.to_csv('/Users/bikenkc/Desktop/web_scraping/selenium/craiglist/books4.csv')
print(df)
