import requests
import json

url1 = 'https://ja.wikipedia.org/w/api.php?action=parse&page=Works%20Human%20Intelligence&prop=wikitext&formatversion=2&format=json'
res = requests.get(url1)
list = res.json()
print(list.get("parse").get("wikitext"))
print("\n")
