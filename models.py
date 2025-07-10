from sqlalchemy import BIGINT, TIMESTAMP, String, Column, Integer, func
from database import Base
from sqlalchemy import Enum as SqlEnum
from enum import Enum

class Category(Enum):
    finished = 'finished'
    semiFinished = 'semi-finished'
    raw = 'raw'

class UnitOfMeasure(Enum):
    mtr = 'mtr'
    mm = 'mm'
    ltr = 'ltr'
    ml = 'ml'
    cm = 'cm'
    mg = 'mg'
    gm = 'gm'
    unit = 'unit'
    pack = 'pack'

class Product(Base):
    __tablename__ = 'product'

    pid = Column(BIGINT, primary_key=True, index=True)
    name = Column(String(100))
    def get_cat_values(enum_class):
        return [member.value for member in enum_class]
    category = Column(SqlEnum(Category, values_callable=get_cat_values), nullable=False)
    description = Column(String(250))
    product_image = Column(String(100))
    sku = Column(String(100))
    def get_unit_values(enum_class):
        return [member.value for member in enum_class]
    units = Column(SqlEnum(UnitOfMeasure, values_callable=get_unit_values), nullable=False)
    lead_time = Column(Integer)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())