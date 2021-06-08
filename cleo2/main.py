from fastapi import FastAPI, Request
from scrapers import morrisons_scraper, aldi_scraper
from fastapi.templating import Jinja2Templates
import uvicorn
from pprint import pprint
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates") # we use jinja2 for the frontend

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # mount static dir

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse("index2.html", {"request":request})

@app.post('/get_prices')
async def get_prices(request:Request):
    allPrices = {}

    myForm = await request.form()
    MorrisonsPrices = morrisons_scraper.scrape_morrisons(myForm["productName"]) # get the prices from morrisons
    AldisPrices = aldi_scraper.scrape_aldi(myForm["productName"]) # get the prices from aldi
    allPrices = {**MorrisonsPrices, **AldisPrices} # merge dictionaries

    cheapest = sorted(allPrices, key=lambda x: allPrices[x]['price']) # get the keys with lowest price
    to_return = ''
    for val in cheapest[0:5]: # top 5 cheapest!
        to_return += f'Name: {val}<br>Price : £{allPrices[val]["price"]}, Store : {allPrices[val]["store"]}, <br><a href="{allPrices[val]["link"]}" target="_blank">Click me to go to the product!</a><br>"' # return html to present
    return {"content":to_return}

uvicorn.run(app)
