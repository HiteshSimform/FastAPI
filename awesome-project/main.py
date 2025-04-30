# print("Hello World")
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool=None

@app.get('/')
def read_root():
    return {"message":"Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/{name}")
async def read_item(name,price):
    return {"name": name,"price":price}

@app.get("/blog/{name}")
async def blog(name):
    return {"Blog Name":{name}}

@app.post("/items/")
async def create_item(item: Item):
    return item

# 127.0.0.1:8000/items/1?item_name=orange&item_price=20


@app.get("/search/")
def search_items(q: str = None, page: int = 1):
    return {"query": q, "page": page}


class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users/create")
def create_user(user: User, send_email: bool = Query(default=False)):
    return {
        "user_data": user,
        "send_email": send_email
    }