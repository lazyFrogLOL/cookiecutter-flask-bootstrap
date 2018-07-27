from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.models import db, User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}