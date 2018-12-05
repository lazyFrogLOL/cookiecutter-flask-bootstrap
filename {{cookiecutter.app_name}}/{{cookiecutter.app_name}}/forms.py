from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from {{cookiecutter.app_name}}.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户不存在')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(password=field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[Email(), DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被占用')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被占用')
