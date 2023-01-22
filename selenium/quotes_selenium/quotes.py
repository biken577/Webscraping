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
driver.get('https://quotes.toscrape.com/')

#print page source
#print(driver.page_source)

#find the all the webelements
quotes=driver.find_elements(By.CLASS_NAME,'quote')

#create empty dataframe
df=pd.DataFrame({'text':[''],'author':[''],'tags':['']})

while True:
	for quote in quotes:
		text=quote.find_element(By.CLASS_NAME,'text').text
		author=quote.find_element(By.CLASS_NAME,'author').text
		tags=quote.find_element(By.CLASS_NAME,'keywords').get_attribute('content')

		#appending data in dataframe
		#df=df.append({'text':text,'author':author,'tags':tags},ignore_index=True)
		
	try:
		print(driver.find_element(By.XPATH,'//*[@class="next"]/a').get_attribute('href'))
		driver.find_element(By.XPATH,'//*[@class="next"]/a').click()
		time.sleep(1)
		quotes=driver.find_elements(By.CLASS_NAME,'quote')
	except:
		print('Last Page')
		break


#converting dataframe to csv file
df.to_csv('/Users/bikenkc/Desktop/web_scraping/selenium/quotes_selenium/testfile.csv')

#print(text)
#print(author)
#print(tags)

