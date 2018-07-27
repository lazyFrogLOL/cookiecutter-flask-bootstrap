from flask import Blueprint

bp = Blueprint('main', __name__)

from {{cookiecutter.app_name}}.main import routes