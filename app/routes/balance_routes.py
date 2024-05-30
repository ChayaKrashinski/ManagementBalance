import uvicorn
from fastapi import APIRouter, HTTPException

from app.db_management.CRUD import *
from app.models.expenditure import Expenditure
from app.models.revenue import Revenue
from app.models.user import User

balance_router = APIRouter()


###revenues

@balance_router.post("/revenues")
async def add_revenue(revenue: Revenue):
    try:
        """
        Adds a new revenue entry to the system.

        Method: POST
        Route: /revenues

        Parameters:
        - revenue (Revenue): The revenue object to be added.

        Returns:
        - The added revenue entry.

        Raises:
        - HTTPException with status code 500 if an error occurs during the addition process.
        """
        res = await add('revenues', revenue)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.put("/revenues")

async def update_revenue(id: int, revenue: Revenue):
    """
      Updates an existing revenue entry in the system.

      Method: PUT
      Route: /revenues

      Parameters:
      - id (int): The ID of the revenue entry to be updated.
      - revenue (Revenue): The updated revenue object.

      Returns:
      - The updated revenue entry.

      Raises:
      - HTTPException with status code 500 if an error occurs during the update process.
      """
    try:
        res = await update("revenues", id, revenue)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.delete("/revenues")
async def delete_revenue(id: int, user: int):
    """
    Deletes a specific revenue entry from the system.

    Method: DELETE
    Route: /revenues

    Parameters:
    - id (int): The ID of the revenue entry to be deleted.
    - user (int): The ID of the user who owns the revenue entry.

    Returns:
    - The deleted revenue entry.

    Raises:
    - HTTPException with status code 500 if an error occurs during the deletion process.
    """
    try:
        r = await delete("revenues", user, id)
        r = (Revenue(id=r.get('id'), user=r.get('user'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return r
    except Exception as e:
        return f"error: {e}"


@balance_router.get("/revenues/get_all")
async def get_all_revenues(user_id: int):
    """
    Retrieves all revenue entries associated with a specific user.

    Method: GET
    Route: /revenues/get_all

    Parameters:
    - user_id (int): The ID of the user whose revenue entries are to be retrieved.

    Returns:
    - A list of revenue entries associated with the specified user.

    Raises:
    - HTTPException with status code 500 if an error occurs during the retrieval process.
    """
    try:
        res = []
        revenues = await get_all("revenues", user_id)
        for r in revenues:
            res.append(Revenue(id=r.get('id'), user=r.get('user'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return res
    except Exception as e:
        return f"error: {e}"

#

@balance_router.get("/revenues")
async def get_revenue(id: int):
    """
       Retrieves a specific revenue entry by its ID.

       Method: GET
       Route: /revenues

       Parameters:
       - id (int): The ID of the revenue entry to be retrieved.

       Returns:
       - The revenue entry with the specified ID.

       Raises:
       - HTTPException with status code 500 if an error occurs during the retrieval process.
       """
    try:
        return await get_by_id("revenues", id)
    except Exception as e:
        return f"error: {e}"


###
###expenses

@balance_router.post("/expenses")
async def add_expenditure(expenditure: Expenditure):
    try:
        """
        Adds a new expenditure entry to the system.

        Method: POST
        Route: /expenses

        Parameters:
        - expenditure (Expenditure): The expenditure object to be added.

        Returns:
        - The added expenditure entry.

        Raises:
        - HTTPException with status code 500 if an error occurs during the addition process.
        """
        res = await add('expenditure', expenditure)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.put("/expenses")
async def update_expenditure(id: int, expenditure: Expenditure):
    """
      Updates an existing expenditure entry in the system.

      Method: PUT
      Route: /expenses

      Parameters:
      - id (int): The ID of the expenditure entry to be updated.
      - expenditure (Expenditure): The updated expenditure object.

      Returns:
      - The updated expenditure entry.

      Raises:
      - HTTPException with status code 500 if an error occurs during the update process.
      """
    try:
        res = await update("expenses", id, expenditure)
        return res
    except Exception as e:
        return f"error: {e}"


@balance_router.delete("/expenses")
async def delete_expenditure(id: int, user: int):
    """
       Deletes a specific expenditure entry from the system.

       Method: DELETE
       Route: /expenses

       Parameters:
       - id (int): The ID of the expenditure entry to be deleted.
       - user (int): The ID of the user who owns the expenditure entry.

       Returns:
       - The deleted expenditure entry.

       Raises:
       - HTTPException with status code 500 if an error occurs during the deletion process.
       """
    try:
        r = await delete("expenses", user, id)
        r = (Expenditure(id=r.get('id'), user=r.get('user'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return r
    except Exception as e:
        return f"error: {e}"


@balance_router.get("/expenses/get_all")
async def get_all_expenditure(user_id: int):
    """
    Retrieves all expenditure entries associated with a specific user.

    Method: GET
    Route: /expenses/get_all

    Parameters:
    - user_id (int): The ID of the user whose expenditure entries are to be retrieved.

    Returns:
    - list: A list of expenditure entries associated with the specified user.

    Raises:
    - HTTPException: If an error occurs during the retrieval process, an HTTPException with status code 500 is raised.
    """

    try:
        res = []
        revenues = await get_all("expenditure", user_id)
        for r in revenues:
            res.append(Expenditure(id=r.get('id'), user=r.get('user'), sum=r.get('sum'), date=r.get('date'), details=r.get('details')))
        return res
    except Exception as e:
        return f"error: {e}"




@balance_router.get("/expenses")
async def get_expenses(id: int):
    """
    Retrieves a specific expenditure entry by its ID.

    Method: GET
    Route: /expenses

    Parameters:
    - id (int): The ID of the expenditure entry to be retrieved.

    Returns:
    - dict: The expenditure entry with the specified ID.

    Raises:
    - HTTPException: If an error occurs during the retrieval process, an HTTPException with status code 500 is raised.
    """

    try:
        return await get_by_id("expenses", id)
    except Exception as e:
        return f"error: {e}"
