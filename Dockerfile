FROM python:3.10-alpine

WORKDIR /app

COPY ./backend /app/backend
COPY ./frontend/dist /app/frontend/dist

RUN pip install -r /app/backend/requirements.txt

CMD ["python", "/app/backend/main.py"]