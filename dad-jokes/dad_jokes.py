from pyfiglet import figlet_format
import requests
from random import choice, randint

def figet_print():
	print(figlet_format('DAD JOKES!'))

def play_again():
	again = input('Do you want to play again: ')
	if again.lower().startswith('y'):
		return get_info()
	else:
		print('Thank you :)')

def get_api(keyword, num=None):
	url='https://www.icanhazdadjoke.com/search'
	response=requests.get(
		url,
		headers={'Accept':'application/json'},
		params={'term':keyword, 'limit':num})
	return response

def random_joke(keyword):
	response = get_api(keyword)
	length=len(response.json()['results'])

	if not response.json()["total_jokes"]:
		print(f'Sorry. There are no jokes about {keyword}. Try another topic.')
	elif response.json()["total_jokes"]==1:
		print(f'I\'ve got one joke about {keyword}. Here it is.')
		print(response.json()['results'][0]['joke'])
	else:
		print(f'I\'ve got {response.json()["total_jokes"]} jokes about {keyword}. Here\'s one for you.')
		print(response.json()['results'][randint(0,length-1)]['joke'])


def num_of_jokes(keyword, num):
	response = get_api(keyword, num)
	if not response.json()["total_jokes"]:
		print(f'Sorry. There are no jokes about {keyword}. Try another topic.')
	elif len(response.json()['results']) < num:
		print(f'Sorry:( I could only find {len(response.json()["results"])} jokes about {keyword}.')
	i=1
	for a in response.json()['results']:
		print(f'{i}. {a["joke"]}')
		i+=1

def get_info():
	print('If you want to exit press \'q\'.')
	keyword=input('What topic? ')
	choice=input('Random joke or some jokes? :')
	if choice.lower().startswith('r'):
		random_joke(keyword)
	else:
		num = making_choice(choice)
		if num:
			num_of_jokes(keyword, num)
		else:
			return
	play_again()


def making_choice(choice):
	if choice.lower().startswith('q'):
		print('Thank you:)')
		return None
	elif choice.isdigit():
		return int(choice)
	elif choice.lower().startswith('s'):
		while True:
			num=input('How many jokes? ')
			if num.lower().startswith('q'):
				print('Thank you:)')
				return
			try:
				num=int(num)
			except ValueError:
				print('You can only enter numbers.')
			else:
				return num

	

if __name__ == '__main__':
	figet_print()
	get_info()