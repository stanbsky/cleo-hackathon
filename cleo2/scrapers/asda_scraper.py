"""
NOT USED IN FINAL CODEBASE DUE TO WEIRD RENDERING
"""

import requests
from bs4 import BeautifulSoup
import urllib
from pprint import pprint
from selenium import webdriver
def scrape_asda(product_name):
    driver = webdriver.Chrome()

    items = {}
    base_url = 'https://groceries.asda.com/search/%s/products?sort=price+asc'
    og_product_name = product_name
    product_name = urllib.parse.quote_plus(product_name)
    print(base_url%product_name)
    driver.get(base_url%product_name)

    soup = BeautifulSoup(driver.page_source)
    prices = soup.find_all("div", {"class":"co-product"})
    print(len(prices))
    for obj in prices:
        product_name = obj.find_all("li", {"class", "co-item ss-modified-2 ssMetricFlag"})
        if og_product_name in product_name[0].text:
            print(product_name[0].text)
            product_price = obj.find_all("strong", {"class":"co-product__price"})
            image = obj.find_all("img", {"class":"co-product__image co-item__image"})
            image_url = image[0]["src"]
            items[product_name[0].text] = {
                "price": product_price,
                "image":image_url
            }
    return items
