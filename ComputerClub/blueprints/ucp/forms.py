from flask import flash
from flask_login import login_user
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo

from database.controller import UsersRepository

users_repository = UsersRepository()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')

    def validate_username(self, username):
        __user = users_repository.get_user(payload={'username': username.data})
        if __user is None or not __user.check_password(self.password.data):
            flash(f'Invalid username or password')
            raise ValidationError()
        login_user(__user, remember=self.remember.data)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('E-mail', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        __user = users_repository.get_user(payload={'username': username.data})
        if __user is not None:
            raise ValidationError('The given username is taken. Use another')

    def validate_email(self, email):
        __user = users_repository.get_user(payload={'email': email.data})
        if __user is not None:
            raise ValidationError('The given E-Mail is taken. Use another')


# todo create RecoveryForm
class RecoveryForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('E-mail')
    submit = SubmitField('Restore account')
