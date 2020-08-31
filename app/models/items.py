from pydantic import BaseModel
from typing import Optional
import datetime


class Item(BaseModel):
    item_name: str
    quantity: float
    add_date: datetime.datetime
    remove_date: Optional[datetime.datetime] = None
    category: Optional[str] = None
    unit: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None


class User_Item(BaseModel):
    uid: Optional[str] = "0"
    item_name: str
    quantity: float
    add_date: datetime.datetime
    remove_date: Optional[datetime.datetime] = None
    category: Optional[str] = None
    unit: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None


class Reciept(BaseModel):
    store_name: Optional[str] = None
    date: datetime.date
    item_count: int
    total_amount: float
