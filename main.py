import json
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database import engine, SessionLocal
import models
from models import Menu, SubMenu, Dish
from schemas import MenuCreate, SubMenuCreate, DishCreate, MenuUpdate, SubMenuUpdate, DishUpdate, MenuOut, SubMenuOut, DishOut
from crud import get_menus

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/api/v1/menus", response_model=List[MenuOut])
def read_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menus = get_menus(db, skip=skip, limit=limit)
    return menus


@app.post("/api/v1/menus", response_model=MenuOut, status_code=201)
def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = Menu(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


@app.get("/api/v1/menus/{target_menu_id}", response_model=MenuOut)
def read_menu(target_menu_id: int, db: Session = Depends(get_db)):
    menu = db.query(Menu).filter(Menu.id == target_menu_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail=f'Menu with id {target_menu_id} not found')
    return menu


@app.post("/api/v1/menus/{target_menu_id}", response_model=MenuOut, status_code=200)
def update_menu(target_menu_id: int, menu: MenuUpdate, db: Session = Depends(get_db)):
    db_menu = db.query(Menu).filter(Menu.id == target_menu_id).first()

    if not db_menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    db_menu.title = menu.title
    db_menu.description = menu.description

    db.commit()
    db.refresh(db_menu)

    return db_menu


@app.delete("/api/v1/menus/{target_menu_id}", status_code=204)
def delete_menu(target_menu_id: int, db: Session = Depends(get_db)):
    db_menu = db.query(Menu).filter(Menu.id == target_menu_id).first()

    if not db_menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    db.delete(db_menu)
    db.commit()

    return None


# @app.post("/api/v1/menus", response_model=MenuOut)
# def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
#     db_menu = Menu(name=menu.name, description=menu.description)