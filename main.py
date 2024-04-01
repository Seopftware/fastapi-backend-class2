from fastapi import FastAPI
from routes.users import router as user_router

app = FastAPI()

app.include_router(user_router) # django => settings.py, urls.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True) # python main.py

    # 127.0.0.1:8000/docs => CRUD test


    # pip install pymysql