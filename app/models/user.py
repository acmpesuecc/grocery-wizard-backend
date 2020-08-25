from pydantic import BaseModel
from typing import Optional
import datetime


class User(BaseModel):
    id: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[int] = None
    address: Optional[int] = None
    city: Optional[int] = None
    state: Optional[int] = None
    pincode: Optional[int] = None
    country: Optional[int] = None
