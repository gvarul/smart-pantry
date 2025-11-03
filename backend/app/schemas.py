from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class UserCreate(BaseModel):
    email: str
    full_name: Optional[str]

class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    quantity: float
    unit: Optional[str] = "pcs"
    category: Optional[str] = None
    purchase_date: Optional[date] = None
    expiry_date: Optional[date] = None
    barcode: Optional[str] = None
    threshold: Optional[float] = 1.0

class ItemCreate(ItemBase):
    user_id: int

class ItemOut(ItemBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class UsageCreate(BaseModel):
    item_id: int
    used_quantity: float
    remarks: Optional[str] = None

class UsageOut(BaseModel):
    id: int
    item_id: int
    used_quantity: float
    used_date: datetime
    remarks: Optional[str]
    class Config:
        orm_mode = True

class ShoppingOut(BaseModel):
    id: int
    item_id: int
    is_purchased: bool
    quantity: Optional[float]
    class Config:
        orm_mode = True
