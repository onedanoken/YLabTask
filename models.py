from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(50))
    submenus = relationship("submenu", back_populates="menu", cascade="all, delete")


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))
    submenu = relationship("SubMenu", back_populates="dishes")


class SubMenu(Base):
    __tablename__ = "submenu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    menu_id = Column(Integer, ForeignKey("menu.id"))
    menu = relationship("Menu", back_populates="submenu")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete")
