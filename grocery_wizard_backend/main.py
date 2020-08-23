from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional
import firebase_admin
from firebase_admin import credentials, auth


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
    item_name: str
    quantity: float
    category: Optional[str] = None
    unit: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None



cred = credentials.Certificate("./admin/grocery-wizard-firebase-adminsdk-95r53-9c32d80748.json")
firebase_admin.initialize_app(cred)
print(firebase_admin.auth.list_users())

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
