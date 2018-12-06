from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from {{cookiecutter.app_name}}.models import User


class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        self.message = message if message else '已被占用'

    def __call__(self, form, field):
        check = self.model.query.filter(self.field==field.data).first()
        if check:
            raise ValidationError(self.message)


class LoginForm(FlaskForm):
    username = StringField('用户名', [DataRequired()])
    password = PasswordField('密码', [DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    username = StringField('用户名', [DataRequired(), Unique(User, User.username, '该用户名已存在')])
    email = StringField('邮箱', [Email(), DataRequired(), Unique(User, User.email, '该邮箱已被占用')])
    password = PasswordField('密码', [DataRequired()])
    confirm = PasswordField('确认密码', [DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')
