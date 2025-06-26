from fastapi import FastAPI
from main import main_processing
import json

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/search/{product}")
def search(product:str):
    return main_processing(product)
    


@app.get("/trending")
def trending():
    with open('most_searched.json', 'r', encoding='utf8') as file:
        used_tokens = json.load(file)
    return used_tokens


