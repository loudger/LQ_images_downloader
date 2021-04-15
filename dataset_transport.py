import os
from os.path import isfile, join
from os import listdir
from PIL import Image, ImageDraw 

def __get_image_pixels(image_path):
	image = Image.open(image_path)
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	r_all = []
	g_all = []
	b_all = []
	for x in range(width):
		for y in range(height):
			r = pix[x, y][0] #узнаём значение красного цвета пикселя
			g = pix[x, y][1] #зелёного
			b = pix[x, y][2] #синего
			r_all.append(r)
			g_all.append(g)
			b_all.append(b)
	return r_all, g_all, b_all

General_folder_name = 'dataset_images'
labels = ['car', 'plane', 'ship']

print(os.getcwd())

def load_dataset():
	BASE_DIR = os.path.join(os.path.dirname( __file__ ))
	General_folder_path = os.path.join(BASE_DIR, General_folder_name)

	dataset_pixels = []
	dataset_labels = []

	for index, label in enumerate(labels):
		index += 1
		subject_folder_path = os.path.join(General_folder_path, label)
		files = os.listdir(subject_folder_path)
		for file in files:
			img_path = os.path.join(subject_folder_path, file)
			# print(img_path)
			dataset_pixels.append(__get_image_pixels(img_path))
			dataset_labels.append(index)
	return dataset_pixels, dataset_labels
