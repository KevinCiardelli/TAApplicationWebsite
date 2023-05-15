# SWEagles

## Getting Started

### Install Django using 
    pip install django
### Install crispy forms
	pip install django-crispy-forms
### Install crispy bootstrap4
	pip install django-crispy-bootstrap4
##### If the above does not work, try:
    pip install git+https://github.com/django-crispy-forms/crispy-bootstrap4.git

### Install multiselectfield
    pip install django-multiselectfield


## Running the Server
    cd mysite (change directory to mysite folder)
    python manage.py migrate
    python manage.py runserver
##### If calling python raises an error, try replacing it with "python3":
    python3 manage.py migrate
    python3 manage.py runserver
