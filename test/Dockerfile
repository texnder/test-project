FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /fastapi

COPY . .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
