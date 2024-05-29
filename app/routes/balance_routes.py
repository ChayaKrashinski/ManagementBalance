import uvicorn
from fastapi import APIRouter,HTTPException

from app.db_management.CRUD import *
from app.models.expenditure import Expenditure
from app.models.revenue import Revenue
from app.models.user import User
balance_router = APIRouter()


###revenues

@balance_router.post("/revenues")
async def add_revenue(revenue:Revenue):
    try:
        # בדיקת תקינות קלט
        # try:
        #     r = Revenue(**revenue)
        #     if await get_by_id('users', revenue.user)==None:
        #           raise Exception
        # except Exception as e:
        #     return f"The amount is incorrect {e}"
        res= await add('revenues', revenue)
        return res
    except Exception as e:
        return f"error: {e}"

@balance_router.put("/revenues")
async def update_revenue(id:int,revenue:Revenue):
    try:
        res = await update("revenues", id, revenue)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.delete("/revenues")
async def delete_revenue(id:int, user:int):
    try:
        r = await delete("revenues", user, id)
        r=(User(id=r.get('id'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return r
    except Exception as e:
        return f"error: {e}"

@balance_router.get("/revenues/get_all")
async def get_all_revenues(user_id:int):
    try:
        res=[]
        revenues = await get_all("revenues", user_id)
        for r in revenues:
            res.append(Revenue(id=r.get('id'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return res
    except Exception as e:
        return f"error: {e}"

@balance_router.get("/revenues")
async def get_revenue(id:int):
    try:
        return await get_by_id("revenues", id)
    except Exception as e:
        return f"error: {e}"


###
###expenses

@balance_router.post("/expenses")
async def add_expenditure(expenditure:Expenditure):
    try:
        # בדיקת תקינות קלט
        # try:
        #     r = Revenue(**revenue)
        #     if await get_by_id('users', revenue.user)==None:
        #           raise Exception
        # except Exception as e:
        #     return f"The amount is incorrect {e}"
        res= await add('revenues', expenditure)
        return res
    except Exception as e:
        return f"error: {e}"

@balance_router.put("/expenses")
async def update_expenditure(id:int,expenditure:Expenditure):
    try:
        res = await update("revenues", id, expenditure)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.delete("/expenses")
async def delete_expenditure(id:int, user:int):
    try:
        r = await delete("revenues", user, id)
        r=(Expenditure(id=r.get('id'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return r
    except Exception as e:
        return f"error: {e}"

@balance_router.get("/expenses/get_all")
async def get_all_expenditure(user_id:int):
    try:
        res=[]
        revenues = await get_all("revenues", user_id)
        for r in revenues:
            res.append(Expenditure(id=r.get('id'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return res
    except Exception as e:
        return f"error: {e}"

@balance_router.get("/expenses")
async def get_expenses(id:int):
    try:
        return await get_by_id("revenues", id)
    except Exception as e:
        return f"error: {e}"