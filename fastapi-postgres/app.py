from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import schema
import crud
from models import users
from db import engine, SessionLocal

users.Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.get('/')
def home():
    return (
        "api test page!!"
    )

@app.get('/get-all-users')
async def get_all_users():
    return {}

# @app.get('/get-user-by-id/{user_id}')
# async def get_by_id(user_id: int):
#     pass

# @app.post('/create-new-user')
# async def post():
#     pass

# @app.delete('/delete-user-by-id/{user_id}')
# async def delete(user_id : int):
#     pass

# @app.update('/update-user/{user_id}')
# async def update(user_id: int):
#     pass

# @app.put('/put-user')
# def put():
#     pass
