from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import random
import uvicorn
app = FastAPI()

@app.get('/')
async def index():
    return {"success":"true", "content":f"{random.randint(1,999999)}"}


@app.post('/')
async def index_post(request:Request):
    message = await request.json()
    message = message["message"]
    return {"success":"true", "content":f"Your message reversed is : {message[::-1]}"}


app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

uvicorn.run(app)
