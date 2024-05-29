import uvicorn
from fastapi import APIRouter,HTTPException

from app.db_management.user_CRUD import *
from app.models.user import User
user_router = APIRouter()

@user_router.post("/register")
async def register(user: User):
    try:
        res= await add('users', user)
        return  res
    except Exception as e:
        return {'error': e}


@user_router.post("/login")
async def my_user(user:User):
    try:
        ret = await get_one('users',user)
        print("/routes")
        ret = User(name=ret.get('name'), password=ret.get('password'), mail=ret.get('mail'))
        return ret
    except Exception as e:
        print("/routes error:")
        print(e)
        return{'error':e}


# @user_router.post("/login")
# async def my_user(name:str, password:str):
#     try:
#         res = await get_one("users",{'password':password,"name": name})
#         return res
#     except Exception as e:
#         return {'messege':'user not found','error': e}