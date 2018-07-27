import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SITE_NAME = {{cookiecutter.app_name}}
    GITHUB_USERNAME = {{cookiecutter.github_username}}
    EMAIL = {{cookiecutter.email}}
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f43hrt53et53'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False