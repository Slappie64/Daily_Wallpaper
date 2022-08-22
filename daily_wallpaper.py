#! /usr/bin/python3

# Imports
import requests
from bs4 import BeautifulSoup 

image_search_url = 'https://www.pexels.com/search/nature/?size=large&orientation=landscape'
image_search_data = requests.get(image_search_url)

soup = BeautifulSoup(image_search_data.content, 'html.parser')

for i in soup:
    print(i)

image_url = 'https://images.pexels.com/photos/844297/pexels-photo-844297.jpeg?auto=compress&cs=tinysrgb&w=400'
image_data = requests.get(image_url).content

image_name = 'name'

with open (image_name, 'wb') as handler:
    handler.write(image_data)
