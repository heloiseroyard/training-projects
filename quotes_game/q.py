import requests
from bs4 import BeautifulSoup
from csv import DictWriter
import pickle

def url_parser(link=''):
	url='http://quotes.toscrape.com'+ str(link)
	result=requests.get(url).text
	return BeautifulSoup(result, 'html.parser')

def scrapping_quotes():
	quotes_info=[]
	page_link=''
	while True:
		parsed = url_parser(page_link)
		quotes = parsed.find_all(class_='quote')
		for quote in quotes:
			quotation = quote.find(class_='text').get_text()
			author = quote.find(class_='author').get_text()
			link = quote.find('a')['href']
			quotes_info.append({
				'quotation' : quotation, 
				'author' : author, 
				'link' : link
				})
		try:
			page_link=parsed.find(class_='next').find('a')['href']
		except:
			break	
	return quotes_info

if __name__=='__main__':
	
	def write_csv(quotes):
		with open('quotes.csv', 'w') as file:
			headers=['quotation', 'author', 'link']
			csv_writer=DictWriter(file, fieldnames=headers)
			csv_writer.writeheader()
			for quote in quotes:
				csv_writer.writerow(quote)


	quotes = scrapping_quotes()
	with open('quotes.pickle', 'wb') as file:
		pickle.dump(quotes, file)





