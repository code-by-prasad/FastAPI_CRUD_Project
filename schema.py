from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models import Category, UnitOfMeasure
class Product(BaseModel):
    pid: int
    name: str
    description: str
    category: Category
    product_image: str
    sku: str
    units: UnitOfMeasure
    lead_time: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {
        "from_attributes": True
    }
    
class ProductPut(BaseModel):
    name: Optional[str] = None
    category: Optional[Category] = None
    description : Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    units: Optional[UnitOfMeasure] = None
    lead_time: Optional[int] = None
    

class ProductResponse(Product):
    pass

