import requests
from bs4 import BeautifulSoup
import urllib
from pprint import pprint
def scrape_wholefoods(product_name):
    items={}
    base_url = 'https://www.buywholefoodsonline.co.uk/catalogsearch/result/?q=%s'
    og_product_nameq = product_name
    product_name = urllib.parse.quote_plus(product_name)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(base_url%product_name, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text)
    print(r.text)
    prices = soup.find_all("li", {"class", "item"})
    print(prices)
scrape_wholefoods("oil")
