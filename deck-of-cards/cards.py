from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit=suit
		self.value=value
#Определяем класс карта для того чтобы ссылаться на него в будущем для создания колоды
#Определяем атрибуты класса (масть и величина).

	def __repr__(self):
		return f'{self.value} of {self.suit}'
#Даем название для каждого обьекта класса (карты) (если его нужно будет вызвать через print)

class Deck:
	allowed_suit=["Hearts", "Diamonds", "Clubs", "Spades"]
	allowed_value=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#Перечисляем возможности для комбинации карт, чтобы потом создать из через вложенный цикл

	def __init__(self):
		self.full_deck=[]
		for a in Deck.allowed_value:
			for b in  Deck.allowed_suit:
				self.full_deck.append(Card(b,a))
#Создаем все возможные комбинации карт, и на каждую пару (масть и величина) применяем класс "Карта".
#Добавляем каждую комбинацию в список (который приравниваем к значению полной колоды в 
#в обозначении класса Колода)

	def __iter__(self):
		return iter(self.full_deck)
	i=0
	# def __next__(self):
	# 	while Deck.i<len(self.full_deck):
	# 		card=self.full_deck[Deck.i]
	# 		Deck.i+=1
	# 		return card

	def first_card(self):
		some_card = self.full_deck[Deck.i]
		Deck.i+=1
		return some_card

	def count(self):
		return len(self.full_deck)
#Создаем функцию подсчета кол-ва обьектов(карт) в обьекте класса Колода(в колоде).

	def __repr__(self):
		return f'Deck of {self.count()} cards.'
#Даем название для каждой колоды (если ее нужно будет вызвать через print). 
#Используя функцию count в скобках уже не указываем self, так как функция уже обозначена

	def _deal(self,num):
#Внутренняя функция (с общей информацией), сама по себе не используется, 
#но может вызываться внутри других функций.
		self.taken_cards=[]
		if num > self.count():
			for a in range(self.count()):
				self.taken_cards.append(self.full_deck.pop())
		elif self.count()==0:
			raise ValueError ('All cards have been dealt.')
		else:
			for a in range(num):
				self.taken_cards.append(self.full_deck.pop())
		return self.taken_cards
#Создаем функцию изьятия карт из колоды, аргумет - кол-во карт которые нужно изьять.
#Создаем список из изьятых карт. Если колода пуста - ошибка, если карт меньше чем 
#кол-во изымаемых карт - изьять существующее кол-во карт. Вернуть список из изьятых карт.

	def shuffle(self):
		if self.count()==52:
			return shuffle(self.full_deck)
		else:
			raise ValueError ('Only full decks can be shuffled.')
#Перемешиваем список из карт

	def deal_card(self):
		return self._deal(1)[0]
#Функция для изьятия 1 карты. Вызывается через функцию _deal 
#с указанием 1 карты как параметра функции. Возвращает список из изьятых карт. 
#Так как карта всегда 1, то применяется индексирование чтобы получить обьект а не список.

	def deal_hand(self, num):
		return self._deal(num)
#Функция для изьятия нескольких карты. Вызывается через функцию _deal 
#с указанием кол-ва карт как параметра функции. Возвращает список из изьятых карт. 

if __name__=='__main__':
	d1=Deck()
	# print(d1.first_card())
	# print(d1.first_card())
	print(d1.full_deck)
	d1.shuffle()
	print(d1.full_deck)
	print(d1.first_card())
	print(d1.first_card())
# for card in d1:
# 	print(card)
# print(d1)
# d1.shuffle()
# card=d1.deal_card()
# print(card)
# hand=d1.deal_hand(5)
# print(hand)
# print(d1)




		

