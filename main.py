from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud,models,schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Go to /docs to see functionalities"}

# ORES

@app.get("/ore/all",response_model=list[schemas.Ore])
async def getOres(db: Session = Depends(get_db)):
    ores = crud.getOres(db=db)
    return ores

@app.put("/ore/all")
async def createAThousandOres(db: Session = Depends(get_db)):
    crud.createAThousandOres(db=db)
    return {"message":"Ores created with sucess."}

@app.get("/ore/{oreID}",response_model=schemas.Ore)
async def getSingleOre(oreID:int, db: Session = Depends(get_db)):
    ore = crud.getOreByID(db=db, oreID=oreID)
    return ore

@app.post("/ore/")
def createOre(ore: schemas.Ore, db: Session = Depends(get_db)):
    return crud.createOre(db=db, newOre=ore)

@app.delete("/ore/{oreID}")
async def deleteOre(oreID:int, db: Session = Depends(get_db)):
    crud.deleteOre(db,oreID=oreID)
    return {"message":"Successfully deleted ore."}

@app.put("/ore/")
def updateOre(ore: schemas.Ore, db: Session = Depends(get_db)):
    return crud.updateOre(db=db, newOre=ore)

@app.put("/ore/add/{oreID}/{quantity}")
def addOre(oreID: int, quantity:float, db: Session = Depends(get_db)):
    return crud.addOre(db=db, oreID=oreID,quantity=quantity)

# MATERIALS

@app.get("/material/all",response_model=list[schemas.Material])
async def getMaterials(db: Session = Depends(get_db)):
    materials = crud.getMaterials(db=db)
    return materials

@app.get("/material/{materialID}",response_model=schemas.Material)
async def getSingleMaterial(materialID:int, db: Session = Depends(get_db)):
    material = crud.getMaterialByID(db=db, materialID=materialID)
    return material

@app.post("/material/")
def createMaterial(material: schemas.Material, db: Session = Depends(get_db)):
    dbMaterial = crud.getMaterialByID(db, material.id)
    if dbMaterial:
        raise HTTPException(status_code=400, detail="Material already registered")
    return crud.createMaterial(db=db, newMaterial=material)

@app.delete("/material/{materialID}")
async def deleteMaterial(materialID:int, db: Session = Depends(get_db)):
    crud.deleteMaterial(db,materialID=materialID)
    return {"message":"Successfully deleted material."}

@app.put("/material/")
def updateOre(material: schemas.Material, db: Session = Depends(get_db)):
    return crud.updateMaterial(db=db, newMaterial=material)

@app.put("/material/create/{materialID}/{oreID}/{quantity}")
def makeMaterial(oreID: int,materialID:int, quantity:float, db: Session = Depends(get_db)):
    return crud.makeMaterial(db=db, oreID=oreID,quantity=quantity,materialID=materialID)

# SALES

@app.get("/sales/all",response_model=list[schemas.Sale])
async def getSales(db: Session = Depends(get_db)):
    sales = crud.getSales(db=db)
    return sales

@app.get("/sales/{salesID}",response_model=schemas.Sale)
async def getSingleSale(salesID:int, db: Session = Depends(get_db)):
    sale = crud.getSaleByID(db=db, saleID=salesID)
    return sale

@app.post("/sales/")
def createSale(sales: schemas.Sale, db: Session = Depends(get_db)):
    dbSale = crud.getSaleByID(db, sales.id)
    if dbSale:
        raise HTTPException(status_code=400, detail="Sale already registered")
    return crud.createSale(db=db, newSale=sales)

@app.delete("/sales/{salesID}")
async def deleteSale(salesID:int, db: Session = Depends(get_db)):
    crud.deleteSale(db,saleID=salesID)
    return {"message":"Successfully deleted sale."}

@app.put("/sales/")
def updateSale(sale: schemas.Sale, db: Session = Depends(get_db)):
    return crud.updateSale(db=db, newSale=sale)

# PRODUCTS

@app.get("/products/all",response_model=list[schemas.Product])
async def getProducts(db: Session = Depends(get_db)):
    products = crud.getProducts(db=db)
    return products

@app.get("/products/{productsID}",response_model=schemas.Product)
async def getSingleProduct(productsID:int, db: Session = Depends(get_db)):
    product = crud.getProductByID(db=db, productID=productsID)
    return product

@app.post("/products/", response_model=schemas.Product)
def createProduct(products: schemas.Product, db: Session = Depends(get_db)):
    dbProduct= crud.getProductByID(db, products.id)
    if dbProduct:
        raise HTTPException(status_code=400, detail="Product already registered")
    return crud.createProduct(db=db, newProduct=products)

@app.delete("/products/{productsID}")
async def deleteProduct(productsID:int, db: Session = Depends(get_db)):
    crud.deleteProduct(db,productID=productsID)
    return {"message":"Successfully deleted product."}

@app.put("/products/")
def updateProduct(product: schemas.Product, db: Session = Depends(get_db)):
    return crud.updateProduct(db=db, newProduct=product)

@app.put("/products/create/{productID}/{quantity}")
def makeProduct(productID:int, quantity:float, db: Session = Depends(get_db)):
    return crud.makeProduct(db=db, quantity=quantity,productID=productID)