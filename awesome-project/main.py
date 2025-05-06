# print("Hello World")
from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI()


# class Item(BaseModel):
#     id: int
#     name: str
#     price: float
#     # is_offer: bool = None


# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


# items = []


# @app.get("/items", response_model=List[Item])
# async def read_items():
#     return items


# @app.post("/items", response_model=Item)
# async def create_item(item: Item):
#     items.append(item)
#     return item


# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: Item):
#     items[item_id] = item
#     return item


# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"message": "Item deleted"}


# print(items)

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# @app.get("/items/{name}")
# async def read_item(name, price):
#     return {"name": name, "price": price}


# @app.get("/blog/{name}")
# async def blog(name):
#     return {"Blog Name": {name}}


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# # 127.0.0.1:8000/items/1?item_name=orange&item_price=20


# @app.get("/search/")
# def search_items(q: str = None, page: int = 1):
#     return {"query": q, "page": page}


# class User(BaseModel):
#     name: str
#     email: str
#     age: int


# @app.post("/users/create")
# def create_user(user: User, send_email: bool = Query(default=False)):
#     return {"user_data": user, "send_email": send_email}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=dict)
def read_root():
    return {"message": "Hello World"}


# @app.get("/items", response_model=list[schemas.Item])
# async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


@app.get("/items", response_model=list[schemas.Item])
async def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items


@app.get("/items/{item_id}", response_model=list[schemas.Item])
async def read_items(item_id: int, db: Session = Depends(get_db)):
    items = crud.get_items_id(item_id, db)
    return items


@app.post("/items", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(
    item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)
):
    return crud.update_item(item_id=item_id, item=item, db=db)


@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(item_id=item_id, db=db)
