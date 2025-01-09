from typing import List
from enum import StrEnum
from pydantic import BaseModel, Field


class Status(StrEnum):
    CREATED = 'created'
    PAID = 'paid'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'


class Product(BaseModel):
    id: int
    quantity: int = Field(gt=0)


class OrderIn(BaseModel):
    products: List[Product]
    


class OrderOut(BaseModel):
    id: int
    status: str = Status.CREATED