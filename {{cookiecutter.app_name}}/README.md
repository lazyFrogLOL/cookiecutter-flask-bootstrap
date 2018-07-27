# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

## 快速上手

### 环境搭建

``` bash
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
cd {{cookiecutter.app_name}}
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 本地测试

``` bash
export FLASK_APP={{cookiecutter.app_name}}.py
export FLASK_DEBUG=1
flask run
```

### 数据库迁移

``` bash
flask db init
flask db migrate
flask db upgrade
```