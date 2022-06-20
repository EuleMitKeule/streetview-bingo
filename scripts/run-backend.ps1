If (!(test-path "venv"))
{
    python -m venv venv
}

.\venv\Scripts\activate.ps1

pip install --upgrade pip
pip install -r requirements.txt

flask openapi write openapi.json
flask run