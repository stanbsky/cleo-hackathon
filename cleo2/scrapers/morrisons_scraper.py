"""
NOT USED IN FINAL CODEBASE DUE TO WEIRD RENDERING
"""


import requests
from bs4 import BeautifulSoup
import urllib
from pprint import pprint
import json
def scrape_morrisons(product_name:str) -> dict:
    items = {}
    base_url = 'https://groceries.morrisons.com/search?entry=%s&sort=PRICE_ASC'
    og_product_name = product_name
    product_name = urllib.parse.quote_plus(product_name)
    #print(product_name)
    #print(base_url%product_name)
    r = requests.get(base_url%product_name)
    #print(r.status_code)
    soup = BeautifulSoup(r.text)
    prices = soup.find_all("div", {"class":"fop-contentWrapper"})
    #pprint(prices)
    #print(r.text)
    #print(type(prices))
    for obj in prices:
        product_name = obj.find_all("h4", {"class":"fop-title"})
        if og_product_name not in str(product_name).lower():
            pass
        else:
            azs=obj.find_all("a")
            link = azs[0]["href"]
            product_price = obj.find_all("span", {"class":"fop-price"})[0].text
            product_image = obj.find_all("img",{"class":"fop-img"})
            image_url = "https://groceries.morrisons.com/" + product_image[0]["src"]
            price_to_send = 0
            if product_price[-1] == 'p':
                price_to_send = float(product_price[:-1])
            else:
                price_to_send = float(product_price[1:])
            items[str(product_name[0].text)] = {
                "price":price_to_send,
                "image":image_url,
                "store":"Morrisons",
                "link":"https://groceries.morrisons.com"+link
            }
    sorted(items, key=lambda x: items[x]['price'])
    return items
