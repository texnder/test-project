import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:918918918@127.0.0.1:5432/socialnetwork"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class pg:
    @classmethod
    def connect(cls):
        cls.conn = psycopg2.connect(
            host= "localhost",
            database= "socialnetwork",
            user = "postgres",
            password = "918918918"
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def execute(cls, sql: str):
        cls.connect()
        cls.cursor.execute(sql)
        cls.close()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.conn.close()

