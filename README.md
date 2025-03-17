Set-ExecutionPolicy RemoteSigned

python -m venv av
av\Scripts\activate
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
pip install jupyter
python -m ipykernel install --user --name=av --display-name "Python (av)"