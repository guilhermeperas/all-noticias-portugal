from os import link
import requests
from bs4 import BeautifulSoup
from app.helpers.json_helper import get_nested_value, save_json, load_json

sites_config = []
all_news = {}

def fetch_data(page=1):
    sites_config = load_json('config.json')
    clean_data = {}
    for site in sites_config: 
        current_site = site['nome']
        if current_site != "Sic Noticias":
            continue
        link = site['url'].format(category_slug=site.get('categorias', {}).get('principal',''),page=page,count=2)
        response = requests.get(link)
        print(link)
        if response.status_code != 200:
            continue
        if site['type'] == 'html':
            clean_data = html_to_json(response.text)
        else:
            clean_data = save_json(response.json(), site.get('data_mapping', {}))
            return
    all_news.update({
        "site": current_site,
        "news": clean_data    
    })
    return all_news

def html_to_json(html_content):
    news = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for item in soup.find_all('article'):
        print(item)
        return
        link_tag = item.find('a')
        link = link_tag.get('href', '')
        title = item.find('span').text.strip()
        img = item.find("picture").find("img")
        desc = img.get('alt', '') 
        img = img.get('src', '')

        news.append({
            'title': title,
            'link': link,
            'img': img,
            'desc': desc
        })
        print(news)
    return news