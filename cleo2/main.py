from fastapi import FastAPI, Request
from scrapers import morrisons_scraper
from fastapi.templating import Jinja2Templates
import uvicorn
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post('/get_prices')
async def get_prices(request:Request):
    myForm = await request.form()
    prices = morrisons_scraper.scrape_morrisons(myForm["productName"])
    print(prices)
    return templates.TemplateResponse("prices_view.html", {"request":request, "prices":prices})

uvicorn.run(app)
