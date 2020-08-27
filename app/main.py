from fastapi import FastAPI, Header, HTTPException

from models.user import User
from models.items import Item,Reciept

from auth import verify

from routers import v1

app = FastAPI()


app.include_router(
    v1.router,
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)


@app.get("/")
async def root():
    return {"message": "Hello World! If you are seeing this message, the server probably works"}

@app.get("/version")
async def current_version():
    return "v1"
