import requests
import sys
import hashlib

def get_hashes(first_chars):
	url = 'https://api.pwnedpasswords.com/range/'+ first_chars
	res = requests.get(url).text 
	return [(line.split(':')) for line in res.splitlines()]


def check_pass(tail_list, end_part):
	for (password,num) in tail_list:
		if end_part.upper()==password:
			return num
	return 0


def ecription(password):
	sha1pass=hashlib.sha1(password.encode('utf-8')).hexdigest()
	main_part, tail = sha1pass[:5], sha1pass[5:]
	passwords = get_hashes(main_part)
	return check_pass(passwords, tail)

def main(args):
	for password in args:
		if ecription(password):
			print(f'Yor password {password} has been hacked {ecription(password)} times')
		else:
			print('No match found')

if __name__=='__main__':
	main(sys.argv[1:])
