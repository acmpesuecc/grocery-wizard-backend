from pydantic import BaseModel
from typing import Optional
import datetime


class Item(BaseModel):
    item_name: str
    quantity: float
    category: Optional[str] = None
    unit: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None

class Reciept(BaseModel):
    store_name: Optional[str] = None
    date: datetime.date
    item_count: int
    total_amount: float
