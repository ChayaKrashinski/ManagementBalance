import uvicorn as uvicorn
from fastapi import FastAPI

from app.routes.balance_routes import balance_router
from app.routes.user_routes import *
from app.routes.visualization_routes import *

app = FastAPI()
app.include_router(router=user_router,  prefix='/user',tags=["users"] )
app.include_router(router=balance_router, prefix='/balance', tags=["balances"])
app.include_router(router=visualization_router, prefix='/visualization', tags=["visualization"])
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

