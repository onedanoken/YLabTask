import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    description = Column(String(50))
    submenu = relationship("SubMenu", back_populates="menu", cascade="all, delete")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    submenu_id = Column(Integer, ForeignKey("submenus.id"))
    submenu = relationship("SubMenu", back_populates="dishes")


class SubMenu(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"))
    menu = relationship("Menu", back_populates="submenu")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete")
