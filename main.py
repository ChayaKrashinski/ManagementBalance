import uvicorn as uvicorn
from fastapi import FastAPI

# from app.db_management.connection import get_db
from app.routes.user_routes import user_router

app = FastAPI()
app.include_router(router=user_router, prefix='/user')

if __name__ == '__main__':
    # get_db()
    uvicorn.run(app, host="127.0.0.1", port=8000)

