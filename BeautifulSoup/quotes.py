#/Users/bikenkc/Desktop/web_scraping/BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://quotes.toscrape.com/'

page=requests.get(url)
#print(requests.status_code)

soup=BeautifulSoup(page.text,'lxml')
#print(soup) 


quotes=soup.find_all('div',class_='quote')
#quotes.prettify
df=pd.DataFrame({'author':[],'text':[],'tags':[]})

while True:
	for quote in quotes:
		author=quote.find('span',class_='text').text
		text=quote.find('small',class_='author').text
		tags=quote.find('meta')['content']
		df=df.append({'author':author,'text':text,'tags':tags},ignore_index=True)
		

	if soup.find('li',class_='next')==[]:
		print('ready to break')
		break
	else:
		link_path=soup.find('li',class_='next').find('a')['href']
		#print(link_path)
		full_link_path='https://quotes.toscrape.com/'+link_path
		#print(full_link_path)
		page=requests.get(full_link_path)
		soup=BeautifulSoup(page.text,'lxml')
		quotes=soup.find_all('div',class_='quote')





df.to_csv('/Users/bikenkc/Desktop/web_scraping/BeautifulSoup/quotes_multiple_pages1.csv')	
print(df)
print(len(df))
