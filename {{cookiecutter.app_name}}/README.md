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

Or build with docker

``` bash
docker build -t {{cookiecutter.app_name}}:latest .
docker run --name {{cookiecutter.app_name}} -d -p 8000:5000 {{cookiecutter.app_name}}:latest
```

### Database Migration

``` bash
flask db init
flask db migrate
flask db upgrade
```

### Run

Note: Environment variables are already set in the `.env` file for local development.

``` bash
flask run
```
