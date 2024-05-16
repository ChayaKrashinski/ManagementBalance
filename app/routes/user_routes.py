import uvicorn
from fastapi import APIRouter,HTTPException

from app.models.user import User

user_router = APIRouter()

@user_router.post("/register/")
async def register(user: User):
    return "hello you! "+user.name

@user_router.get("/**")
async def default():
    return "page 404"