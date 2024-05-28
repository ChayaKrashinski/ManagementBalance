import uvicorn
from fastapi import APIRouter,HTTPException

from app.models.user import User
from app.db_management.user_CRUD import find_user
user_router = APIRouter()

@user_router.put("/register/")
async def register(user: User):
    return "hello you! "+user.name

@user_router.post("/my_user")
async def my_user(name:str, password:str):
    find_user(password, name)
    return "ok"
    # try:
    #     user = findUser(name, password)
    #     if(user!=None):
    #         return user
    # except:
    #     return "user not found"