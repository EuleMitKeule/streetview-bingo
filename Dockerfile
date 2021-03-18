FROM python:3.9

WORKDIR /app/

ADD ./backend ./backend
ADD ./frontend/dist/frontend ./frontend/dist/frontend

RUN ls -la

RUN pip install -r ./backend/requirements.txt

CMD [ "python", "./backend/main.py" ]