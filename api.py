from fastapi import FastAPI
from main import main_processing
from database import get_most_searched

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
    return get_most_searched()


