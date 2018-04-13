Python 3 required.

Start by initialising  a virtual environment:
virtualenv env
.\env\Scripts\activate

Install the following packages
pip install django
pip install djangorestframework
pip install django-extension
pip install django-rest-auth
pip install requests

Proceed by running:
python manage.py migrate
python manage.py runserver

The web page will now be active at: http://127.0.0.1:8000/
