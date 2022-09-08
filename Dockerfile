FROM python:3.8

WORKDIR /usr/app

COPY requirements.txt ./


RUN pip install -r requirements.txt 

COPY ./ ./



CMD ["python", "./application/main.py"]