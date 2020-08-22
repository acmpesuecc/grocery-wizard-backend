from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional


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

class Item(BaseModel):
    name: str
    quantity: float
    unit: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None


from firebase_admin import auth
default_app = firebase_admin.initialize_app(cred)
print(default_app.name)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{username}")
async def read_user(username: str):
    return {"id":username}

@app.post("/users")
async def create_user(user:User, user_id: str = Header(None)):
    user_dict = user.dict()
    return user_id
