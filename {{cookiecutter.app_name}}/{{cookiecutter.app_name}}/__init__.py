from flask import Flask
from config import Config
from {{cookiecutter.app_name}}.extensions import *
from {{cookiecutter.app_name}}.models import db, User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    debugtoolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

    from {{cookiecutter.app_name}}.main import bp as main_bp
    app.register_blueprint(main_bp)

    from {{cookiecutter.app_name}}.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from {{cookiecutter.app_name}}.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}

    return app
