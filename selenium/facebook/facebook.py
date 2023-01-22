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
  chrome_options.add_argument('--disable-notifications')
  s=Service('/usr/local/bin/chromedriver')
  driver=webdriver.Chrome(options=chrome_options,service=s)
  return driver


driver=get_driver()
driver.get('https://www.facebook.com/login')


#Add wait time to make sure the website is fully loaded
time.sleep(3)

#Login with username and password
email=driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys('')   #pass user name or phone number
password=driver.find_element(By.XPATH,'//*[@id="pass"]')
password.send_keys('')     #pass password

#login
button=driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
button.send_keys(Keys.ENTER)

WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Search Facebook"]')))
#go on the search box 
search=driver.find_element(By.XPATH,'//*[@aria-label="Search Facebook"]')

#type string in the search box
search.send_keys('robinhood')
search.send_keys(Keys.ENTER)

#WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jsc_c_s"]//a'))).click()
#WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="nc684nl6"]')))
#search the group and enter the group
time.sleep(3)
robinhood=driver.find_element(By.XPATH,'//a[@aria-label="Robinhood, Verified account"]')
#print(type(robinhood))
#print(robinhood)
robinhood.click()

time.sleep(2)
# divs=driver.find_elements(By.XPATH,'//div[@class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')
# for i,div in enumerate(divs):
  # text=div.find_element(By.XPATH,'//div[@data-ad-preview="message"]').text()
  # print(i,':',text)
#//div[@class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]

#using beautiful soup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

divs=soup.find_all('div',class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')
for div in divs:
  text=div.get_text()
  print(text)



#last_height=driver.execute_script('return document.body.scrollHeight')
#print(last_height)


#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#new_height=driver.execute_script('return document.body.scrollHeight')
#print(last_height)
#print(new_height)
#if last_height==new_height:

#id="jsc_c_1yv"
#data-ad-preview="message"
#data-ad-comet-preview="message"

#//div[@data-ad-preview="message"]//text()
#getText()
#du4w35lb k4urcfbm l9j0dhe7 sjgh65i0
