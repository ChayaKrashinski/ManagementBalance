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


@user_router.get("/login")
async def my_user(user:User):
    try:
        ret = await get_one('users',user)
        print("/routes")
        ret = User(id=ret.get('id'),name=ret.get('name'), password=ret.get('password'), mail=ret.get('mail'))
        return ret
    except Exception as e:
        print("/routes error:")
        print(e)
        return{'error':e}


@user_router.put("/")
async def update_user(id:int,user:User):
    try:
        res = await update("users", id, user)
        return res
    except Exception as e:
        print(e)
        return {'messege':'router error','error': e}


@user_router.get("/get_all")
async def all_users():
    try:
        res=[]
        users = await get_all_connection("users")
        for u in users:
            res.append(User(id=u.get('id'),name=u.get('name'), password=u.get('password'), mail=u.get('mail')))
        return res
    except Exception as e:
        return {'messege':'users not found','error': e}