from fastapi import FastAPI, Header
import firebase_admin
from firebase_admin import credentials, auth
from models.user import User
from models.items import Item,Reciept


cred = credentials.Certificate("../grocery-wizard-firebase-adminsdk-95r53-9c32d80748.json")
firebase_admin.initialize_app(cred)
print(firebase_admin.auth.list_users())

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! If you are seeing this message, the server probably works"}

@app.get("/users/{username}")
async def read_user(username: str):
    return {"id":username}

@app.post("/users")
async def create_user(user:User, user_id: str = Header(None)):
    user_dict = user.dict()
    return user_id
