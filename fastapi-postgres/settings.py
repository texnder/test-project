import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
# SECRET_KEY = os.getenv("EMAIL")
DATABASE_URL = os.getenv("DB_URL")