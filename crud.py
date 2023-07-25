from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List
from decimal import Decimal
import models
from models import Menu, SubMenu, Dish
from schemas import MenuCreate, SubMenuCreate, DishCreate, MenuUpdate, SubMenuUpdate, DishUpdate, MenuOut, SubMenuOut, DishOut


# Helper function to round decimal number to 2 decimal places
def round_decimal(value: float) -> float:
    return round(Decimal(value), 2)


# CRUD Operation for Menu model
def get_menus(db: Session, skip: int = 0, limit: int = 100) -> List[MenuOut]:
    return db.query(Menu).offset(skip).limit(limit).all()

