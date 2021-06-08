"""
NOT USED IN FINAL CODEBASE DUE TO WEIRD RENDERING
"""

import requests
from bs4 import BeautifulSoup
import urllib
from pprint import pprint
import json
from selenium import webdriver
def scrape_sainsburys(product_name):
    items = {}
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")

    driver = webdriver.PhantomJS(executable_path='/Users/charlie/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

    base_url = 'https://www.sainsburys.co.uk/gol-ui/SearchDisplayView?filters[keyword]=oil&langId=44&pageNumber=1&searchTerm=%s&searchType=2&sort=PRICE_ASC'
    og_product_name = product_name
    product_name = urllib.parse.quote_plus(product_name)
    driver.get("https://www.sainsburys.co.uk")
    driver.get(base_url%product_name)
    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source)
    prices = soup.find_all("div", {"class", "pt__content"})
    print(len(prices))
