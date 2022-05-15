FROM python:3.10-alpine

WORKDIR /app

COPY ./ /app/

RUN pip install -r /app/backend/requirements.txt

CMD ["python", "/app/backend/main.py"]