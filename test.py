import requests
from data import dict

data = requests.get(dict[0]["url"]).json()
print(data.keys())
