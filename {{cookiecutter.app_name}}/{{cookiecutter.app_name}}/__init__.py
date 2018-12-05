import os
from flask import Flask, render_template
from {{cookiecutter.app_name}}.config import config
from {{cookiecutter.app_name}}.extensions import *
from {{cookiecutter.app_name}}.models import db, User
from {{cookiecutter.app_name}}.blueprints.auth import bp as auth_bp
from {{cookiecutter.app_name}}.blueprints.main import bp as main_bp
from {{cookiecutter.app_name}}.blueprints.user import bp as user_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_errors(app)

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    debugtoolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
