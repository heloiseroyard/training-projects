import requests
from bs4 import BeautifulSoup
import sys
import 

def get_parser(url):
	res = requests.get(url).text
	return BeautifulSoup(res, 'html.parser')

def get_info(soup):
	athing = soup.find_all(class_='athing')
	score = soup.find_all(class_='subtext')
	new_link = soup.find(class_='morelink')['href']
	return (zip(athing, score), new_link)

def sort_by_views(lst):
	return sorted(lst, key=lambda n: n['views'], reverse=True)

def scrape(soup, rate, n):
	lst=[]
	for _ in range(n):
		zipped_info = get_info(soup)[0]
		new_link = get_info(soup)[1]
		for (article,views) in zipped_info:
			try:
				num_views = views.find(class_='score').get_text()
			except:
				pass
			else:
				number = int(''.join([s for s in num_views if s.isdigit()]))
				if number > rate:
					title = article.find(class_='storylink').get_text()
					link = article.find(class_='storylink')['href']
					lst.append({'title': title, 'views': number, 'link': link})
		soup = get_parser(f'{url}{new_link}')
	return sort_by_views(lst)

url = 'https://news.ycombinator.com/'
soup = get_parser(url)
print(scrape(soup, int(sys.argv[1]), int(sys.argv[2])))
