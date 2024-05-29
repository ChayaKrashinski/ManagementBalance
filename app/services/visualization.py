import matplotlib.pyplot as plt
from app.routes import balance_routes,user_routes
async def expense_and_revenue_by_date(user_id: str):
    """
    Generate a graph showing expenses and revenues over time for a specific user.

    Args:
        user_id (str): The ID of the user.

    Raises:
        Exception: If there is an error during the process.

    Returns:
        None
    """
    try:
        expenses = await expense_service.get_expenses(user_id)
        revenues = await revenue_service.get_revenues(user_id)
        expenses = sorted(expenses, key=lambda expense: expense['date'])
        expense_dates = [expense['date'] for expense in expenses]
        expense_amounts = [expense['amount'] for expense in expenses]
        revenues = sorted(revenues, key=lambda revenue: revenue['date'])
        revenue_dates = [revenue['date'] for revenue in revenues]
        revenue_amounts = [revenue['amount'] for revenue in revenues]

        plt.figure(figsize=(10, 6))
        plt.plot(expense_dates, expense_amounts, 'o-', label='Expenses')
        plt.plot(revenue_dates, revenue_amounts, 'o-', label='Revenues')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title(f'Revenues & Expenses for User ID = {user_id}')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        raise e

