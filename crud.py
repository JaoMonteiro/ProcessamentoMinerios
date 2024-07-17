from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import delete
import datetime, random, string
import models, schemas
from models import Sales


def gerarAleatorios():
    # Gera 3 numeros entre 10 e 150, um numero entre 0 e 1, e uma string aleatória.
    numeros = [random.randint(10, 150) for _ in range(2)]
    numero_entre_0_e_1 = random.random()
    caracteres = string.digits  # Usa apenas os dígitos de 0 a 9
    string_aleatoria = ''.join(random.choice(caracteres) for _ in range(1000))
    return numeros, numero_entre_0_e_1,string_aleatoria

# ORES

def getOres(db: Session):
    db.flush
    return db.query(models.Ores).all()


def getOreByID(db: Session, oreID: int):
    if(db.query(models.Ores).where(models.Ores.id == oreID).first()):
        return db.query(models.Ores).filter(models.Ores.id == oreID).first()
    else:
        raise HTTPException(status_code=404, detail="Ore not found")


def createOre(db: Session, newOre: schemas.OreCreate):
    
    if(db.query(models.Ores).where(models.Ores.name == newOre.name).first()):
        raise HTTPException(status_code=404, detail="Ore already exists.")
    else:
        dbOre = models.Ores(name=newOre.name,quantity=newOre.quantity,price=newOre.price,purity=newOre.purity)
        db.add(dbOre)
        db.commit()
        db.refresh(dbOre)
        return dbOre


def createAThousandOres(db: Session):
    
    i = 0
    while (i < 1000000):
        i+=1
        values,purity,name = gerarAleatorios()
        dbOre = models.Ores(name=name,quantity=values[0],price=values[1],purity=purity)
        db.add(dbOre)

    db.commit()
    return dbOre


def deleteOre(db: Session, oreID: schemas.OreDelete):

    query = delete(models.Ores).where(models.Ores.id == oreID)
    db.execute(query)
    db.commit()
    return {"message":"Ore successfully deleted."}


def updateOre(db: Session,newOre:schemas.Ore):

    ore = getOreByID(db=db,oreID=newOre.id)

    ore.name = newOre.name
    ore.price = newOre.price
    ore.quantity = newOre.quantity
    ore.purity = newOre.purity
    db.commit()
    
    return {"message":"Ore successfully updated."}


def addOre(db:Session, oreID:int,quantity:int):
    
    ore = getOreByID(db=db,oreID=oreID)

    ore.quantity += quantity
    db.commit()
    return {"message":"Ore successfully updated."}


# MATERIALS

def getMaterials(db: Session):
    return db.query(models.Materials).all()


def getMaterialByID(db: Session, materialID: int):
    return db.query(models.Materials).filter(models.Materials.id == materialID).first()


def createMaterial(db: Session, newMaterial: schemas.MaterialCreate):
    
    if(db.query(models.Materials).filter(models.Materials.name == newMaterial.name).first()):
        raise HTTPException(status_code=404, detail="Material already exists.")
    else:
        dbMaterial = models.Materials(name=newMaterial.name,quantity=newMaterial.quantity,composition= newMaterial.composition,price=newMaterial.price)
        db.add(dbMaterial)
        db.commit()
        db.refresh(dbMaterial)
        return dbMaterial
   

def deleteMaterial(db: Session, materialID: schemas.MaterialDelete):

    query = delete(models.Materials).where(models.Materials.id == materialID)
    db.execute(query)
    db.commit()
    return {"message":"Material successfully deleted."}


def updateMaterial(db: Session,newMaterial:schemas.Material):

    material = getMaterialByID(db=db, materialID= newMaterial.id)

    material.name = newMaterial.name
    material.description = newMaterial.description
    material.quantity = newMaterial.quantity
    material.price = newMaterial.price
    material.composition = newMaterial.composition
    db.commit()
    
    return {"message":"Material successfully updated."}


def makeMaterial(db:Session,oreID:int, quantity:int,materialID:int):

    ore = getOreByID(db=db,oreID=oreID)

    if(ore.quantity < quantity):
        raise HTTPException(status_code=412,detail="Not enough ore for the material.")
    else:
        ore.quantity -=quantity
        material = getMaterialByID(db=db, materialID=materialID)
        material.quantity += quantity
        db.commit()
        return {"message":"Material created with success."}


# SALES

def getSales(db: Session):
    return db.query(models.Sales).all()


def getSaleByID(db: Session, saleID: int):
    return db.query(models.Sales).filter(models.Sales.id == saleID).first()


def createSale(db: Session, newSale: schemas.SaleCreate):
    
    dbSales = models.Sales(value=newSale.value,data=newSale.data)
    db.add(dbSales)
    db.commit()
    db.refresh(dbSales)
    return dbSales


def deleteSale(db: Session, saleID: schemas.SaleDelete):

    query = delete(models.Sales).where(models.Sales.id == saleID)
    db.execute(query)
    db.commit()
    return {"message":"Sales successfully deleted."}


def updateSale(db: Session,newSale:schemas.Sale):

    sale = getSaleByID(db=db, saleID= newSale.id)

    sale.value = newSale.value
    sale.data = newSale.data
    db.commit()
    
    return {"message":"Sale successfully updated."}


# PRODUCTS

def getProducts(db: Session):
    return db.query(models.Products).all()


def getProductByID(db: Session, productID: int):
    return db.query(models.Products).filter(models.Products.id == productID).first()


def createProduct(db: Session, newProduct: schemas.ProductCreate):
    
    if(db.query(models.Products).filter(models.Products.name == newProduct.name).first()):
        raise HTTPException(status_code=404, detail="Product already exists.")
    else:
        dbProducts = models.Products(name=newProduct.name,quantity=newProduct.quantity,price=newProduct.price,materials= newProduct.materials)
        db.add(dbProducts)
        db.commit()
        db.refresh(dbProducts)
        return dbProducts
    

def deleteProduct(db: Session, productID: schemas.ProductDelete):

    query = delete(models.Products).where(models.Products.id == productID)
    db.execute(query)
    db.commit()
    return {"message":"Products successfully deleted."}


def updateProduct(db: Session,newProduct:schemas.Product):

    product = getProductByID(db=db, productID= newProduct.id)

    product.name = newProduct.name
    product.materials = newProduct.materials
    product.quantity = newProduct.quantity
    product.price = newProduct.price
    db.commit()
    
    return {"message":"Product successfully updated."}


def makeProduct(db:Session, quantity:float, productID:int):
    
    product =getProductByID(db=db,productID=productID)
    material = getMaterialByID(db=db, materialID=product.materials)

    if(material.quantity < quantity):
        raise HTTPException(status_code=412,detail="Not enough material for this product.")
    else:
        material.quantity -=quantity
        product.quantity += quantity

        value = quantity * material.price
        data = datetime.date.today()
        newSale = Sales(value=value,data=data)
        db.add(newSale)
        db.commit()
        return {"message":"Product made with success."}