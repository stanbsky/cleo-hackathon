import requests
import bs4
import urllib
from pprint import pprint
from bs4 import BeautifulSoup
import json
def scrape_aldi(product_name):
    items = {}
    base_url =  "https://aldi.co.uk/search?sort=price-asc&q=%s"
    og_product_name = product_name
    product_name = urllib.parse.quote_plus(product_name)
    print(base_url%product_name)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(base_url%product_name, headers=headers)
    soup = BeautifulSoup(r.text)
    prices = soup.find_all("div", {"class":"hover-item category-item js-category-item"})
    for obj in prices:
        product_name = obj.find_all("span", {"class":"hidden gtm-product-data"})
        product_json = json.loads(product_name[0].text)
        product_name = product_json['name']
        product_price = product_json['price']
        image_src=obj.find_all("img")[0]["src"]

        if og_product_name in product_name.lower() and product_json['stateKey'] == 'instore.available':
            items[product_name] = {
                "price" : product_price,
                "image" : image_src,
                "store" : "Aldi"
            }
        else:
            print(product_name)

    return items
