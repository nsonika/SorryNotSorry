FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 7000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload", "--port=7000"]