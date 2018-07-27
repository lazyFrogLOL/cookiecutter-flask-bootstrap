from flask import Blueprint

bp = Blueprint('auth', __name__)

from {{cookiecutter.app_name}}.auth import routes