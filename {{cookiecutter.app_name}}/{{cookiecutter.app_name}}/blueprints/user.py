from flask import Blueprint, render_template
from {{cookiecutter.app_name}}.models import User, db


bp = Blueprint('user', __name__)


@bp.route('/<string:username>')
def index(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user/index.html', user=user)
