FROM python:3.9

RUN mkdir /app/backend
ADD backend /app/backend/
RUN mkdir /app/frontend/dist
ADD frontend/dist /app/frontend/dist

RUN ls -la

WORKDIR /app/

RUN pip install -r /app/backend/requirements.txt

CMD [ "python", "./backend/main.py" ]