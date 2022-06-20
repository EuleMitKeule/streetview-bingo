#!/usr/bin/env bash

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

flask openapi write openapi.json
flask run