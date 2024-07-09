# Hi Flask

Is a microservice that allows you to save greetings in the database, consult them and use them as required in other services.

## Use Docker to run the application

To build the containers for this application you need to run:

´´´
$ docker compose build
´´´

And then you can execute the containers by using:

´´´
$ docker compose up
´´´

Then you need to run the migrations and create the application tables in the container DB, run in another terminal (with the hi-flask container running):

´´´
$ docker compose exec hi-flask python src/manage.py create_db
´´´

## Run in a local environment

This project was developed using Flask, the steps to install it in a local machine are:

1. In a terminal, get into the root folder of the hi_flask project and create a Python virtual environment, using python3-venv:

´´´
$ python3 -m venv env
´´´

Activate your virtual environment, you will see the environment in parenthesis in your command line:

´´´
$ source env/bin/activate
(env) $
´´´

2. Install the requirements:

```
(env) $ pip install requirements.txt
```

## Create a Database and adding settings

You need to create a database and add the URI for connect with it in the src/settings.py file, updating the value of SQLALCHEMY_DATABASE_URI

Also, to add the SECRET_KEY of your application, you could use:

```
python3 -c 'import secrets; print(secrets.token_hex())'
```

## Run the server

To run the project on the localhost server:

```
(env) $ python src/app.py
```

# Test the application

Then in a browser or using Postman you can access to your system putting in your search bar the url that connect with your server `localhost:8080`.

The available routes are:

GET /saludos/: List of the saved greetings.
POST /saludos/: Save a new greeting.
GET /saludos/{id}: Get the greeting that match with the requested id.
