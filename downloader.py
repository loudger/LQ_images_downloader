import os
import re

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def name_gen(word):
	i = 0
	while True:
		i += 1
		yield f'photos/{word}_{i}.jpg'

def next_name(gen_func):
	return next(gen_func)


def download_uri(uri, dir='./'):
	with open(dir + uri.split('/')[-1], 'wb') as f:
		f.write(requests.get(uri, stream=True).content)

def download_image(url, gen_func):
	p = requests.get(url)
	out = open(next_name(gen_func), "wb")
	out.write(p.content)
	out.close()


def download_bing(word, gen_func):
	url = 'https://www.bing.com/images/search?q=' + word
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	images = soup.find_all('img', {'class': 'mimg rms_img'})
	for image in images:
		print(image['src'])
		download_image(image['src'], gen_func)

def download_google(word, gen_func):
	url = r'https://www.google.ru/search?q='+ word +'&newwindow=1&source=lnms&tbm=isch'
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	images = soup.find_all('img', {'class':'t0fcAb'})
	for image in images:
		print(image['src'])
		download_image(image['src'], gen_func)

def create_folder_if_not_exist():
	if not os.path.exists('photos/'):
		os.makedirs('photos/')

if __name__ == '__main__':
	word = input("Input key word: ")
	create_folder_if_not_exist()
	gen_func = name_gen(word)
	download_bing(word, gen_func)
	download_google(word, gen_func)

