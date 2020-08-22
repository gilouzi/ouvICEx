python3 -m venv ouvicex_env
source ouvicex_env/bin/activate
pip install -r requirements.txt
export FLASK_APP=ouvICEx/init_flask.py
python3 ouvICEx/init_flask.py
