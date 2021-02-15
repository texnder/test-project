FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /fastapi

COPY . .

RUN pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
