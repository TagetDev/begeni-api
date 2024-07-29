FROM python:3.11.9

WORKDIR /api

COPY requirements.txt .


RUN  pip install --upgrade pip && pip install -r requirements.txt # Install dependencies
 
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

