# CSE 3200: System Development Project

This project uses [python](https://www.python.org/) version 3.11.1 and [Django](https://www.djangoproject.com/) version 4.1.4

## Create a virtual environment

- Run `python -m venv venv` to create a virtual environment

## Activate the virtual environment

- Run `venv\Scripts\activate` to activate the virtual environment

## Installing the Dependencies

- Run `python -m pip install -r requirements.txt` to install the dependencies.
- Check if the dependencies are installed by running `pip freeze`
- Check the Django version by running `python -m django --version`

It is recommended to use a virtual environment.

## Run the Server

If no errors from migrations

- Run `python manage.py runserver` to run the server
- The server should open in `http://localhost:8000/` or `http://127.0.0.1:8000/`
- Use `Ctrl + C` or `Ctrl + pause/break` to shut down the server

## Applying the Migrations

Go to the project root directory

- Run `python manage.py makemigrations` to make migration files
- Run `python manage.py migrate` to apply the migrations to the database
- Run `python manage.py check` to check for any errors

## Accessing the Admin Panel
python manage.py createsuperuser
- Run `` to create a superuser to log into the admin panel
- Give `username, email & password` of choice
- Go to `http://localhost:8000/admin/` to log into the admin panel

## Testing

- Run `python manage.py test` to test the application

## Deactivating the virtual environment

- Run `deactivate` to deactivate the virtual environment

## Further Help

To get more help on Django Command line run `python manage.py help` or go check out the [django-admin and manage.py](https://docs.djangoproject.com/en/3.1/ref/django-admin/) page.
