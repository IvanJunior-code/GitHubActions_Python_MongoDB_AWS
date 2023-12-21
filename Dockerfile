FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app /app

RUN pip install --no-cache-dir \
    uvicorn \
    gunicorn \
    fastapi \
    motor

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
