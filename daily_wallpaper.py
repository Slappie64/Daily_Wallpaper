#! /usr/bin/python3

# Imports
import requests

url = 'https://www.pexels.com/search/abstract/?orientation=landscape'
page = requests.get(url)

print(page.text)
