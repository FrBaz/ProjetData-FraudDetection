FROM python:3.10

WORKDIR /app

COPY ./app ./app
COPY ./model ./model
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
