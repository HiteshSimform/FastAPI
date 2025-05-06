from sqlalchemy.orm import Session
import models, schemas
from fastapi import FastAPI, HTTPException

# def get_items(db: Session, skip: int = 0, limit: int=100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


def get_items(db: Session):
    return db.query(models.Item).all()


def get_items_id(item_id: int, db: Session):
    db_item = db.query(models.Item).filter(models.Item.id == item_id)
    return db_item


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted Successfully"}


def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name:
        db_item.name = item.name
    if item.price is not None:
        db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item
