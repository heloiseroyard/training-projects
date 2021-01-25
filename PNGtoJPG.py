import sys
import os
import re
from PIL import Image



directory = sys.argv[1] #path to directory with images
new_directory = sys.argv[2] #path to new directory


# try to make new directory (if it doesn't exist)
def create_dir(new_directory):
	try:
		os.mkdir(f'.\\{new_directory}')
	except OSError:
		pass

create_dir(new_directory)
#searching for name of file without format
pattern = re.compile(r'(.+)(\..+)')

for file in os.listdir(directory):
	name=pattern.search(file).groups()[0]
	im = Image.open(f'{directory}{file}')
	im.save(f'{new_directory}{name}.png','png')



