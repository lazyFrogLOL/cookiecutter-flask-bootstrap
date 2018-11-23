from datetime import datetime
from flask import Blueprint, render_template
from flask_login import current_user
from {{cookiecutter.app_name}}.models import User, db


bp = Blueprint('main', __name__)


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/user/<string:username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('main/user.html', user=user)
