FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn asyncpg python-dotenv

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
