import requests
from bs4 import BeautifulSoup
from data import dict
import json

all_news = {}

def fetch_data():
    clean_data = {}
    for site in dict:
        if site['type'] == 'json':
            continue
        print(f"Fetching data from {site['nome']}...")
        response = requests.get(site['url']).text
        if response.status_code == 200:
            soup = html_to_json(response)
        else:
            print(f"failed from {site['nome']}")
            continue
    clean_data = save_json(soup)
    all_news.update(clean_data)
    return all_news


# Save what i want from json
def save_json(data):
    return data

# convert html to json
def html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup