import os
from os.path import isfile, join
from os import listdir, path

name_pattern = input('Шаблон имени: ')
i = 1
BASE_DIR = os.path.join(os.path.dirname( __file__ ))
files = os.listdir(BASE_DIR)
files.remove(os.path.basename(__file__))
for file in files:
	fullname = os.path.join(BASE_DIR, file)
	if os.path.isfile(fullname):
		os.rename(file, f'{name_pattern}_{i}.jpg')
		i += 1


