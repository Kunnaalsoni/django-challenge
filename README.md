# django-challenge
A challenge for Frontend Development role at Avkara Technologies Private Limited.

This is a challenge for Django development internship.
Django is a high level web framework that runs on Python. Read more at https://www.djangoproject.com/

Instructions to run this project.

Prerequisites:
Python(https://www.python.org/)
Virtualenv(https://pypi.org/project/virtualenv/)

1. Clone this repository
2. In your command line, navigate to project level directory and run the following command:
    pip install -r requirements.txt
3. After installation of all packages, run the following command:
    python manage.py migrate
4. This will create a sqlite3 database in project level directory.
5. Then, run:
    python manage.py makemigrations Features
6. Finally, run:
    python manage.py runserver
