FROM python:3.9

WORKDIR /app/

ADD ./backend ./
ADD ./frontend ./

RUN ls -la

RUN pip install -r ./backend/requirements.txt

CMD [ "python", "./backend/main.py" ]