from fastapi import APIRouter, HTTPException
from app.services import visualization

visualization_router = APIRouter()


@visualization_router.get("/balance_data")
async def get_expense_and_revenue_by_date(user_id: str):
    """
    Retrieves expense and revenue data by date for a specific user.

    Method: GET
    Route: /balance_data

    Parameters:
    - user_id (str): The ID of the user for whom the data is to be retrieved.

    Raises:
    - HTTPException: If an error occurs during the retrieval process, an HTTPException with status code 500 is raised, providing details of the error.
    """

    try:
        await visualization.show_expense_and_revenue_by_date(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get("/balance_of_all_users")
async def balance_of_all_users():
    """
    Retrieves balance data for all users.

    Method: GET
    Route: /balance_of_all_users

    Raises:
    - HTTPException: If an error occurs during the retrieval process, an HTTPException with status code 500 is raised, providing details of the error.
    """

    try:
        await visualization.get_users_expenses()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
