# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

## Quick Start

### Build

``` bash
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
cd {{cookiecutter.app_name}}
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or build with docker (which is more convenient)

``` bash
docker build -t {{cookiecutter.app_name}}:latest .
docker run --name {{cookiecutter.app_name}} -d -p 8000:5000 {{cookiecutter.app_name}}:latest
```

### Run

``` bash
export FLASK_APP={{cookiecutter.app_name}}.py
export FLASK_DEBUG=1
flask run
```

### Database Migration

``` bash
flask db init
flask db migrate
flask db upgrade
```