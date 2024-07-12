import datetime
from pydantic import BaseModel,Field

class Ore(BaseModel):
    id:int  | None = None
    name:str
    quantity: float
    price: float = Field(gt=0, description="The price must be greater than zero")
    purity: float

class OreCreate(Ore):
    pass

class OreDelete(Ore):
    pass

class OreUpdate(Ore):
    pass


class Material(BaseModel):
    id:int  | None = None
    name:str
    description: str | None = None
    quantity:float
    price:float
    composition:int

class MaterialCreate(Material):
    pass

class MaterialDelete(Material):
    pass

class MaterialUpdate(Material):
    pass


class Sale(BaseModel):
    id:int  | None = None
    value:float
    data:str

class SaleCreate(Sale):
    pass

class SaleDelete(Sale):
    pass

class SaleUpdate(Sale):
    pass


class Product(BaseModel):
    id:int  | None = None
    name:str
    materials:int
    quantity:float
    price: float = Field(gt=0, description="The price must be greater than zero")

class ProductCreate(Product):
    pass

class ProductDelete(Product):
    pass

class ProductUpdate(Product):
    pass
