from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


# Schemas for Menu Model
class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):
    pass


class MenuOut(MenuBase):
    id: int

    class Config:
        from_attributes = True


# Schemas for SubMenu model
class SubMenuBase(BaseModel):
    name: str
    menu_id: int


class SubMenuCreate(SubMenuBase):
    pass


class SubMenuUpdate(SubMenuBase):
    pass


class SubMenuOut(SubMenuBase):
    id: int

    class Config:
        orm_mode = True


# Schemas for DishModel
class DishBase(BaseModel):
    name: str
    price: float
    description: str
    submenu_id: int


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    pass


class DishOut(DishBase):
    id: int

    class Config:
        orm_mode = True


# Schemas for response models
class MenuListOut(BaseModel):
    items: List[MenuOut]


class SubMenuListOut(BaseModel):
    items: List[SubMenuOut]


class DishListOut(BaseModel):
    items: List[DishOut]