from fastapi import FastAPI, Request
from scrapers import morrisons_scraper, aldi_scraper
from fastapi.templating import Jinja2Templates
import uvicorn
from pprint import pprint
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse("index2.html", {"request":request})

@app.post('/get_prices')
async def get_prices(request:Request):
    allPrices = {}

    myForm = await request.form()
    MorrisonsPrices = morrisons_scraper.scrape_morrisons(myForm["productName"])
    AldisPrices = aldi_scraper.scrape_aldi(myForm["productName"])
    allPrices["Morrisons"] = MorrisonsPrices
    allPrices["Aldi"] = AldisPrices
    pprint(allPrices)
    to_return = ''
    cnt = 0
    for i in allPrices["Morrisons"]:
        print(i)
        cnt+=1
        to_return += f'Price : {allPrices["Morrisons"][i]["price"]}, Store : Morrisons, Name: {i}<br>'
        if cnt==6:
            break
    return {"content":to_return}
    #ßeturn allPrices["Moririsons"][0:5]
    #return templates.TemplateResponse("prices_view.html", {"request":request, "allPrices":allPrices})

uvicorn.run(app, port=4444)
