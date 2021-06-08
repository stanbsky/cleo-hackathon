from fastapi import FastAPI, Request
from scrapers import morrisons_scraper, aldi_scraper
from fastapi.templating import Jinja2Templates
import uvicorn
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post('/get_prices')
async def get_prices(request:Request):
    allPrices = {}

    myForm = await request.form()
    MorrisonsPrices = morrisons_scraper.scrape_morrisons(myForm["productName"])
    AldisPrices = aldi_scraper.scrape_aldi(myForm["productName"])
    allPrices["Morrisons"] = MorrisonsPrices
    allPrices["Aldi"] = AldisPrices
    print(allPrices)
    return templates.TemplateResponse("prices_view.html", {"request":request, "allPrices":allPrices})

uvicorn.run(app)
