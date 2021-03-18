FROM python:3.9

ADD backend /app/backend
ADD frontend/dist /app/frontend/dist

RUN ls -la

WORKDIR /app/

RUN pip install -r /app/backend/requirements.txt

CMD [ "python", "./backend/main.py" ]