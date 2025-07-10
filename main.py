from fastapi import Depends, FastAPI, HTTPException, status
import models, schema
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=List[schema.ProductResponse])
def get_product_list(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.post("/product/add", response_model=schema.ProductResponse, status_code=status.HTTP_201_CREATED)
def add_product(product: schema.Product, db: Session = Depends(get_db)):
    product_add = models.Product(**product.model_dump())
    db.add(product_add)
    db.commit()
    db.refresh(product_add)
    return product_add

@app.get("/product/{pid}/info", response_model=schema.ProductResponse)
def get_product(pid:int, db: Session = Depends(get_db)):
    product_one = db.query(models.Product).filter(models.Product.pid==pid).first()
    if not product_one:
        raise HTTPException(status_code=404, detail=f"Product with ID {pid} not found")
    return product_one

@app.put("/product/{pid}/update", response_model=schema.ProductPut)
def update_product(pid: int, product_data: schema.ProductPut, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.pid == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    
    db.commit()
    db.refresh(product)
    return product
