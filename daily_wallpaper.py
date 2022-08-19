#! /usr/bin/python3

# Imports
import secret
from pexels_api import API

api = API(secret.api_key)
api.search('Abstract', page=1, results_per_page=10)
photos = api.get_entries()
for photo in photos:
    print(photo.url)
