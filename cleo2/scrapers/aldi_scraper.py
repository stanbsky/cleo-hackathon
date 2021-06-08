import requests
import bs4
import pandas as pd
import urllib
from bs4 import BeautifulSoup
def items_on_sale(product_name):
    items = {}
    base_url =  "aldi.co.uk/search?sort=price-asc&q=%s"
    og_product_name = product_name
    product_name = urllib.parse.quote_plus(product_name)
