from {{cookiecutter.app_name}}.main import bp
from flask import render_template, current_app, g
from flask_login import current_user
from {{cookiecutter.app_name}}.models import User, db
from datetime import datetime


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.title = current_app.config['SITE_NAME']
    g.github_username = current_app.config['GITHUB_USERNAME']
    g.email = current_app.config['EMAIL']


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/user/<string:username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
