cd example_project

python3 -m venv venv

source venv/bin/activate
python3 -m pip install --upgrade pip



pip install --upgrade pip setuptools wheel
pip install twine keyrings.google-artifactregistry-auth



pip install -r requirements.txt 

deactivate

pip freeze > requirements.txt