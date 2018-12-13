# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

## Quick Start

### Build

You can build with [pipenv](https://github.com/pypa/pipenv)

``` bash
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
cd {{cookiecutter.app_name}}
pipenv install --dev
pipenv shell
```

### Database Migration

``` bash
flask db init
flask db migrate
flask db upgrade
```

### Run

Note: Environment variables are already set in the `.flaskenv` file for local development, change if you want.

``` bash
flask run
```

### Test

``` bash
pipenv run test
pipenv run coverage
```