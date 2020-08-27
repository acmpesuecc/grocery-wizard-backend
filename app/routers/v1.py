from fastapi import APIRouter, HTTPException, Header

router = APIRouter()


@router.get("/")
async def read_items():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]


@router.get("/users/{username}")
async def read_user(username: str):
    return {"id":username}


@router.post("/users")
async def create_user(id_token: str = Header(None)):
    if id_token:
        uid = verify(id_token)
        if uid == -1:
            raise HTTPException(status_code=403, detail="Forbidden. The ID Token is invalid.")
    else:
        raise HTTPException(status_code=403, detail="Forbidden. Provide ID Token.")
    print(uid)
    user_dict = user.dict()
    return user_id
