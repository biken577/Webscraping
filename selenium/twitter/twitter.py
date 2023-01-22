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
import re


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  s=Service('/usr/local/bin/chromedriver')
  driver=webdriver.Chrome(options=chrome_options,service=s)
  return driver


driver=get_driver()


wait = WebDriverWait(driver, 30)
driver.get('https://www.twitter.com/login')

username_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
username_input.send_keys('') #pass username or phone number
username_input.send_keys(Keys.ENTER)
time.sleep(2)
password=driver.find_element(By.NAME,'password')
password.send_keys('')    #pass password
password.send_keys(Keys.ENTER)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@type="text"]')))

search=driver.find_element(By.XPATH,'//input[@type="text"]')
search.send_keys('elon musk')
search.send_keys(Keys.ENTER)

#click on people's tab
time.sleep(5)
people=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a').click()

#click on profile 
time.sleep(3)
user=driver.find_element(By.XPATH,'//span[contains(text(),"Elon Musk")]').click()
#user=driver.find_element(By.XPATH,'//span[contains(text(),"Elon Musk")])

time.sleep(10)
soup=BeautifulSoup(driver.page_source,'lxml')

with open("output1.lxml", "w") as file:
    file.write(str(soup))


#with open('tweet.html','w') as f:
  #f.write(get_source)
# last_height=driver.execute_script('return document.body.scrollHeight')
# postings=driver.find_elements(By.XPATH,'//div[starts-with(@id,"id_")]/span')
# tweets=[]
# i=0
# while i<30:
#   try:
#     for post in postings:
#       post=post.text
#       tweets.append(post)
#   except:
#       pass
#   driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#   new_height=driver.execute_script('return document.body.scrollHeight')
#   time.sleep(2)
#   postings=driver.find_elements(By.XPATH,'//div[starts-with(@id,"id_")]/span')
#   i=i+1
# print(tweets)
# if len(tweets)>200:
#   break
# df = pd.DataFrame(tweets, columns=['tweets'])
# df.to_csv('/Users/bikenkc/Desktop/web_scraping/twitter/elontweet2.csv')

#Beautiful soup method
# soup=BeautifulSoup(driver.page_source,'lxml')
# postings=soup.select('div[class^=id_]>span')
# tweets=[]

# #while True:
# for post in postings:
#   tweets.append(post.text)
#   break
# time.sleep(1)
# #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# #time.sleep(1)
# #soup=BeautifulSoup(driver.page_source,'lxml')
# #postings=soup.select('div[class^=id_]>span')
# #tweets2=list(set(tweets))

# #if len(tweets2)>50:
#   #break
# print(soup)
# print(tweets)






