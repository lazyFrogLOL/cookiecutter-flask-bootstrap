from flask import Blueprint

bp = Blueprint('errors', __name__)

from {{cookiecutter.app_name}}.errors import handlers