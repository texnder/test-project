from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:918918918@localhost/socialnetwork"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# conn = psycopg2.connect(
#             host= "localhost",
#             database= "socialnetwork",
#             user = "postgres",
#             password = "918918918"
#         )
# cursor = conn.cursor()

# create_users_table = cursor.execute(
#     'CREATE TABLE users( \
#         id SERIAL PRIMARY KEY, \
#         username VARCHAR(32) UNIQUE  NOT NULL, \
#         password VARCHAR(256) NOT NULL, \
#         created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, \
#         updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP \
#     );'
# )

# cursor.close()
# conn.close()

# # create posts table
# create_posts_table = pg.execute(
#     'CREATE TABLE posts( \
#         id SERIAL PRIMARY KEY, \
#         title VARCHAR(400)  NOT NULL, \
#         caption VARCHAR(400), \
#         body TEXT NOT NULL, \
#         user_id INTEGER REFERENCES users(id), \
#         created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, \
#         updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, \
#         deleted_at TIMESTAMP WITH TIME ZONE DEFAULT NULL \
#     );'
# )

class Users(BaseModel):
    username: str
    password: str

class Posts(BaseModel):
    title: str
    caption: str
    body: str
    user_id: int

app = FastAPI()

@app.get('/')
def home():
    return (
        "api test page!!"
    )

@app.get('/get-all-users')
async def get_all_users():
    data = pg.execute("select * from users")
    result = data.fetch_all
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
