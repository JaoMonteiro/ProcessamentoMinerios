from sqlalchemy import Double, Column, ForeignKey, Integer, String,DateTime

from database import Base

class Ores(Base):
    __tablename__ = "ores"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Double)
    price = Column(Double)
    purity = Column(Double)
    class Config:
        orm_mode = True

class Materials(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Double)
    price = Column(Double)
    composition = Column(Integer, ForeignKey("ores.id"),nullable=False)
    class Config:
        orm_mode = True

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    value = Column(Double)
    data = Column(DateTime)
    class Config:
        orm_mode = True

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Double)
    price = Column(Double)
    materials = Column(Integer, ForeignKey("materials.id"))
    class Config:
        orm_mode = True