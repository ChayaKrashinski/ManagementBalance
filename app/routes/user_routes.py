import uvicorn
from fastapi import APIRouter, HTTPException

from app.db_management.CRUD import *
from app.models.user import User

user_router = APIRouter()
user_id = 0


@user_router.post("/register")
async def register(user: User):
    """
    Registers a new user in the system.

    Method: POST
    Route: /register

    Parameters:
    - user (User): The user object to be registered.

    Returns:
    - dict: The registered user details.

    Raises:
    - HTTPException: If an error occurs during the registration process, an HTTPException with status code 500 is raised.
    """

    try:
        res = await add('users', user)
        return res
    except Exception as e:
        return {'error': e}


@user_router.get("/login")
async def my_user(user: User):
    """
    Retrieves user information based on provided credentials.

    Method: GET
    Route: /login

    Parameters:
    - user (User): The user object containing login credentials.

    Returns:
    - dict: The user details upon successful login.

    Raises:
    - HTTPException: If an error occurs during the login process, an HTTPException with status code 500 is raised.
    """

    try:
        ret = await get_one('users', user)
        print("/routes")
        ret = User(id=ret.get('id'), name=ret.get('name'), password=ret.get('password'), mail=ret.get('mail'))
        user_id = ret.id
        return ret
    except Exception as e:
        print("/routes error:")
        print(e)
        return {'error': e}


@user_router.put("/")
async def update_user(id: int, user: User):
    """
    Updates an existing user's information.

    Method: PUT
    Route: /

    Parameters:
    - id (int): The ID of the user to be updated.
    - user (User): The updated user object.

    Returns:
    - dict: The updated user details.

    Raises:
    - HTTPException: If an error occurs during the update process, an HTTPException with status code 500 is raised.
    """

    try:
        res = await update("users", id, user)
        return res
    except Exception as e:
        print(e)
        return {'messege': 'router error', 'error': e}


@user_router.get("/get_all")
async def all_users():
    """
    Retrieves information about all users in the system.

    Method: GET
    Route: /get_all

    Returns:
    - list: A list of user details for all users in the system.

    Raises:
    - HTTPException: If no users are found or if an error occurs during the retrieval process, an HTTPException with status code 500 is raised.
    """

    try:
        res = []
        users = await get_all_collection("users")
        for u in users:
            res.append(User(id=u.get('id'), name=u.get('name'), password=u.get('password'), mail=u.get('mail')))
        return res
    except Exception as e:
        return {'messege': 'users not found', 'error': e}
