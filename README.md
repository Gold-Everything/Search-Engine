# RPI Content Search-Engine
### Large Scale Programming & Testing 2019

## How to run

1. Have pipenv installed, `pip install pipenv`
2. Installed the package dependencies via `pipenv install --system`
3. Run `python manage.py runserver [port]` within `[project root]/src`

## How to test

1. Have `pytest` installed. Should be if you installed the dependencies.
2. `pytest` provides a simple interface for unit testing. Prefix or suffix the name of your test functions with "test" and they will be automatically evaluted when you run `pytest`

## Adding packages

1. You should add python packages via `pipenv install [pkg name]` so that it's automatically added the the pipfile. That way anyone is able to easily install dependencies.

#### Architecture

Backend: Django
Frontend: React

#### Design

Send raw(?) query to ranking team API, get list of document ids ranked by relevance. Send that off to document data store to get actual documents. Generate a blurb for each document, display score (maybe), generate a results view. (Basic idea is the goal for now)

#### Contributing

Pull requests are open. Hopefully travis will check whether it conforms to certain stuff.
