cd example_project

python3 -m venv venv

source venv/bin/activate

pip install numpy

pip install -r requirements.txt 

deactivate

pip freeze > requirements.txt