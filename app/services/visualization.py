import matplotlib.pyplot as plt
from starlette.responses import StreamingResponse
import io

from app.db_management import CRUD
from app.models.expenditure import Expenditure
from app.models.revenue import Revenue


async def get_expenses(user_id: int):
    """
    Retrieves expenses for a given user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of Expenditure objects representing the expenses.
    """
    try:
        res = []
        expenses = await CRUD.get_all("expenses", user_id)
        for r in expenses:
            res.append(Expenditure(
                id=r.get('id'),
                user=r.get('user'),
                sum=r.get('sum'),
                date=r.get('date'),
                details=r.get('details')
            ))
        return res
    except Exception as e:
        return f"error: {e}"


async def get_revenues(user_id: int):
    """
    Retrieves revenues for a given user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of Revenue objects representing the revenues.
    """
    try:
        res = []
        revenues = await CRUD.get_all("revenues", user_id)
        for r in revenues:
            res.append(Revenue(
                id=r.get('id'),
                user=r.get('user'),
                sum=r.get('sum'),
                date=r.get('date'),
                details=r.get('details')
            ))
        return res
    except Exception as e:
        return f"error: {e}"


async def show_expense_and_revenue_by_date(user_id: str):
    """
    Displays expenses and revenues over time for a given user ID.

    Args:
        user_id (str): The ID of the user.
    """
    try:
        expenses = await get_expenses(user_id)
        revenues = await get_revenues(user_id)
        expenses = sorted(expenses, key=lambda expense: expense.date)

        expense_dates = [expense.date for expense in expenses]
        expense_amounts = [expense.sum for expense in expenses]

        revenues = sorted(revenues, key=lambda revenue: revenue.date)
        revenue_dates = [revenue.date for revenue in revenues]
        revenue_amounts = [revenue.sum for revenue in revenues]

        plt.figure(figsize=(10, 6))
        plt.plot(expense_dates, expense_amounts, 'o', label='Expenses')
        plt.plot(revenue_dates, revenue_amounts, '*', label='Revenues')
        plt.xlabel('Date')
        plt.ylabel('Sum')
        plt.title(f'Revenues & Expenses for User ID = {user_id}')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        raise e


async def get_users_expenses():
    """
    Retrieves users' expenses and generates a bar graph representing the balance for each user.

    Returns:
        StreamingResponse: A streaming response containing the bar graph image.
    """
    users = await CRUD.get_all_collection("users")
    users_names = []
    users_expenses = []
    for u in users:
        users_names.append(u['name'])
        users_expenses.append(await get_expenses(u['id']).get('sum'))
    plt.bar(users_names, users_expenses, color='red')
    plt.title('Users Balance Bar Graph')
    plt.xlabel('Users')
    plt.ylabel('Balance')
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()
    return StreamingResponse(io.BytesIO(img_bytes.read()), media_type="image/png")
