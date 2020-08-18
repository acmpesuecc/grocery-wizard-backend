from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[int] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{username}", response_model=User)
async def read_user(username: str):
    return {"id":username}
