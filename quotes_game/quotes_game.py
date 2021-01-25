import requests
from bs4 import BeautifulSoup
from random import choice
from q import url_parser
# from csv import DictReader
import pickle

# def read_csv():
# 	with open('quotes.csv', 'r') as file:
# 		quotes = DictReader(file)
# 		quotes=list(quotes)
# 	return quotes

def read_pickle():
	with open('quotes.pickle', 'rb') as file:
		return pickle.load(file)

def play_again():
	again=input('Do you want to play again? :')
	if again.lower().startswith('y'):
		return True
	else:
		return False

def scraping_author_info(page):
	date=page.find(class_='author-born-date').get_text()
	place=page.find(class_='author-born-location').get_text()
	return {'date':date, 'place':place}

def author_names(name):
	names = name.split()
	first = names[0]
	last = names[1]
	return {'first': first, 'last': last}

def guess(quotes):
	again=True
	while again:	

		random_quote = choice(quotes)
		parsed_hint_page = url_parser(random_quote['link'])
		scraping_info = scraping_author_info(parsed_hint_page)
		author_name = author_names(random_quote['author'])
		print(f'Here is a quote: \n')
		print(random_quote["quotation"])
		num_guesses=4

		while num_guesses>0:

			print()
			guess = input(f'Who said that? Guesses left: {num_guesses} ')
			if guess.lower() == random_quote['author'].lower():
				print(f'You guessed correcttly! Congratulations!')
				break
			else: 
				num_guesses-=1
				if num_guesses == 3:
					print(f'Here is a hint: The author was born in {scraping_info["date"]} in {scraping_info["place"]}')
				if num_guesses == 2:
					print(f'Here is a tip: The author\'s first name starts with {author_name["first"][0]}.')
				if num_guesses == 1:
					print(f'Here is a tip: The author\'s last name starts with {author_name["last"][0]}.')
				if num_guesses == 0:
					print(f'Sorry! You have run out of guesses. The answer was {random_quote["author"]}')
			
		again = play_again()
				
	print('Thank you for playing')

quotes_list=read_pickle()
guess(quotes_list)







