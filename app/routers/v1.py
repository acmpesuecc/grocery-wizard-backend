from fastapi import APIRouter, HTTPException, Header

import motor.motor_asyncio
from bson.objectid import ObjectId

from models.user import User
from models.items import Item,Reciept

from auth.firebaseauth import verify


router = APIRouter()


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:gwpassword@gw-db-1.vbttl.azure.mongodb.net/?retryWrites=true&w=majority")

gwdb = client.gwdb


@router.get("/")
async def api_version():
    return "API V1"


@router.get("/users/{username}")
async def read_user(username: str):
    return {"id":username}


@router.post("/users")
async def create_user(user:User, id_token: str = Header(None)):
    if id_token:
        uid = verify(id_token)
    else:
        raise HTTPException(status_code=403, detail="Forbidden. Provide ID Token.")

    print(uid)
    user_dict = user.dict()
    return user_id


@router.post("/items")
async def add_item(item:Item, id_token: str = Header(None)):
    if id_token:
        uid = verify(id_token)
    else:
        raise HTTPException(status_code=403, detail="Forbidden. Provide ID Token.")

    item_dict = item.dict()
    item_dict['uid'] = uid
    result = await gwdb.items.insert_one(item_dict)
    return {"inserted_id":str(result.inserted_id)}
