python3 -m venv virt
source "virt/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
pip list
export PATH=$PATH:/usr/local/python3/bin
