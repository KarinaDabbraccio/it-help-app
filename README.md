# IT Help App

IT Help is a web application that uses the Django techstack with PostgreSQL

## Installation using Anaconda

Use the package manager [conda](https://docs.anaconda.com/anaconda/user-guide/) to install the following:

- [python](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) (>=3.10.0)
- [pip](https://anaconda.org/anaconda/pip) (>=21.2.4)
- [django](https://anaconda.org/anaconda/django) (>=3.2.5)

Ensure that the virtual python environment uses [pip](https://anaconda.org/anaconda/pip) to install the following packages:

- [django-dotenv](https://github.com/jpadilla/django-dotenv) (>=1.4.2) for environment setup
- [psycopg2](https://pypi.org/project/psycopg2/) (>=2.9.3) for integration with PostgreSQL 14

Finally, install [PostgreSQL](https://www.postgresql.org/download/) locally and follow the installation guide. Ensure that it is running on `localhost:5432`.

## Set up .env

Create an .env file in your root directory with the following information:
```
DJANGO_ENV=development
DJANGO_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Running in Python (in the following order)

1. `python manage.py makemigrations` (Create migrations for the database)
2. `python manage.py migrate` (Perform migration)
3. Run one of the following
- `python manage.py test` (Run tests locally)
- `python manage.py runserver` (Run server locally)

## Initializing the database with sample data

Optional:
`python manage.py flush` 
Clears all the current data in your database

`python manage.py loaddata data_init.json` 
Overwrites the first 5/6 rows of data for each model, including any superusers

An admin with the username `admin_tester` and password `P455w0rd!` will be created. All other accounts have the password `ithelpticket`.

OR

You can create your own admin account with the following command.
`python manage.py createsuperuser` 

See the [Django Docs](https://docs.djangoproject.com/en/4.0/) for more info.
