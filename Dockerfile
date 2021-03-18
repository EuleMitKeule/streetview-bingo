FROM python:3.9-alpine

ADD backend /app/backend
ADD frontend/dist /app/frontend/dist

RUN ls -la
RUN chmod 777 -R /app

WORKDIR /app/

RUN pip install -r /app/backend/requirements.txt

CMD [ "python", "./backend/main.py" ]