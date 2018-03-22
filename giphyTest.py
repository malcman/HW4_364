from giphy_api_key import api_key
import json
import requests

baseurl = "https://api.giphy.com/v1/gifs/search"
params = {'api_key': api_key, 'q': 'The Office'}
r = requests.get(baseurl, params = params)

with open('gipyTest.json', 'w') as f:
	f.write(json.dumps(json.loads(r.text), indent = 2))